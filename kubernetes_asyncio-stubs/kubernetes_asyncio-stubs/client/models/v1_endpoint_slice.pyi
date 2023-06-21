import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EndpointSlice:
    address_type: str
    api_version: typing.Optional[str]
    endpoints: list[kubernetes_asyncio.client.V1Endpoint]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    ports: typing.Optional[list[kubernetes_asyncio.client.DiscoveryV1EndpointPort]]
    
    def __init__(self, *, address_type: str, api_version: typing.Optional[str] = ..., endpoints: list[kubernetes_asyncio.client.V1Endpoint], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., ports: typing.Optional[list[kubernetes_asyncio.client.DiscoveryV1EndpointPort]] = ...) -> None:
        ...
    def to_dict(self) -> V1EndpointSliceDict:
        ...
class V1EndpointSliceDict(typing.TypedDict, total=False):
    addressType: str
    apiVersion: typing.Optional[str]
    endpoints: list[kubernetes_asyncio.client.V1EndpointDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    ports: typing.Optional[list[kubernetes_asyncio.client.DiscoveryV1EndpointPortDict]]
