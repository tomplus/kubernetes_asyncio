import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2FlowSchema:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta2FlowSchemaSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1beta2FlowSchemaStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1beta2FlowSchemaSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1beta2FlowSchemaStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1beta2FlowSchemaDict:
        ...
class V1beta2FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta2FlowSchemaSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1beta2FlowSchemaStatusDict]
