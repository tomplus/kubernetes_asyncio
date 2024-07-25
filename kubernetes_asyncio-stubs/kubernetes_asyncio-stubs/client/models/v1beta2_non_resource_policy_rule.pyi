import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2NonResourcePolicyRule:
    non_resource_ur_ls: list[str]
    verbs: list[str]
    
    def __init__(self, *, non_resource_ur_ls: list[str], verbs: list[str]) -> None:
        ...
    def to_dict(self) -> V1beta2NonResourcePolicyRuleDict:
        ...
class V1beta2NonResourcePolicyRuleDict(typing.TypedDict, total=False):
    nonResourceURLs: list[str]
    verbs: list[str]
