import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1StatefulSet:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1StatefulSetSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1StatefulSetStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1StatefulSetSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1StatefulSetStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1StatefulSetDict:
        ...
class V1StatefulSetDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1StatefulSetSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1StatefulSetStatusDict]
