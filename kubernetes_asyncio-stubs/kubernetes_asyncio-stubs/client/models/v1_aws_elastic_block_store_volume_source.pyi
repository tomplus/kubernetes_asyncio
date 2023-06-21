import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1AWSElasticBlockStoreVolumeSource:
    fs_type: typing.Optional[str]
    partition: typing.Optional[int]
    read_only: typing.Optional[bool]
    volume_id: str
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., partition: typing.Optional[int] = ..., read_only: typing.Optional[bool] = ..., volume_id: str) -> None:
        ...
    def to_dict(self) -> V1AWSElasticBlockStoreVolumeSourceDict:
        ...
class V1AWSElasticBlockStoreVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    partition: typing.Optional[int]
    readOnly: typing.Optional[bool]
    volumeID: str
