import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DownwardAPIVolumeSource:
    default_mode: typing.Optional[int]
    items: typing.Optional[list[kubernetes_asyncio.client.V1DownwardAPIVolumeFile]]
    
    def __init__(self, *, default_mode: typing.Optional[int] = ..., items: typing.Optional[list[kubernetes_asyncio.client.V1DownwardAPIVolumeFile]] = ...) -> None:
        ...
    def to_dict(self) -> V1DownwardAPIVolumeSourceDict:
        ...
class V1DownwardAPIVolumeSourceDict(typing.TypedDict, total=False):
    defaultMode: typing.Optional[int]
    items: typing.Optional[list[kubernetes_asyncio.client.V1DownwardAPIVolumeFileDict]]
