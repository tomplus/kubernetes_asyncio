import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2HorizontalPodAutoscalerStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V2HorizontalPodAutoscalerCondition]]
    current_metrics: typing.Optional[list[kubernetes_asyncio.client.V2MetricStatus]]
    current_replicas: typing.Optional[int]
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]
    
    def __init__(self, *, conditions: typing.Optional[list[kubernetes_asyncio.client.V2HorizontalPodAutoscalerCondition]] = ..., current_metrics: typing.Optional[list[kubernetes_asyncio.client.V2MetricStatus]] = ..., current_replicas: typing.Optional[int] = ..., desired_replicas: int, last_scale_time: typing.Optional[datetime.datetime] = ..., observed_generation: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V2HorizontalPodAutoscalerStatusDict:
        ...
class V2HorizontalPodAutoscalerStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes_asyncio.client.V2HorizontalPodAutoscalerConditionDict]]
    currentMetrics: typing.Optional[list[kubernetes_asyncio.client.V2MetricStatusDict]]
    currentReplicas: typing.Optional[int]
    desiredReplicas: int
    lastScaleTime: typing.Optional[datetime.datetime]
    observedGeneration: typing.Optional[int]
