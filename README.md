# Kubernetes Python Client

![Status - under heavy development](https://img.shields.io/badge/status-%20under%20heavy%20development-red.svg)

Asynchronous (AsyncIO) client library for the [Kubernetes](http://kubernetes.io/) API.

This library is created in the same way as official https://github.com/kubernetes-client/python but uses asynchronous version of swagger-codegen.

## Installation

From [PyPi](https://pypi.python.org/pypi/kubernetes_asyncio/) directly:

```
pip install kubernetes_asyncio
```

## Example

To list all pods:

```python
import asyncio
from kubernetes_asyncio import client, config


async def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = await v1.list_pod_for_all_namespaces()

    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
```

More examples you can find in `examples/` folder.
