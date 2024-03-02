import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolumeClaimCondition:
    last_probe_time: typing.Optional[datetime.datetime]
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
    
    def __init__(self, *, last_probe_time: typing.Optional[datetime.datetime] = ..., last_transition_time: typing.Optional[datetime.datetime] = ..., message: typing.Optional[str] = ..., reason: typing.Optional[str] = ..., status: str, type: str) -> None:
        ...
    def to_dict(self) -> V1PersistentVolumeClaimConditionDict:
        ...
class V1PersistentVolumeClaimConditionDict(typing.TypedDict, total=False):
    lastProbeTime: typing.Optional[datetime.datetime]
    lastTransitionTime: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
