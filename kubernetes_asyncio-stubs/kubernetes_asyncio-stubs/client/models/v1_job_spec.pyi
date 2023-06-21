import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1JobSpec:
    active_deadline_seconds: typing.Optional[int]
    backoff_limit: typing.Optional[int]
    completion_mode: typing.Optional[str]
    completions: typing.Optional[int]
    manual_selector: typing.Optional[bool]
    parallelism: typing.Optional[int]
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    suspend: typing.Optional[bool]
    template: kubernetes_asyncio.client.V1PodTemplateSpec
    ttl_seconds_after_finished: typing.Optional[int]
    
    def __init__(self, *, active_deadline_seconds: typing.Optional[int] = ..., backoff_limit: typing.Optional[int] = ..., completion_mode: typing.Optional[str] = ..., completions: typing.Optional[int] = ..., manual_selector: typing.Optional[bool] = ..., parallelism: typing.Optional[int] = ..., selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., suspend: typing.Optional[bool] = ..., template: kubernetes_asyncio.client.V1PodTemplateSpec, ttl_seconds_after_finished: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1JobSpecDict:
        ...
class V1JobSpecDict(typing.TypedDict, total=False):
    activeDeadlineSeconds: typing.Optional[int]
    backoffLimit: typing.Optional[int]
    completionMode: typing.Optional[str]
    completions: typing.Optional[int]
    manualSelector: typing.Optional[bool]
    parallelism: typing.Optional[int]
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    suspend: typing.Optional[bool]
    template: kubernetes_asyncio.client.V1PodTemplateSpecDict
    ttlSecondsAfterFinished: typing.Optional[int]
