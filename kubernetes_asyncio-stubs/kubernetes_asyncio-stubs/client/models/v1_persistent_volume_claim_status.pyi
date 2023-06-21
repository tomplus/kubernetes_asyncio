import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolumeClaimStatus:
    access_modes: typing.Optional[list[str]]
    allocated_resources: typing.Optional[dict[str, str]]
    capacity: typing.Optional[dict[str, str]]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1PersistentVolumeClaimCondition]]
    phase: typing.Optional[str]
    resize_status: typing.Optional[str]
    
    def __init__(self, *, access_modes: typing.Optional[list[str]] = ..., allocated_resources: typing.Optional[dict[str, str]] = ..., capacity: typing.Optional[dict[str, str]] = ..., conditions: typing.Optional[list[kubernetes_asyncio.client.V1PersistentVolumeClaimCondition]] = ..., phase: typing.Optional[str] = ..., resize_status: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1PersistentVolumeClaimStatusDict:
        ...
class V1PersistentVolumeClaimStatusDict(typing.TypedDict, total=False):
    accessModes: typing.Optional[list[str]]
    allocatedResources: typing.Optional[dict[str, str]]
    capacity: typing.Optional[dict[str, str]]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1PersistentVolumeClaimConditionDict]]
    phase: typing.Optional[str]
    resizeStatus: typing.Optional[str]
