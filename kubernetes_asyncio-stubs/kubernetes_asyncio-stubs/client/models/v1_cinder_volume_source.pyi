import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CinderVolumeSource:
    fs_type: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference]
    volume_id: str
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., read_only: typing.Optional[bool] = ..., secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference] = ..., volume_id: str) -> None:
        ...
    def to_dict(self) -> V1CinderVolumeSourceDict:
        ...
class V1CinderVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReferenceDict]
    volumeID: str
