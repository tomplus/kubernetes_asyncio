import kubernetes_asyncio.client
import typing

class CoreApi:
    def __init__(self, api_client: typing.Optional[kubernetes_asyncio.client.api_client.ApiClient] = ...) -> None:
        ...
    async def get_api_versions(self) -> kubernetes_asyncio.client.V1APIVersions:
        ...
