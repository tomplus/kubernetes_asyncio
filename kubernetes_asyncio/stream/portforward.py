# Copyright 2026 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Async Kubernetes pod port-forward over WebSockets."""

from __future__ import annotations

import asyncio
import socket
from collections.abc import Callable
from typing import Any

from aiohttp import WSMsgType
from aiohttp.client_ws import ClientWebSocketResponse


def _normalize_ports(ports: int | str | list[int]) -> list[int]:
    if isinstance(ports, int):
        port_list = [ports]
    elif isinstance(ports, str):
        port_list = [int(p) for p in ports.split(",") if p]
    else:
        port_list = [int(p) for p in ports]

    if not port_list:
        raise ValueError("Missing required parameter `ports`")

    seen: set[int] = set()
    for port_number in port_list:
        if not (0 < port_number < 65536):
            raise ValueError(
                f"Port number must be between 0 and 65536: {port_number}"
            )
        if port_number in seen:
            raise ValueError(f"Duplicate port numbers: {port_number}")
        seen.add(port_number)
    return port_list


class _Socket:
    """Wrap a socketpair endpoint so AF_INET TCP options are ignored."""

    def __init__(self, sock: socket.socket) -> None:
        self._socket = sock

    def __getattr__(self, name: str) -> Any:
        return getattr(self._socket, name)

    def setsockopt(self, level: int, optname: int, value: Any) -> None:
        if level == socket.IPPROTO_TCP and optname == socket.TCP_NODELAY:
            return
        self._socket.setsockopt(level, optname, value)


class _Port:
    def __init__(self, ix: int, port_number: int) -> None:
        self.port_number = port_number
        # Data channel byte for this port (error channel is ix*2+1).
        self.channel = bytes((ix * 2,))
        app_sock, self.python = socket.socketpair()
        self.python.setblocking(False)
        # Application side stays blocking-compatible for sync-style I/O;
        # asyncio callers can still use run_in_executor / sock_* helpers.
        self.socket = _Socket(app_sock)
        self.error: str | None = None


