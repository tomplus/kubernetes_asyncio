import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1APIGroupList:
    api_version: typing.Optional[str]
    groups: list[kubernetes_asyncio.client.V1APIGroup]
    kind: typing.Optional[str]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., groups: list[kubernetes_asyncio.client.V1APIGroup], kind: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1APIGroupListDict:
        ...
class V1APIGroupListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    groups: list[kubernetes_asyncio.client.V1APIGroupDict]
    kind: typing.Optional[str]
