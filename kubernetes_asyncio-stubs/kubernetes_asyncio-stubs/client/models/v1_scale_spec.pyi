import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ScaleSpec:
    replicas: typing.Optional[int]
    
    def __init__(self, *, replicas: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1ScaleSpecDict:
        ...
class V1ScaleSpecDict(typing.TypedDict, total=False):
    replicas: typing.Optional[int]
