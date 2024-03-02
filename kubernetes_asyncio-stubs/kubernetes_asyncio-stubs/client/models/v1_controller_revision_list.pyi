import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ControllerRevisionList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1ControllerRevision]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.V1ControllerRevision], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> V1ControllerRevisionListDict:
        ...
class V1ControllerRevisionListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1ControllerRevisionDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
