import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1GroupVersionForDiscovery:
    group_version: str
    version: str
    
    def __init__(self, *, group_version: str, version: str) -> None:
        ...
    def to_dict(self) -> V1GroupVersionForDiscoveryDict:
        ...
class V1GroupVersionForDiscoveryDict(typing.TypedDict, total=False):
    groupVersion: str
    version: str
