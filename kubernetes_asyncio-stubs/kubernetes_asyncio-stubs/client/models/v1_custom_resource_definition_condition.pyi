import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceDefinitionCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
    
    def __init__(self, *, last_transition_time: typing.Optional[datetime.datetime] = ..., message: typing.Optional[str] = ..., reason: typing.Optional[str] = ..., status: str, type: str) -> None:
        ...
    def to_dict(self) -> V1CustomResourceDefinitionConditionDict:
        ...
class V1CustomResourceDefinitionConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
