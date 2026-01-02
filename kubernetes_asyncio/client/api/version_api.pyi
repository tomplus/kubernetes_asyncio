from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.client.models import VersionInfo
from multidict import CIMultiDictProxy
from typing import Any
from typing import Awaitable

class VersionApi:
    def __init__(self, api_client: ApiClient) -> None: ...
    def get_code(self, **kwargs: Any) -> Awaitable[VersionInfo]: ...
    def get_code_with_http_info(self, **kwargs: Any) -> Awaitable[tuple[VersionInfo, int, CIMultiDictProxy]]: ...
