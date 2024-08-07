import asyncio

from kubernetes_asyncio import client, config, utils
from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.stream import WsApiClient

BUSYBOX_POD = "busybox-test"


async def find_busybox_pod():
    async with ApiClient() as api:
        v1 = client.CoreV1Api(api)
        ret = await v1.list_pod_for_all_namespaces()
        for i in ret.items:
            if i.metadata.namespace == 'default' and i.metadata.name == BUSYBOX_POD:
                print(f"Found busybox pod: {i.metadata.name}")
                return i.metadata.name
    return None


async def create_busybox_pod():
    print(f"Pod {BUSYBOX_POD} does not exist. Creating it...")
    manifest = {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {
            'name': BUSYBOX_POD,
        },
        'spec': {
            'containers': [{
                'image': 'busybox',
                'name': 'sleep',
                "args": [
                    "/bin/sh",
                    "-c",
                    "while true; do date; sleep 5; done"
                ]
            }]
        }
    }
    async with ApiClient() as api:
        objects = await utils.create_from_dict(api, manifest, namespace="default")
        pod = objects[0]
        print(f"Created pod {pod.metadata.name}.")
        return pod.metadata.name


async def wait_busybox_pod_ready():
    print(f"Waiting pod {BUSYBOX_POD} to be ready.")
    async with ApiClient() as api:
        v1 = client.CoreV1Api(api)
        while True:
            ret = await v1.read_namespaced_pod(name=BUSYBOX_POD, namespace="default")
            if ret.status.phase != 'Pending':
                break
            await asyncio.sleep(1)


async def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    await config.load_kube_config()

    pod = await find_busybox_pod()
    if not pod:
        pod = await create_busybox_pod()
    await wait_busybox_pod_ready()

    # Execute a command in a pod non-interactively, and display its output
    print("-------------")
    async with WsApiClient() as ws_api:
        v1_ws = client.CoreV1Api(api_client=ws_api)
        exec_command = [
            "/bin/sh",
            "-c",
            "echo This message goes to stderr >&2; echo This message goes to stdout",
        ]
        ret = await v1_ws.connect_get_namespaced_pod_exec(
            pod,
            "default",
            command=exec_command,
            stderr=True,
            stdin=False,
            stdout=True,
            tty=False,
        )
        print(f"Response: {ret}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
