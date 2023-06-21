import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VolumeNodeAffinity:
    required: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]
    
    def __init__(self, *, required: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...) -> None:
        ...
    def to_dict(self) -> V1VolumeNodeAffinityDict:
        ...
class V1VolumeNodeAffinityDict(typing.TypedDict, total=False):
    required: typing.Optional[kubernetes_asyncio.client.V1NodeSelectorDict]
