import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SELinuxOptions:
    level: typing.Optional[str]
    role: typing.Optional[str]
    type: typing.Optional[str]
    user: typing.Optional[str]
    
    def __init__(self, *, level: typing.Optional[str] = ..., role: typing.Optional[str] = ..., type: typing.Optional[str] = ..., user: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1SELinuxOptionsDict:
        ...
class V1SELinuxOptionsDict(typing.TypedDict, total=False):
    level: typing.Optional[str]
    role: typing.Optional[str]
    type: typing.Optional[str]
    user: typing.Optional[str]
