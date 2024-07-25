import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Condition:
    last_transition_time: datetime.datetime
    message: str
    observed_generation: typing.Optional[int]
    reason: str
    status: str
    type: str
    
    def __init__(self, *, last_transition_time: datetime.datetime, message: str, observed_generation: typing.Optional[int] = ..., reason: str, status: str, type: str) -> None:
        ...
    def to_dict(self) -> V1ConditionDict:
        ...
class V1ConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: datetime.datetime
    message: str
    observedGeneration: typing.Optional[int]
    reason: str
    status: str
    type: str
