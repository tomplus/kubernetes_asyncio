import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VolumeAttachmentSource:
    inline_volume_spec: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeSpec]
    persistent_volume_name: typing.Optional[str]
    
    def __init__(self, *, inline_volume_spec: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeSpec] = ..., persistent_volume_name: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1VolumeAttachmentSourceDict:
        ...
class V1VolumeAttachmentSourceDict(typing.TypedDict, total=False):
    inlineVolumeSpec: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeSpecDict]
    persistentVolumeName: typing.Optional[str]
