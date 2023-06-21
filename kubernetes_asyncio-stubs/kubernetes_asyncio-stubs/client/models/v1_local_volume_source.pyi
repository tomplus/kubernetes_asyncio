import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LocalVolumeSource:
    fs_type: typing.Optional[str]
    path: str
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., path: str) -> None:
        ...
    def to_dict(self) -> V1LocalVolumeSourceDict:
        ...
class V1LocalVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    path: str
