import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1GlusterfsVolumeSource:
    endpoints: str
    path: str
    read_only: typing.Optional[bool]
    
    def __init__(self, *, endpoints: str, path: str, read_only: typing.Optional[bool] = ...) -> None:
        ...
    def to_dict(self) -> V1GlusterfsVolumeSourceDict:
        ...
class V1GlusterfsVolumeSourceDict(typing.TypedDict, total=False):
    endpoints: str
    path: str
    readOnly: typing.Optional[bool]
