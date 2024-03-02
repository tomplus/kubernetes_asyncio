import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2FlowSchemaList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1beta2FlowSchema]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes_asyncio.client.V1beta2FlowSchema], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> V1beta2FlowSchemaListDict:
        ...
class V1beta2FlowSchemaListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1beta2FlowSchemaDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
