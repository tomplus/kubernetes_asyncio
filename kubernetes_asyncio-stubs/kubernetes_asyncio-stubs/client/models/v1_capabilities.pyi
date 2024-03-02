import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Capabilities:
    add: typing.Optional[list[str]]
    drop: typing.Optional[list[str]]
    
    def __init__(self, *, add: typing.Optional[list[str]] = ..., drop: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1CapabilitiesDict:
        ...
class V1CapabilitiesDict(typing.TypedDict, total=False):
    add: typing.Optional[list[str]]
    drop: typing.Optional[list[str]]
