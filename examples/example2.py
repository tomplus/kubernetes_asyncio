import asyncio

from kubernetes_asyncio import client, config, watch


async def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    await config.load_kube_config()
    async with client.ApiClient() as api:

        v1 = client.CoreV1Api(api)
        count = 10
        w = watch.Watch()

        async for event in w.stream(v1.list_namespace, timeout_seconds=10):
            print("Event: {} {}".format(event['type'], event['object'].metadata.name))
            count -= 1
            if not count:
                w.stop()

        print("Ended.")
        await w.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
