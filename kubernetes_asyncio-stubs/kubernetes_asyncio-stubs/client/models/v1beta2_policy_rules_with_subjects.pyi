import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta2NonResourcePolicyRule]]
    resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta2ResourcePolicyRule]]
    subjects: list[kubernetes_asyncio.client.V1beta2Subject]
    
    def __init__(self, *, non_resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta2NonResourcePolicyRule]] = ..., resource_rules: typing.Optional[list[kubernetes_asyncio.client.V1beta2ResourcePolicyRule]] = ..., subjects: list[kubernetes_asyncio.client.V1beta2Subject]) -> None:
        ...
    def to_dict(self) -> V1beta2PolicyRulesWithSubjectsDict:
        ...
class V1beta2PolicyRulesWithSubjectsDict(typing.TypedDict, total=False):
    nonResourceRules: typing.Optional[list[kubernetes_asyncio.client.V1beta2NonResourcePolicyRuleDict]]
    resourceRules: typing.Optional[list[kubernetes_asyncio.client.V1beta2ResourcePolicyRuleDict]]
    subjects: list[kubernetes_asyncio.client.V1beta2SubjectDict]
