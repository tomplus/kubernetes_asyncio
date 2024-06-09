import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1EndpointSlice:
    address_type: str
    api_version: typing.Optional[str]
    endpoints: list[kubernetes_asyncio.client.V1beta1Endpoint]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1beta1EndpointPort]]
    
    def __init__(self, *, address_type: str, api_version: typing.Optional[str] = ..., endpoints: list[kubernetes_asyncio.client.V1beta1Endpoint], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., ports: typing.Optional[list[kubernetes_asyncio.client.V1beta1EndpointPort]] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1EndpointSliceDict:
        ...
class V1beta1EndpointSliceDict(typing.TypedDict, total=False):
    addressType: str
    apiVersion: typing.Optional[str]
    endpoints: list[kubernetes_asyncio.client.V1beta1EndpointDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1beta1EndpointPortDict]]
