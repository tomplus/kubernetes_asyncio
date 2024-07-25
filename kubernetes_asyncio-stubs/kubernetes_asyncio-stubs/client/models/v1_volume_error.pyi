import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VolumeError:
    message: typing.Optional[str]
    time: typing.Optional[datetime.datetime]
    
    def __init__(self, *, message: typing.Optional[str] = ..., time: typing.Optional[datetime.datetime] = ...) -> None:
        ...
    def to_dict(self) -> V1VolumeErrorDict:
        ...
class V1VolumeErrorDict(typing.TypedDict, total=False):
    message: typing.Optional[str]
    time: typing.Optional[datetime.datetime]
