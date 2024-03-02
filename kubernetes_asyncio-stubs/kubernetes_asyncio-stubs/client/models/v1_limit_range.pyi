import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LimitRange:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1LimitRangeSpec]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1LimitRangeSpec] = ...) -> None:
        ...
    def to_dict(self) -> V1LimitRangeDict:
        ...
class V1LimitRangeDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1LimitRangeSpecDict]
