import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1HorizontalPodAutoscaler:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V2beta1HorizontalPodAutoscalerSpec]
    status: typing.Optional[kubernetes_asyncio.client.V2beta1HorizontalPodAutoscalerStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V2beta1HorizontalPodAutoscalerSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V2beta1HorizontalPodAutoscalerStatus] = ...) -> None:
        ...
    def to_dict(self) -> V2beta1HorizontalPodAutoscalerDict:
        ...
class V2beta1HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V2beta1HorizontalPodAutoscalerSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V2beta1HorizontalPodAutoscalerStatusDict]
