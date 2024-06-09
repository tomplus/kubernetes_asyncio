import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1WatchEvent:
    object: typing.Any
    type: str
    
    def __init__(self, *, object: typing.Any, type: str) -> None:
        ...
    def to_dict(self) -> V1WatchEventDict:
        ...
class V1WatchEventDict(typing.TypedDict, total=False):
    object: typing.Any
    type: str
