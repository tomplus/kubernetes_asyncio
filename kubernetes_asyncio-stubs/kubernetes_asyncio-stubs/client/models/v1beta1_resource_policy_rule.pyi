import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ResourcePolicyRule:
    api_groups: list[str]
    cluster_scope: typing.Optional[bool]
    namespaces: typing.Optional[list[str]]
    resources: list[str]
    verbs: list[str]
    
    def __init__(self, *, api_groups: list[str], cluster_scope: typing.Optional[bool] = ..., namespaces: typing.Optional[list[str]] = ..., resources: list[str], verbs: list[str]) -> None:
        ...
    def to_dict(self) -> V1beta1ResourcePolicyRuleDict:
        ...
class V1beta1ResourcePolicyRuleDict(typing.TypedDict, total=False):
    apiGroups: list[str]
    clusterScope: typing.Optional[bool]
    namespaces: typing.Optional[list[str]]
    resources: list[str]
    verbs: list[str]
