import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1StatefulSetPersistentVolumeClaimRetentionPolicy:
    when_deleted: typing.Optional[str]
    when_scaled: typing.Optional[str]
    
    def __init__(self, *, when_deleted: typing.Optional[str] = ..., when_scaled: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1StatefulSetPersistentVolumeClaimRetentionPolicyDict:
        ...
class V1StatefulSetPersistentVolumeClaimRetentionPolicyDict(typing.TypedDict, total=False):
    whenDeleted: typing.Optional[str]
    whenScaled: typing.Optional[str]
