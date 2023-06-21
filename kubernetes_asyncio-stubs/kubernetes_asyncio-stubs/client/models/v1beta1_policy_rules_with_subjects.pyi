import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta1NonResourcePolicyRule]]
    resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta1ResourcePolicyRule]]
    subjects: list[kubernetes_asyncio.client.V1beta1Subject]
    
    def __init__(self, *, non_resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta1NonResourcePolicyRule]] = ..., resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta1ResourcePolicyRule]] = ..., subjects: list[kubernetes_asyncio.client.V1beta1Subject]) -> None:
        ...
    def to_dict(self) -> V1beta1PolicyRulesWithSubjectsDict:
        ...
class V1beta1PolicyRulesWithSubjectsDict(typing.TypedDict, total=False):
    nonResourceRules: typing.Optional[list[kubernetes_asyncio.client.V1beta1NonResourcePolicyRuleDict]]
    resourceRules: typing.Optional[list[kubernetes_asyncio.client.V1beta1ResourcePolicyRuleDict]]
    subjects: list[kubernetes_asyncio.client.V1beta1SubjectDict]
