import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1KeyToPath:
    key: str
    mode: typing.Optional[int]
    path: str
    
    def __init__(self, *, key: str, mode: typing.Optional[int] = ..., path: str) -> None:
        ...
    def to_dict(self) -> V1KeyToPathDict:
        ...
class V1KeyToPathDict(typing.TypedDict, total=False):
    key: str
    mode: typing.Optional[int]
    path: str
