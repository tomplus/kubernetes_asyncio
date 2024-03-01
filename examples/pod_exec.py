import asyncio

from kubernetes_asyncio import client, config
from kubernetes_asyncio.stream import WsApiClient


async def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    await config.load_kube_config()

    v1 = client.CoreV1Api()

    print("Try to find a pod with busybox (name busybox*) ...")
    ret = await v1.list_pod_for_all_namespaces()

    for i in ret.items:
        if i.metadata.name.startswith("busybox"):
            pod = i.metadata.name
            namespace = i.metadata.namespace
            print("Buxy box", pod, "namespace", namespace)
            break
    else:
        print("Busybox not found !")
        return

    v1_ws = client.CoreV1Api(api_client=WsApiClient())

    exec_command = [
        "/bin/sh",
        "-c",
        "echo This message goes to stderr >&2; echo This message goes to stdout",
    ]

    resp = v1_ws.connect_get_namespaced_pod_exec(
        pod,
        namespace,
        command=exec_command,
        stderr=True,
        stdin=False,
        stdout=True,
        tty=False,
    )

    ret = await resp

    print("Response: ", ret)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
