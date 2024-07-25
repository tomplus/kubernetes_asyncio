import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VsphereVirtualDiskVolumeSource:
    fs_type: typing.Optional[str]
    storage_policy_id: typing.Optional[str]
    storage_policy_name: typing.Optional[str]
    volume_path: str
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., storage_policy_id: typing.Optional[str] = ..., storage_policy_name: typing.Optional[str] = ..., volume_path: str) -> None:
        ...
    def to_dict(self) -> V1VsphereVirtualDiskVolumeSourceDict:
        ...
class V1VsphereVirtualDiskVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    storagePolicyID: typing.Optional[str]
    storagePolicyName: typing.Optional[str]
    volumePath: str
