import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeCondition:
    last_heartbeat_time: typing.Optional[datetime.datetime]
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
    
    def __init__(self, *, last_heartbeat_time: typing.Optional[datetime.datetime] = ..., last_transition_time: typing.Optional[datetime.datetime] = ..., message: typing.Optional[str] = ..., reason: typing.Optional[str] = ..., status: str, type: str) -> None:
        ...
    def to_dict(self) -> V1NodeConditionDict:
        ...
class V1NodeConditionDict(typing.TypedDict, total=False):
    lastHeartbeatTime: typing.Optional[datetime.datetime]
    lastTransitionTime: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
