import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NetworkPolicy:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1NetworkPolicySpec]
    status: typing.Optional[kubernetes_asyncio.client.V1NetworkPolicyStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1NetworkPolicySpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1NetworkPolicyStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1NetworkPolicyDict:
        ...
class V1NetworkPolicyDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1NetworkPolicySpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1NetworkPolicyStatusDict]
