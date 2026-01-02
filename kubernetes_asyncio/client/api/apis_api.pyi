from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.client.models import V1APIGroupList
from multidict import CIMultiDictProxy
from typing import Any
from typing import Awaitable

class ApisApi:
    def __init__(self, api_client: ApiClient) -> None: ...
    def get_api_versions(self, **kwargs: Any) -> Awaitable[V1APIGroupList]: ...
    def get_api_versions_with_http_info(self, **kwargs: Any) -> Awaitable[tuple[V1APIGroupList, int, CIMultiDictProxy]]: ...
