import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1HostPortRange:
    max: int
    min: int
    
    def __init__(self, *, max: int, min: int) -> None:
        ...
    def to_dict(self) -> V1beta1HostPortRangeDict:
        ...
class V1beta1HostPortRangeDict(typing.TypedDict, total=False):
    max: int
    min: int
