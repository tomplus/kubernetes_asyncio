import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1UserInfo:
    extra: typing.Optional[dict[str, list[str]]]
    groups: typing.Optional[list[str]]
    uid: typing.Optional[str]
    username: typing.Optional[str]
    
    def __init__(self, *, extra: typing.Optional[dict[str, list[str]]] = ..., groups: typing.Optional[list[str]] = ..., uid: typing.Optional[str] = ..., username: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1UserInfoDict:
        ...
class V1UserInfoDict(typing.TypedDict, total=False):
    extra: typing.Optional[dict[str, list[str]]]
    groups: typing.Optional[list[str]]
    uid: typing.Optional[str]
    username: typing.Optional[str]
