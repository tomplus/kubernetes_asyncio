import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeConfigStatus:
    active: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource]
    assigned: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource]
    error: typing.Optional[str]
    last_known_good: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource]
    
    def __init__(self, *, active: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource] = ..., assigned: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource] = ..., error: typing.Optional[str] = ..., last_known_good: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource] = ...) -> None:
        ...
    def to_dict(self) -> V1NodeConfigStatusDict:
        ...
class V1NodeConfigStatusDict(typing.TypedDict, total=False):
    active: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSourceDict]
    assigned: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSourceDict]
    error: typing.Optional[str]
    lastKnownGood: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSourceDict]
