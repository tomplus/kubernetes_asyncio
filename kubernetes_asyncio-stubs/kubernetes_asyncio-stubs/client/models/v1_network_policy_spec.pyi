import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NetworkPolicySpec:
    egress: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyEgressRule]]
    ingress: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyIngressRule]]
    pod_selector: kubernetes_asyncio.client.V1LabelSelector
    policy_types: typing.Optional[list[str]]
    
    def __init__(self, *, egress: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyEgressRule]] = ..., ingress: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyIngressRule]] = ..., pod_selector: kubernetes_asyncio.client.V1LabelSelector, policy_types: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1NetworkPolicySpecDict:
        ...
class V1NetworkPolicySpecDict(typing.TypedDict, total=False):
    egress: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyEgressRuleDict]]
    ingress: typing.Optional[list[kubernetes_asyncio.client.V1NetworkPolicyIngressRuleDict]]
    podSelector: kubernetes_asyncio.client.V1LabelSelectorDict
    policyTypes: typing.Optional[list[str]]
