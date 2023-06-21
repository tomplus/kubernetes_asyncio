import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodAntiAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[list[kubernetes_asyncio.client.V1WeightedPodAffinityTerm]]
    required_during_scheduling_ignored_during_execution: typing.Optional[list[kubernetes_asyncio.client.V1PodAffinityTerm]]
    
    def __init__(self, *, preferred_during_scheduling_ignored_during_execution: typing.Optional[list[kubernetes_asyncio.client.V1WeightedPodAffinityTerm]] = ..., required_during_scheduling_ignored_during_execution: typing.Optional[list[kubernetes_asyncio.client.V1PodAffinityTerm]] = ...) -> None:
        ...
    def to_dict(self) -> V1PodAntiAffinityDict:
        ...
class V1PodAntiAffinityDict(typing.TypedDict, total=False):
    preferredDuringSchedulingIgnoredDuringExecution: typing.Optional[list[kubernetes_asyncio.client.V1WeightedPodAffinityTermDict]]
    requiredDuringSchedulingIgnoredDuringExecution: typing.Optional[list[kubernetes_asyncio.client.V1PodAffinityTermDict]]
