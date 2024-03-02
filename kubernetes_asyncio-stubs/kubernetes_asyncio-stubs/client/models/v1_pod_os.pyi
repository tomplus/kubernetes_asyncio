import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodOS:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1PodOSDict:
        ...
class V1PodOSDict(typing.TypedDict, total=False):
    name: str
