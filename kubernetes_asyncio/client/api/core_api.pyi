from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.client.models import V1APIVersions
from multidict import CIMultiDictProxy
from typing import Any
from typing import Awaitable

class CoreApi:
    def __init__(self, api_client: ApiClient | None = None) -> None: ...
    def get_api_versions(self, **kwargs: Any) -> Awaitable[V1APIVersions]: ...
    def get_api_versions_with_http_info(self, **kwargs: Any) -> Awaitable[tuple[V1APIVersions, int, CIMultiDictProxy]]: ...
