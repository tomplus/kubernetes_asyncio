import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Namespace:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1NamespaceSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1NamespaceStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1NamespaceSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1NamespaceStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1NamespaceDict:
        ...
class V1NamespaceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1NamespaceSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1NamespaceStatusDict]
