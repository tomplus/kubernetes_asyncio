import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EndpointSliceList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1EndpointSlice]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.V1EndpointSlice], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> V1EndpointSliceListDict:
        ...
class V1EndpointSliceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1EndpointSliceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
