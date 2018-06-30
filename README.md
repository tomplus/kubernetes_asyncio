# Kubernetes Python Client

[![Build Status](https://travis-ci.org/tomplus/kubernetes_asyncio.svg?branch=master)](https://travis-ci.org/tomplus/kubernetes_asyncio)
[![PyPI version](https://badge.fury.io/py/kubernetes_asyncio.svg)](https://badge.fury.io/py/kubernetes_asyncio)
[![codecov](https://codecov.io/gh/tomplus/kubernetes_asyncio/branch/master/graph/badge.svg)](https://codecov.io/gh/tomplus/kubernetes_asyncio)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/kubernetes_asyncio.svg)](https://pypi.python.org/pypi/kubernetes_asyncio)

Asynchronous (AsyncIO) client library for the [Kubernetes](http://kubernetes.io/) API.

This library is created in the same way as official https://github.com/kubernetes-client/python but uses asynchronous version of swagger-codegen.
My motivation is described here: https://github.com/kubernetes-client/python/pull/324

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
    await config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = await v1.list_pod_for_all_namespaces()

    for i in ret.items:
        print(i.status.pod_ip, i.metadata.namespace, i.metadata.name)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
```

More complicated examples, like asynchronous multiple watch or tail logs from pods,
you can find in `examples/` folder.


## Comparison with official synchronous library

This library is generated in the same way as the official Kubernetes Python Library. It uses swagger-codegen and the same concepts
like streaming, watching or reading configuration. Because of an early stage of this library some differences still exist:

|  | [synchronous library kubernetes-client/python](https://github.com/kubernetes-client/python) | [this libray](https://github.com/tomplus/kubernetes_asyncio/) |
|--|--------------------------------------------------------------------|---------------------------------------------------------------|
| authentication method | gcp-token, user-token, oid-token, user-password, in-cluster | gcp-token (only via gcloud command), user-token, user-password, in-cluster |
| refesh token | no | yes, optional |
| python | 2.7 3.4 3.5 3.6 | 3.5 3.6 |
| streaming data via websocket from PODs | bidirectional | read-only is already implemented |


## Development
Install the development packages:

```bash
pip install -r requirements.txt
pip install -r test-requirements.txt
```

You can run the style checks and tests with

```bash
flake8 && isort -c
nosetests
```
