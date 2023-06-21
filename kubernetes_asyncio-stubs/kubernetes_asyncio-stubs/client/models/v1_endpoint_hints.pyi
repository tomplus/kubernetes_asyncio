import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EndpointHints:
    for_zones: typing.Optional[list[kubernetes_asyncio.client.V1ForZone]]
    
    def __init__(self, *, for_zones: typing.Optional[list[kubernetes_asyncio.client.V1ForZone]] = ...) -> None:
        ...
    def to_dict(self) -> V1EndpointHintsDict:
        ...
class V1EndpointHintsDict(typing.TypedDict, total=False):
    forZones: typing.Optional[list[kubernetes_asyncio.client.V1ForZoneDict]]
