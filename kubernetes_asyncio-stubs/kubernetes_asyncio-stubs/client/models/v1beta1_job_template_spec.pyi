import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1JobTemplateSpec:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1JobSpec]
    
    def __init__(self, *, metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1JobSpec] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1JobTemplateSpecDict:
        ...
class V1beta1JobTemplateSpecDict(typing.TypedDict, total=False):
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1JobSpecDict]
