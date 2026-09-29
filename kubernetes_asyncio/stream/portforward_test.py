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

import asyncio
import struct
from unittest import IsolatedAsyncioTestCase

from aiohttp import WSMsgType

from kubernetes_asyncio.stream.portforward import PortForward, _normalize_ports


def _init_frame(channel: int, port: int) -> bytes:
    return bytes([channel]) + struct.pack("<H", port)


class _FakeWSMessage:
    def __init__(self, data: bytes, msg_type=WSMsgType.BINARY) -> None:
        self.data = data
        self.type = msg_type


class FakeWebSocket:
    def __init__(self, incoming: list[bytes]) -> None:
        self._incoming: asyncio.Queue = asyncio.Queue()
        for item in incoming:
            self._incoming.put_nowait(item)
        self.sent: list[bytes] = []
        self.closed = False

    def push(self, data: bytes) -> None:
        self._incoming.put_nowait(data)

    def close_incoming(self) -> None:
        self._incoming.put_nowait(None)

    async def receive(self):
        data = await self._incoming.get()
        if data is None:
            self.closed = True
            return _FakeWSMessage(b"", WSMsgType.CLOSED)
        return _FakeWSMessage(data)

    async def send_bytes(self, data: bytes) -> None:
        self.sent.append(data)

    async def close(self) -> None:
        self.closed = True
        self.close_incoming()


class PortForwardTest(IsolatedAsyncioTestCase):
    def test_normalize_ports(self) -> None:
        self.assertEqual(_normalize_ports(80), [80])
        self.assertEqual(_normalize_ports("80,443"), [80, 443])
        self.assertEqual(_normalize_ports([80, 443]), [80, 443])
        with self.assertRaises(ValueError):
            _normalize_ports([])
        with self.assertRaises(ValueError):
            _normalize_ports("80,80")
        with self.assertRaises(ValueError):
            _normalize_ports(0)

    async def test_portforward_proxy_roundtrip(self) -> None:
        # Initial frames for data (ch 0) and error (ch 1) channels.
        ws = FakeWebSocket(
            [
                _init_frame(0, 80),
                _init_frame(1, 80),
            ]
        )

        async with PortForward(ws, ports=80) as pf:
            sock = pf.socket(80)
            sock.setblocking(True)

            # Application -> pod
            sock.sendall(b"GET / HTTP/1.1\r\n\r\n")
            for _ in range(50):
                if ws.sent:
                    break
                await asyncio.sleep(0.01)
            self.assertTrue(ws.sent)
            self.assertEqual(ws.sent[0][0], 0)
            self.assertEqual(ws.sent[0][1:], b"GET / HTTP/1.1\r\n\r\n")

            # Pod -> application
            ws.push(bytes([0]) + b"HTTP/1.1 200 OK\r\n\r\nhello")
            data = b""
            while b"hello" not in data:
                chunk = await asyncio.get_running_loop().run_in_executor(
                    None, sock.recv, 1024
                )
                if not chunk:
                    break
                data += chunk
            self.assertIn(b"hello", data)
            self.assertIsNone(pf.error(80))

        ws.close_incoming()

    async def test_portforward_error_channel(self) -> None:
        ws = FakeWebSocket(
            [
                _init_frame(0, 80),
                _init_frame(1, 80),
                bytes([1]) + b"connection refused",
            ]
        )

        async with PortForward(ws, ports=80) as pf:
            for _ in range(50):
                if pf.error(80):
                    break
                await asyncio.sleep(0.01)
            self.assertEqual(pf.error(80), "connection refused")

        ws.close_incoming()

    async def test_invalid_port_access(self) -> None:
        ws = FakeWebSocket([_init_frame(0, 80), _init_frame(1, 80)])
        async with PortForward(ws, ports=80) as pf:
            with self.assertRaises(ValueError):
                pf.socket(443)
            with self.assertRaises(ValueError):
                pf.error(443)
        ws.close_incoming()
