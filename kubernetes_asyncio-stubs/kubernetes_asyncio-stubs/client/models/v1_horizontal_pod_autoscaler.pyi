import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1HorizontalPodAutoscaler:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1HorizontalPodAutoscalerSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1HorizontalPodAutoscalerStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1HorizontalPodAutoscalerSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1HorizontalPodAutoscalerStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1HorizontalPodAutoscalerDict:
        ...
class V1HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1HorizontalPodAutoscalerSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1HorizontalPodAutoscalerStatusDict]
