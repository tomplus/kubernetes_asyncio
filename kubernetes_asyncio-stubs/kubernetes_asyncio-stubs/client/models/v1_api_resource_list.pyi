import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1APIResourceList:
    api_version: typing.Optional[str]
    group_version: str
    kind: typing.Optional[str]
    resources: list[kubernetes_asyncio.client.V1APIResource]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., group_version: str, kind: typing.Optional[str] = ..., resources: list[kubernetes_asyncio.client.V1APIResource]) -> None:
        ...
    def to_dict(self) -> V1APIResourceListDict:
        ...
class V1APIResourceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    groupVersion: str
    kind: typing.Optional[str]
    resources: list[kubernetes_asyncio.client.V1APIResourceDict]
