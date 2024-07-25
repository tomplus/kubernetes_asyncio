import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1RuntimeClass:
    api_version: typing.Optional[str]
    handler: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    overhead: typing.Optional[kubernetes_asyncio.client.V1beta1Overhead]
    scheduling: typing.Optional[kubernetes_asyncio.client.V1beta1Scheduling]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., handler: str, kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., overhead: typing.Optional[kubernetes_asyncio.client.V1beta1Overhead] = ..., scheduling: typing.Optional[kubernetes_asyncio.client.V1beta1Scheduling] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1RuntimeClassDict:
        ...
class V1beta1RuntimeClassDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    handler: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    overhead: typing.Optional[kubernetes_asyncio.client.V1beta1OverheadDict]
    scheduling: typing.Optional[kubernetes_asyncio.client.V1beta1SchedulingDict]
