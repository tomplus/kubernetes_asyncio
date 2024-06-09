import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1StorageVersionCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    observed_generation: typing.Optional[int]
    reason: str
    status: str
    type: str
    
    def __init__(self, *, last_transition_time: typing.Optional[datetime.datetime] = ..., message: typing.Optional[str] = ..., observed_generation: typing.Optional[int] = ..., reason: str, status: str, type: str) -> None:
        ...
    def to_dict(self) -> V1alpha1StorageVersionConditionDict:
        ...
class V1alpha1StorageVersionConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    observedGeneration: typing.Optional[int]
    reason: str
    status: str
    type: str
