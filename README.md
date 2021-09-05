# Kubernetes Python Client

![Build status](https://github.com/tomplus/kubernetes_asyncio/workflows/Tests/badge.svg)
[![PyPI version](https://badge.fury.io/py/kubernetes_asyncio.svg)](https://badge.fury.io/py/kubernetes_asyncio)
[![codecov](https://codecov.io/gh/tomplus/kubernetes_asyncio/branch/master/graph/badge.svg)](https://codecov.io/gh/tomplus/kubernetes_asyncio)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/kubernetes_asyncio.svg)](https://pypi.python.org/pypi/kubernetes_asyncio)
[![Client Capabilities](https://img.shields.io/badge/Kubernetes%20client-Silver-blue.svg?style=flat&colorB=C0C0C0&colorA=306CE8)](http://bit.ly/kubernetes-client-capabilities-badge)
[![Client Support Level](https://img.shields.io/badge/kubernetes%20client-beta-green.svg?style=flat&colorA=306CE8)](http://bit.ly/kubernetes-client-support-badge)

Asynchronous (AsyncIO) client library for the [Kubernetes](http://kubernetes.io/) API.

This library is created in the same way as official https://github.com/kubernetes-client/python but uses asynchronous version of OpenAPI Generator.
My motivation is described here: https://github.com/kubernetes-client/python/pull/324

## Installation

From [PyPi](https://pypi.python.org/pypi/kubernetes_asyncio/) directly:

```
pip install kubernetes_asyncio
```

It requires Python 3.6+

## OpenAPI generator

Starting from v9.0.0 [OpenAPI generator](https://github.com/openapitools/openapi-generator) is used to generate code instead of
swagger-codegen. This change should be transparent from the client point of view.

## Example

To list all pods:

```python
import asyncio
from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient


async def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    await config.load_kube_config()

    # use the context manager to close http sessions automatically
    async with ApiClient() as api:

        v1 = client.CoreV1Api(api)
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


## Compatibility

This library is generated in the same way as the official Kubernetes Python Library. It uses swagger-codegen and the same concepts
like streaming, watching or reading configuration. Because of an early stage of this library some differences still exist:

|  | [synchronous library kubernetes-client/python](https://github.com/kubernetes-client/python) | [this library](https://github.com/tomplus/kubernetes_asyncio/) |
|--|--------------------------------------------------------------------|---------------------------------------------------------------|
| authentication method | gcp-token, azure-token, user-token, oidc-token, user-password, in-cluster | gcp-token (only via gcloud command), user-token, oidc-token, user-password, in-cluster |
| streaming data via websocket from PODs | bidirectional | read-only is already implemented |

## Versions

This library is versioned in the same way as the synchronous library.
The scehma version has been changed with version v18.20.0. Now, first
two numbers from version are Kubernetes version (v.1.18.20). The last
number is for changes in the library not directly connected with K8s.

## Development
Install the development packages:

```bash
pip install -r requirements.txt
pip install -r test-requirements.txt
```

You can run the style checks and tests with

```bash
flake8 kubernetes_asyncio/
isort --diff kubernetes_asyncio/
nosetests
```
