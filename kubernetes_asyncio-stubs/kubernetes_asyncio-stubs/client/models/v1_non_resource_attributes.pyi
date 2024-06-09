import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NonResourceAttributes:
    path: typing.Optional[str]
    verb: typing.Optional[str]
    
    def __init__(self, *, path: typing.Optional[str] = ..., verb: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1NonResourceAttributesDict:
        ...
class V1NonResourceAttributesDict(typing.TypedDict, total=False):
    path: typing.Optional[str]
    verb: typing.Optional[str]
