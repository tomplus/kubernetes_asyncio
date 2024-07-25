import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LimitRangeSpec:
    limits: list[kubernetes_asyncio.client.V1LimitRangeItem]
    
    def __init__(self, *, limits: list[kubernetes_asyncio.client.V1LimitRangeItem]) -> None:
        ...
    def to_dict(self) -> V1LimitRangeSpecDict:
        ...
class V1LimitRangeSpecDict(typing.TypedDict, total=False):
    limits: list[kubernetes_asyncio.client.V1LimitRangeItemDict]
