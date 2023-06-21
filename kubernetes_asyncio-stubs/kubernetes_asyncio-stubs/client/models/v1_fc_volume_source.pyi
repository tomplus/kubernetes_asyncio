import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1FCVolumeSource:
    fs_type: typing.Optional[str]
    lun: typing.Optional[int]
    read_only: typing.Optional[bool]
    target_ww_ns: typing.Optional[list[str]]
    wwids: typing.Optional[list[str]]
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., lun: typing.Optional[int] = ..., read_only: typing.Optional[bool] = ..., target_ww_ns: typing.Optional[list[str]] = ..., wwids: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1FCVolumeSourceDict:
        ...
class V1FCVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    lun: typing.Optional[int]
    readOnly: typing.Optional[bool]
    targetWWNs: typing.Optional[list[str]]
    wwids: typing.Optional[list[str]]
