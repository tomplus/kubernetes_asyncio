import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2HorizontalPodAutoscalerList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V2beta2HorizontalPodAutoscaler]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.V2beta2HorizontalPodAutoscaler], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> V2beta2HorizontalPodAutoscalerListDict:
        ...
class V2beta2HorizontalPodAutoscalerListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V2beta2HorizontalPodAutoscalerDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
