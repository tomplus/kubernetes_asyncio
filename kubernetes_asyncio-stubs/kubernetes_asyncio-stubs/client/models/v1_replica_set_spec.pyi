import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ReplicaSetSpec:
    min_ready_seconds: typing.Optional[int]
    replicas: typing.Optional[int]
    selector: kubernetes_asyncio.client.V1LabelSelector
    template: typing.Optional[kubernetes_asyncio.client.V1PodTemplateSpec]
    
    def __init__(self, *, min_ready_seconds: typing.Optional[int] = ..., replicas: typing.Optional[int] = ..., selector: kubernetes_asyncio.client.V1LabelSelector, template: typing.Optional[kubernetes_asyncio.client.V1PodTemplateSpec] = ...) -> None:
        ...
    def to_dict(self) -> V1ReplicaSetSpecDict:
        ...
class V1ReplicaSetSpecDict(typing.TypedDict, total=False):
    minReadySeconds: typing.Optional[int]
    replicas: typing.Optional[int]
    selector: kubernetes_asyncio.client.V1LabelSelectorDict
    template: typing.Optional[kubernetes_asyncio.client.V1PodTemplateSpecDict]
