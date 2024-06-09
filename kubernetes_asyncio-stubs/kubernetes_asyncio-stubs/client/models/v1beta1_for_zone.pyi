import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ForZone:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1beta1ForZoneDict:
        ...
class V1beta1ForZoneDict(typing.TypedDict, total=False):
    name: str
