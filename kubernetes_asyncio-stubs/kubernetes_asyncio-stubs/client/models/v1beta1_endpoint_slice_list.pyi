import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1EndpointSliceList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1beta1EndpointSlice]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.V1beta1EndpointSlice], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1EndpointSliceListDict:
        ...
class V1beta1EndpointSliceListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1beta1EndpointSliceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
