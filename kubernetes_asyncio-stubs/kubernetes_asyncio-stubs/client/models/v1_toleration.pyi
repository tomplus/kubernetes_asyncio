import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Toleration:
    effect: typing.Optional[str]
    key: typing.Optional[str]
    operator: typing.Optional[str]
    toleration_seconds: typing.Optional[int]
    value: typing.Optional[str]
    
    def __init__(self, *, effect: typing.Optional[str] = ..., key: typing.Optional[str] = ..., operator: typing.Optional[str] = ..., toleration_seconds: typing.Optional[int] = ..., value: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1TolerationDict:
        ...
class V1TolerationDict(typing.TypedDict, total=False):
    effect: typing.Optional[str]
    key: typing.Optional[str]
    operator: typing.Optional[str]
    tolerationSeconds: typing.Optional[int]
    value: typing.Optional[str]
