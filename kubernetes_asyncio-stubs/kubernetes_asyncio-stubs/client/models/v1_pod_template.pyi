import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodTemplate:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    template: typing.Optional[kubernetes_asyncio.client.V1PodTemplateSpec]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., template: typing.Optional[kubernetes_asyncio.client.V1PodTemplateSpec] = ...) -> None:
        ...
    def to_dict(self) -> V1PodTemplateDict:
        ...
class V1PodTemplateDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    template: typing.Optional[kubernetes_asyncio.client.V1PodTemplateSpecDict]
