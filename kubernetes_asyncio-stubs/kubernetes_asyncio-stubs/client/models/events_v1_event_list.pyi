import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class EventsV1EventList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.EventsV1Event]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.EventsV1Event], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> EventsV1EventListDict:
        ...
class EventsV1EventListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.EventsV1EventDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
