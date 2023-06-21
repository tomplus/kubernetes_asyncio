import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DaemonSetStatus:
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1DaemonSetCondition]]
    current_number_scheduled: int
    desired_number_scheduled: int
    number_available: typing.Optional[int]
    number_misscheduled: int
    number_ready: int
    number_unavailable: typing.Optional[int]
    observed_generation: typing.Optional[int]
    updated_number_scheduled: typing.Optional[int]
    
    def __init__(self, *, collision_count: typing.Optional[int] = ..., conditions: typing.Optional[list[kubernetes_asyncio.client.V1DaemonSetCondition]] = ..., current_number_scheduled: int, desired_number_scheduled: int, number_available: typing.Optional[int] = ..., number_misscheduled: int, number_ready: int, number_unavailable: typing.Optional[int] = ..., observed_generation: typing.Optional[int] = ..., updated_number_scheduled: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1DaemonSetStatusDict:
        ...
class V1DaemonSetStatusDict(typing.TypedDict, total=False):
    collisionCount: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1DaemonSetConditionDict]]
    currentNumberScheduled: int
    desiredNumberScheduled: int
    numberAvailable: typing.Optional[int]
    numberMisscheduled: int
    numberReady: int
    numberUnavailable: typing.Optional[int]
    observedGeneration: typing.Optional[int]
    updatedNumberScheduled: typing.Optional[int]
