import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[list[kubernetes_asyncio.client.V1PreferredSchedulingTerm]]
    required_during_scheduling_ignored_during_execution: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]
    
    def __init__(self, *, preferred_during_scheduling_ignored_during_execution: typing.Optional[list[kubernetes_asyncio.client.V1PreferredSchedulingTerm]] = ..., required_during_scheduling_ignored_during_execution: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...) -> None:
        ...
    def to_dict(self) -> V1NodeAffinityDict:
        ...
class V1NodeAffinityDict(typing.TypedDict, total=False):
    preferredDuringSchedulingIgnoredDuringExecution: typing.Optional[list[kubernetes_asyncio.client.V1PreferredSchedulingTermDict]]
    requiredDuringSchedulingIgnoredDuringExecution: typing.Optional[kubernetes_asyncio.client.V1NodeSelectorDict]
