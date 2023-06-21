import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1HostPathVolumeSource:
    path: str
    type: typing.Optional[str]
    
    def __init__(self, *, path: str, type: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1HostPathVolumeSourceDict:
        ...
class V1HostPathVolumeSourceDict(typing.TypedDict, total=False):
    path: str
    type: typing.Optional[str]
