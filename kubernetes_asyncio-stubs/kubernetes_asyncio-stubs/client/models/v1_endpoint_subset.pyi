import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EndpointSubset:
    addresses: typing.Optional[list[kubernetes_asyncio.client.V1EndpointAddress]]
    not_ready_addresses: typing.Optional[list[kubernetes_asyncio.client.V1EndpointAddress]]
    ports: typing.Optional[list[kubernetes_asyncio.client.CoreV1EndpointPort]]
    
    def __init__(self, *, addresses: typing.Optional[list[kubernetes_asyncio.client.V1EndpointAddress]] = ..., not_ready_addresses: typing.Optional[list[kubernetes_asyncio.client.V1EndpointAddress]] = ..., ports: typing.Optional[list[kubernetes_asyncio.client.CoreV1EndpointPort]] = ...) -> None:
        ...
    def to_dict(self) -> V1EndpointSubsetDict:
        ...
class V1EndpointSubsetDict(typing.TypedDict, total=False):
    addresses: typing.Optional[list[kubernetes_asyncio.client.V1EndpointAddressDict]]
    notReadyAddresses: typing.Optional[list[kubernetes_asyncio.client.V1EndpointAddressDict]]
    ports: typing.Optional[list[kubernetes_asyncio.client.CoreV1EndpointPortDict]]
