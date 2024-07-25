import kubernetes_asyncio.client
import typing

class LogsApi:
    def __init__(self, api_client: typing.Optional[kubernetes_asyncio.client.api_client.ApiClient] = ...) -> None:
        ...
    async def log_file_list_handler(self) -> None:
        ...
    async def log_file_handler(self, logpath: str) -> None:
        ...
