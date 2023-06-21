import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1FlowSchemaCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: typing.Optional[str]
    type: typing.Optional[str]
    
    def __init__(self, *, last_transition_time: typing.Optional[datetime.datetime] = ..., message: typing.Optional[str] = ..., reason: typing.Optional[str] = ..., status: typing.Optional[str] = ..., type: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1FlowSchemaConditionDict:
        ...
class V1beta1FlowSchemaConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: typing.Optional[str]
    type: typing.Optional[str]
