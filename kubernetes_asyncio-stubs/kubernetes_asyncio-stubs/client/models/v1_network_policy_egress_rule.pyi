import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NetworkPolicyEgressRule:
    ports: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPort]]
    to: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPeer]]
    
    def __init__(self, *, ports: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPort]] = ..., to: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPeer]] = ...) -> None:
        ...
    def to_dict(self) -> V1NetworkPolicyEgressRuleDict:
        ...
class V1NetworkPolicyEgressRuleDict(typing.TypedDict, total=False):
    ports: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPortDict]]
    to: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyPeerDict]]
