import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DownwardAPIProjection:
    items: typing.Optional[list[kubernetes_asyncio.client.V1DownwardAPIVolumeFile]]
    
    def __init__(self, *, items: typing.Optional[list[kubernetes_asyncio.client.V1DownwardAPIVolumeFile]] = ...) -> None:
        ...
    def to_dict(self) -> V1DownwardAPIProjectionDict:
        ...
class V1DownwardAPIProjectionDict(typing.TypedDict, total=False):
    items: typing.Optional[list[kubernetes_asyncio.client.V1DownwardAPIVolumeFileDict]]
