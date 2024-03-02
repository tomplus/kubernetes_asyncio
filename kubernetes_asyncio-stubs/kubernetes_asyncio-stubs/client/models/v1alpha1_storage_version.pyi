import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1StorageVersion:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Any
    status: kubernetes_asyncio.client.V1alpha1StorageVersionStatus
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Any, status: kubernetes_asyncio.client.V1alpha1StorageVersionStatus) -> None:
        ...
    def to_dict(self) -> V1alpha1StorageVersionDict:
        ...
class V1alpha1StorageVersionDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Any
    status: kubernetes_asyncio.client.V1alpha1StorageVersionStatusDict
