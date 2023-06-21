import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ReplicationController:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1ReplicationControllerSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1ReplicationControllerStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1ReplicationControllerSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1ReplicationControllerStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1ReplicationControllerDict:
        ...
class V1ReplicationControllerDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1ReplicationControllerSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1ReplicationControllerStatusDict]
