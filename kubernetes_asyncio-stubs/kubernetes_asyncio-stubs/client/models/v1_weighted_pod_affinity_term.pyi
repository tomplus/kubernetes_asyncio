import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1WeightedPodAffinityTerm:
    pod_affinity_term: kubernetes_asyncio.client.V1PodAffinityTerm
    weight: int
    
    def __init__(self, *, pod_affinity_term: kubernetes_asyncio.client.V1PodAffinityTerm, weight: int) -> None:
        ...
    def to_dict(self) -> V1WeightedPodAffinityTermDict:
        ...
class V1WeightedPodAffinityTermDict(typing.TypedDict, total=False):
    podAffinityTerm: kubernetes_asyncio.client.V1PodAffinityTermDict
    weight: int