class PortForward:
    """Translate Kubernetes port-forward WebSocket frames to local sockets.

    Each forwarded port exposes a socket via :meth:`socket` that applications
    can read/write as if connected directly to the pod port. A background task
    proxies bytes between those sockets and the WebSocket, matching the sync
    client's ``PortForward`` behaviour.
    """

    def __init__(
        self, websocket: ClientWebSocketResponse, ports: int | str | list[int]
    ) -> None:
        self.websocket = websocket
        self.local_ports = {
            port_number: _Port(ix, port_number)
            for ix, port_number in enumerate(_normalize_ports(ports))
        }
        self._proxy_task: asyncio.Task | None = None
        self._ready = asyncio.Event()
        self._proxy_error: BaseException | None = None

    @property
    def connected(self) -> bool:
        return not self.websocket.closed

    def socket(self, port_number: int) -> _Socket:
        if port_number not in self.local_ports:
            raise ValueError("Invalid port number")
        return self.local_ports[port_number].socket

    def error(self, port_number: int) -> str | None:
        if port_number not in self.local_ports:
            raise ValueError("Invalid port number")
        return self.local_ports[port_number].error

    async def __aenter__(self) -> PortForward:
        self._proxy_task = asyncio.create_task(self._proxy())
        await self._ready.wait()
        if self._proxy_error is not None:
            raise self._proxy_error
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    async def close(self) -> None:
        for port in self.local_ports.values():
            for sock in (port.socket, port.python):
                try:
                    sock.close()
                except OSError:
                    pass

        if self._proxy_task is not None:
            self._proxy_task.cancel()
            try:
                await self._proxy_task
            except asyncio.CancelledError:
                pass
            self._proxy_task = None

    async def _proxy(self) -> None:
        channel_ports: list[_Port] = []
        channel_initialized: list[bool] = []
        for port in self.local_ports.values():
            channel_ports.append(port)
            channel_initialized.append(False)
            channel_ports.append(port)
            channel_initialized.append(False)

        loop = asyncio.get_running_loop()
        readers = [
            asyncio.create_task(self._local_to_ws(port, loop))
            for port in self.local_ports.values()
        ]
        ws_task = asyncio.create_task(
            self._ws_to_local(channel_ports, channel_initialized, loop)
        )

        try:
            done, _ = await asyncio.wait(
                [ws_task, *readers], return_when=asyncio.FIRST_COMPLETED
            )
            for task in done:
                exc = task.exception()
                if exc is not None and not isinstance(exc, asyncio.CancelledError):
                    self._proxy_error = exc
                    self._ready.set()
                    raise exc
        finally:
            for task in [ws_task, *readers]:
                task.cancel()
            await asyncio.gather(ws_task, *readers, return_exceptions=True)
            for port in self.local_ports.values():
                try:
                    port.python.close()
                except OSError:
                    pass

    async def _ws_to_local(
        self,
        channel_ports: list[_Port],
        channel_initialized: list[bool],
        loop: asyncio.AbstractEventLoop,
    ) -> None:
        try:
            while not self.websocket.closed:
                msg = await self.websocket.receive()
                if msg.type in (WSMsgType.CLOSE, WSMsgType.CLOSING, WSMsgType.CLOSED):
                    break
                if msg.type != WSMsgType.BINARY or not msg.data:
                    continue

                channel = msg.data[0]
                if channel >= len(channel_ports):
                    raise RuntimeError(f"Unexpected channel number: {channel}")

                port = channel_ports[channel]
                if not channel_initialized[channel]:
                    if len(msg.data) != 3:
                        raise RuntimeError(
                            "Unexpected initial channel frame data size"
                        )
                    port_number = msg.data[1] + (msg.data[2] * 256)
                    if port_number != port.port_number:
                        raise RuntimeError(
                            "Unexpected port number in initial channel frame: "
                            f"{port_number}"
                        )
                    channel_initialized[channel] = True
                    if all(channel_initialized):
                        self._ready.set()
                    continue

                payload = msg.data[1:]
                if channel % 2:
                    if port.error is None:
                        port.error = ""
                    port.error += payload.decode()
                    try:
                        port.python.close()
                    except OSError:
                        pass
                elif payload:
                    await loop.sock_sendall(port.python, payload)
        except Exception as exc:
            self._proxy_error = exc
            self._ready.set()
            raise

    async def _local_to_ws(
        self, port: _Port, loop: asyncio.AbstractEventLoop
    ) -> None:
        while True:
            try:
                data = await loop.sock_recv(port.python, 1024 * 1024)
            except (ConnectionResetError, OSError):
                break
            if not data:
                break
            await self.websocket.send_bytes(port.channel + data)


class portforward:
    """Async context manager that opens a pod port-forward.

    Example::

        async with WsApiClient() as api:
            v1 = CoreV1Api(api)
            async with portforward(
                v1.connect_get_namespaced_pod_portforward,
                "nginx",
                "default",
                ports=80,
            ) as pf:
                sock = pf.socket(80)
                sock.sendall(b"GET / HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n")
                print(sock.recv(4096))
    """

    def __init__(
        self,
        api_method: Callable[..., Any],
        name: str,
        namespace: str,
        ports: int | str | list[int],
        **kwargs: Any,
    ) -> None:
        self._api_method = api_method
        self._name = name
        self._namespace = namespace
        self._ports = _normalize_ports(ports)
        self._kwargs = kwargs
        self._ws_cm: Any | None = None
        self._pf: PortForward | None = None

    async def __aenter__(self) -> PortForward:
        ports_str = ",".join(str(p) for p in self._ports)
        self._ws_cm = await self._api_method(
            self._name,
            self._namespace,
            ports=ports_str,
            _preload_content=False,
            **self._kwargs,
        )
        websocket = await self._ws_cm.__aenter__()
        self._pf = PortForward(websocket, self._ports)
        return await self._pf.__aenter__()

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._pf is not None:
            await self._pf.__aexit__(exc_type, exc, tb)
            self._pf = None
        if self._ws_cm is not None:
            await self._ws_cm.__aexit__(exc_type, exc, tb)
            self._ws_cm = None
