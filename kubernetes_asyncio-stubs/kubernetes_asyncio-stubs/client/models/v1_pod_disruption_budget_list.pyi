import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodDisruptionBudgetList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1PodDisruptionBudget]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.V1PodDisruptionBudget], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> V1PodDisruptionBudgetListDict:
        ...
class V1PodDisruptionBudgetListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1PodDisruptionBudgetDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
