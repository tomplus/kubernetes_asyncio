import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolumeClaimTemplate:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1PersistentVolumeClaimSpec
    
    def __init__(self, *, metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: kubernetes_asyncio.client.V1PersistentVolumeClaimSpec) -> None:
        ...
    def to_dict(self) -> V1PersistentVolumeClaimTemplateDict:
        ...
class V1PersistentVolumeClaimTemplateDict(typing.TypedDict, total=False):
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1PersistentVolumeClaimSpecDict
