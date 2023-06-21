import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Role:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    rules: typing.Optional[list[kubernetes_asyncio.client.V1PolicyRule]]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., rules: typing.Optional[list[kubernetes_asyncio.client.V1PolicyRule]] = ...) -> None:
        ...
    def to_dict(self) -> V1RoleDict:
        ...
class V1RoleDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    rules: typing.Optional[list[kubernetes_asyncio.client.V1PolicyRuleDict]]
