import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodTemplateSpec:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1PodSpec]
    
    def __init__(self, *, metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1PodSpec] = ...) -> None:
        ...
    def to_dict(self) -> V1PodTemplateSpecDict:
        ...
class V1PodTemplateSpecDict(typing.TypedDict, total=False):
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1PodSpecDict]
