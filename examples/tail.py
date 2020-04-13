#
# Script to print logs from container in PODs.
#
# Usage:
#       python tail.py <namespace> <prefix for pods' name> [-n LINES] [-f]
#
# Example:
#       python tail.py kube-system kube-dns -f
#
#       It will be streaming logs from all containers from PODs which name ~ "^kube-dns.*"
#

import argparse
import asyncio

from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient


def parse_args():
    parser = argparse.ArgumentParser(description='Tail for pods')
    parser.add_argument('namespace', help="k8s namespace")
    parser.add_argument('pod', help="pod name or prefix")
    parser.add_argument('-f', '--follow', action='store_true',
                        help="output appended data as the file grows")
    parser.add_argument('-n', '--lines', default=10,
                        help='show the last LINES lines')
    return parser.parse_args()


async def print_pod_log(v1_api, pod, namespace, container, lines, follow):
    if not follow:
        resp = await v1_api.read_namespaced_pod_log(pod,
                                                    namespace,
                                                    container=container,
                                                    tail_lines=lines)
        print(resp)
    else:
        resp = await v1_api.read_namespaced_pod_log(pod,
                                                    namespace,
                                                    container=container,
                                                    tail_lines=lines,
                                                    follow=True, _preload_content=False)
        while True:
            line = await resp.content.readline()
            if not line:
                break
            print(line.decode('utf-8'), end="")


async def main():
    args = parse_args()

    loader = await config.load_kube_config()
    api = ApiClient()
    v1_api = client.CoreV1Api(api)
    ret = await v1_api.list_namespaced_pod(args.namespace)
    cmd = []
    for pod in ret.items:
        if pod.metadata.name.startswith(args.pod):
            for container in pod.spec.containers:
                cmd.append(print_pod_log(v1_api,
                                         pod.metadata.name,
                                         args.namespace,
                                         container.name,
                                         args.lines,
                                         args.follow))

    if cmd == []:
        print('No matching PODs !')
        return

    if args.follow:
        # autorefresh gcp token
        cmd.append(config.refresh_token(loader))

    await asyncio.wait(cmd)
    await api.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
