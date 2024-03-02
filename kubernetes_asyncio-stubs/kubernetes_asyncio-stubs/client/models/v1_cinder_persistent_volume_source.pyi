import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CinderPersistentVolumeSource:
    fs_type: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference]
    volume_id: str
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., read_only: typing.Optional[bool] = ..., secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference] = ..., volume_id: str) -> None:
        ...
    def to_dict(self) -> V1CinderPersistentVolumeSourceDict:
        ...
class V1CinderPersistentVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[kubernetes_asyncio.client.V1SecretReferenceDict]
    volumeID: str
