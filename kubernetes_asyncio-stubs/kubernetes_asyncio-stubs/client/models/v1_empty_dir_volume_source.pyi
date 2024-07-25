import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EmptyDirVolumeSource:
    medium: typing.Optional[str]
    size_limit: typing.Optional[str]
    
    def __init__(self, *, medium: typing.Optional[str] = ..., size_limit: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1EmptyDirVolumeSourceDict:
        ...
class V1EmptyDirVolumeSourceDict(typing.TypedDict, total=False):
    medium: typing.Optional[str]
    sizeLimit: typing.Optional[str]
