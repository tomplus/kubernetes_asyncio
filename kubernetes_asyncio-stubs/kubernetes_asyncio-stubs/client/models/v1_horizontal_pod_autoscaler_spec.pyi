import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1HorizontalPodAutoscalerSpec:
    max_replicas: int
    min_replicas: typing.Optional[int]
    scale_target_ref: kubernetes_asyncio.client.V1CrossVersionObjectReference
    target_cpu_utilization_percentage: typing.Optional[int]
    
    def __init__(self, *, max_replicas: int, min_replicas: typing.Optional[int] = ..., scale_target_ref: kubernetes_asyncio.client.V1CrossVersionObjectReference, target_cpu_utilization_percentage: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1HorizontalPodAutoscalerSpecDict:
        ...
class V1HorizontalPodAutoscalerSpecDict(typing.TypedDict, total=False):
    maxReplicas: int
    minReplicas: typing.Optional[int]
    scaleTargetRef: kubernetes_asyncio.client.V1CrossVersionObjectReferenceDict
    targetCPUUtilizationPercentage: typing.Optional[int]
