import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ReplicaSet:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1ReplicaSetSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1ReplicaSetStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1ReplicaSetSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1ReplicaSetStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1ReplicaSetDict:
        ...
class V1ReplicaSetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1ReplicaSetSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1ReplicaSetStatusDict]
