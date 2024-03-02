import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ControllerRevision:
    api_version: typing.Optional[str]
    data: typing.Optional[typing.Any]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    revision: int
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., data: typing.Optional[typing.Any] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., revision: int) -> None:
        ...
    def to_dict(self) -> V1ControllerRevisionDict:
        ...
class V1ControllerRevisionDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    data: typing.Optional[typing.Any]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    revision: int
