import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PhotonPersistentDiskVolumeSource:
    fs_type: typing.Optional[str]
    pd_id: str
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., pd_id: str) -> None:
        ...
    def to_dict(self) -> V1PhotonPersistentDiskVolumeSourceDict:
        ...
class V1PhotonPersistentDiskVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    pdID: str
