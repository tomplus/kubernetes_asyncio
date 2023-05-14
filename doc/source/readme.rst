Welcome to kubernetes-asyncio documentation!
============================================

Asynchronous (AsyncIO) client library for the `Kubernetes <http://kubernetes.io>`_ API.

This library is created in the same way as official https://github.com/kubernetes-client/python but uses asynchronous version of OpenAPI Generator.
My motivation is described here: https://github.com/kubernetes-client/python/pull/324

Installation
------------

From `PyPi <https://pypi.python.org/pypi/kubernetes_asyncio>`_ directly:
::

    pip install kubernetes_asyncio

It requires Python 3.6+

OpenAPI generator
-----------------

Starting from v9.0.0 `OpenAPI generator <https://github.com/openapitools/openapi-generator>`_ is used to generate code instead of
swagger-codegen. This change should be transparent from the client point of view.

Example
-------

To list all pods:
::

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

More complicated examples, like asynchronous multiple watch or tail logs from pods,
you can find in `examples/` folder.

There is also support for DynamicClient which will query the cluster for all supported
resources.  This allows for dynamic resource selection at runtime.
The above example using DynamicClient would look like this:
::

    import asyncio
    from kubernetes_asyncio import config
    from kubernetes_asyncio.client.api_client import ApiClient
    from kubernetes_asyncio.dynamic import DynamicClient


    async def main():
        # Configs can be set in Configuration class directly or using helper
        # utility. If no argument provided, the config will be loaded from
        # default location.
        await config.load_kube_config()

        # use the context manager to close http sessions automatically
        async with ApiClient() as api:
            client = await DynamicClient(api)
            v1 = await client.resources.get(api_version="v1", kind="Pod")
            print("Listing pods with their IPs:")
            ret = await v1.get()

            for i in ret.items:
                print(i.status.pod_ip, i.metadata.namespace, i.metadata.name)


    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()

Additional examples are in the `examples/dynamic-client` folder.

Versions
--------

This library is versioned in the same way as the synchronous library.
The schema version has been changed with version v18.20.0. Now, first
two numbers from version are Kubernetes version (v.1.18.20). The last
number is for changes in the library not directly connected with K8s.

Development
-----------
Install the development packages:
::

    pip install -r requirements.txt
    pip install -r test-requirements.txt

You can run the style checks and tests with
::

    flake8 kubernetes_asyncio/
    isort --diff kubernetes_asyncio/
    nosetests
