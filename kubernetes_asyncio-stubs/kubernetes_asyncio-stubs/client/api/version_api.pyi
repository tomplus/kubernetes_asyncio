import kubernetes_asyncio.client
import typing

class VersionApi:
    def __init__(self, api_client: typing.Optional[kubernetes_asyncio.client.api_client.ApiClient] = ...) -> None:
        ...
    async def get_code(self) -> kubernetes_asyncio.client.VersionInfo:
        ...
