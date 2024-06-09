import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DaemonSetSpec:
    min_ready_seconds: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: kubernetes_asyncio.client.V1LabelSelector
    template: kubernetes_asyncio.client.V1PodTemplateSpec
    update_strategy: typing.Optional[kubernetes_asyncio.client.V1DaemonSetUpdateStrategy]
    
    def __init__(self, *, min_ready_seconds: typing.Optional[int] = ..., revision_history_limit: typing.Optional[int] = ..., selector: kubernetes_asyncio.client.V1LabelSelector, template: kubernetes_asyncio.client.V1PodTemplateSpec, update_strategy: typing.Optional[kubernetes_asyncio.client.V1DaemonSetUpdateStrategy] = ...) -> None:
        ...
    def to_dict(self) -> V1DaemonSetSpecDict:
        ...
class V1DaemonSetSpecDict(typing.TypedDict, total=False):
    minReadySeconds: typing.Optional[int]
    revisionHistoryLimit: typing.Optional[int]
    selector: kubernetes_asyncio.client.V1LabelSelectorDict
    template: kubernetes_asyncio.client.V1PodTemplateSpecDict
    updateStrategy: typing.Optional[kubernetes_asyncio.client.V1DaemonSetUpdateStrategyDict]
