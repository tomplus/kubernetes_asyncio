import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1AllowedCSIDriver:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1beta1AllowedCSIDriverDict:
        ...
class V1beta1AllowedCSIDriverDict(typing.TypedDict, total=False):
    name: str
