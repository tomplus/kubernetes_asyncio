from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.client.models import V1APIGroup
from multidict import CIMultiDictProxy
from typing import Any
from typing import Awaitable

class CertificatesApi:
    def __init__(self, api_client: ApiClient | None = None) -> None: ...
    def get_api_group(self, **kwargs: Any) -> Awaitable[V1APIGroup]: ...
    def get_api_group_with_http_info(self, **kwargs: Any) -> Awaitable[tuple[V1APIGroup, int, CIMultiDictProxy]]: ...
