import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NetworkPolicyIngressRule:
    _from: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPeer]]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPort]]
    
    def __init__(self, *, _from: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPeer]] = ..., ports: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPort]] = ...) -> None:
        ...
    def to_dict(self) -> V1NetworkPolicyIngressRuleDict:
        ...
class V1NetworkPolicyIngressRuleDict(typing.TypedDict, total=False):
    _from: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPeerDict]]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPortDict]]
