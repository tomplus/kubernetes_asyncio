import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ScaleStatus:
    replicas: int
    selector: typing.Optional[str]
    
    def __init__(self, *, replicas: int, selector: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1ScaleStatusDict:
        ...
class V1ScaleStatusDict(typing.TypedDict, total=False):
    replicas: int
    selector: typing.Optional[str]
