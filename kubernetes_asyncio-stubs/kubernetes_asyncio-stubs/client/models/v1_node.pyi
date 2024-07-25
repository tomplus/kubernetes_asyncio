import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Node:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1NodeSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1NodeStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1NodeSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1NodeStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1NodeDict:
        ...
class V1NodeDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1NodeSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1NodeStatusDict]
