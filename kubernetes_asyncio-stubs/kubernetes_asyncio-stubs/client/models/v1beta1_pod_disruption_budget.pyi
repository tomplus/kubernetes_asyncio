import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1PodDisruptionBudget:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta1PodDisruptionBudgetSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1beta1PodDisruptionBudgetStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1beta1PodDisruptionBudgetSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1beta1PodDisruptionBudgetStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1PodDisruptionBudgetDict:
        ...
class V1beta1PodDisruptionBudgetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta1PodDisruptionBudgetSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1beta1PodDisruptionBudgetStatusDict]
