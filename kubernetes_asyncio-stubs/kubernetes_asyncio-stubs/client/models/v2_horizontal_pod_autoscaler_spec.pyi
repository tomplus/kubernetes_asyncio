import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2HorizontalPodAutoscalerSpec:
    behavior: typing.Optional[kubernetes_asyncio.client.V2HorizontalPodAutoscalerBehavior]
    max_replicas: int
    metrics: typing.Optional[list[kubernetes_asyncio.client.V2MetricSpec]]
    min_replicas: typing.Optional[int]
    scale_target_ref: kubernetes_asyncio.client.V2CrossVersionObjectReference
    
    def __init__(self, *, behavior: typing.Optional[kubernetes_asyncio.client.V2HorizontalPodAutoscalerBehavior] = ..., max_replicas: int, metrics: typing.Optional[list[kubernetes_asyncio.client.V2MetricSpec]] = ..., min_replicas: typing.Optional[int] = ..., scale_target_ref: kubernetes_asyncio.client.V2CrossVersionObjectReference) -> None:
        ...
    def to_dict(self) -> V2HorizontalPodAutoscalerSpecDict:
        ...
class V2HorizontalPodAutoscalerSpecDict(typing.TypedDict, total=False):
    behavior: typing.Optional[kubernetes_asyncio.client.V2HorizontalPodAutoscalerBehaviorDict]
    maxReplicas: int
    metrics: typing.Optional[list[kubernetes_asyncio.client.V2MetricSpecDict]]
    minReplicas: typing.Optional[int]
    scaleTargetRef: kubernetes_asyncio.client.V2CrossVersionObjectReferenceDict
