import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolumeClaim:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1PersistentVolumeClaimDict:
        ...
class V1PersistentVolumeClaimDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimStatusDict]
