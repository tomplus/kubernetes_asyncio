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

"""
Shows async port-forward streaming using an nginx container.

Creates (or reuses) a pod named ``portforward-example`` and opens an HTTP
connection to port 80 through ``kubernetes_asyncio.stream.portforward``.
"""

import asyncio

from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.client.rest import ApiException
from kubernetes_asyncio.stream import WsApiClient, portforward

POD_NAME = "portforward-example"
NAMESPACE = "default"
PORT = 80


async def ensure_nginx_pod(v1: client.CoreV1Api) -> None:
    try:
        await v1.read_namespaced_pod(name=POD_NAME, namespace=NAMESPACE)
        print(f"Pod {POD_NAME} already exists.")
        return
    except ApiException as exc:
        if exc.status != 404:
            raise

    print(f"Pod {POD_NAME} does not exist. Creating it...")
    manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": POD_NAME},
        "spec": {
            "containers": [
                {
                    "image": "nginx",
                    "name": "nginx",
                    "ports": [{"containerPort": PORT}],
                }
            ]
        },
    }
    await v1.create_namespaced_pod(body=manifest, namespace=NAMESPACE)

    while True:
        pod = await v1.read_namespaced_pod(name=POD_NAME, namespace=NAMESPACE)
        if pod.status.phase != "Pending":
            break
        await asyncio.sleep(1)
    print("Pod is ready.")


async def main() -> None:
    await config.load_kube_config()

    async with ApiClient() as api:
        await ensure_nginx_pod(client.CoreV1Api(api))

    async with WsApiClient() as ws_api:
        v1 = client.CoreV1Api(ws_api)
        async with portforward(
            v1.connect_get_namespaced_pod_portforward,
            POD_NAME,
            NAMESPACE,
            ports=PORT,
        ) as pf:
            sock = pf.socket(PORT)
            sock.setblocking(True)
            sock.sendall(b"GET / HTTP/1.1\r\n")
            sock.sendall(b"Host: 127.0.0.1\r\n")
            sock.sendall(b"Connection: close\r\n")
            sock.sendall(b"Accept: */*\r\n")
            sock.sendall(b"\r\n")

            response = b""
            while True:
                chunk = await asyncio.get_running_loop().run_in_executor(
                    None, sock.recv, 1024
                )
                if not chunk:
                    break
                response += chunk
            sock.close()

            print(response.decode("utf-8", errors="replace"))
            error = pf.error(PORT)
            if error is None:
                print(f"No port forward errors on port {PORT}.")
            else:
                print(f"Port {PORT} has the following error: {error}")


if __name__ == "__main__":
    asyncio.run(main())
