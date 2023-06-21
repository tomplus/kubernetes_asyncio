import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class CoreV1EventList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.CoreV1Event]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.CoreV1Event], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> CoreV1EventListDict:
        ...
class CoreV1EventListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.CoreV1EventDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
