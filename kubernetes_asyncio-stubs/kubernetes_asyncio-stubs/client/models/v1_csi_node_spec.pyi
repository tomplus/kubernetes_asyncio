import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CSINodeSpec:
    drivers: list[kubernetes_asyncio.client.V1CSINodeDriver]
    
    def __init__(self, *, drivers: list[kubernetes_asyncio.client.V1CSINodeDriver]) -> None:
        ...
    def to_dict(self) -> V1CSINodeSpecDict:
        ...
class V1CSINodeSpecDict(typing.TypedDict, total=False):
    drivers: list[kubernetes_asyncio.client.V1CSINodeDriverDict]
