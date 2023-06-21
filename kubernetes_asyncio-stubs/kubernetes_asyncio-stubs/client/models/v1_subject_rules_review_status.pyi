import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SubjectRulesReviewStatus:
    evaluation_error: typing.Optional[str]
    incomplete: bool
    non_resource_rules: list[kubernetes_asyncio.client.V1NonResourceRule]
    resource_rules: list[kubernetes_asyncio.client.V1ResourceRule]
    
    def __init__(self, *, evaluation_error: typing.Optional[str] = ..., incomplete: bool, non_resource_rules: list[kubernetes_asyncio.client.V1NonResourceRule], resource_rules: list[kubernetes_asyncio.client.V1ResourceRule]) -> None:
        ...
    def to_dict(self) -> V1SubjectRulesReviewStatusDict:
        ...
class V1SubjectRulesReviewStatusDict(typing.TypedDict, total=False):
    evaluationError: typing.Optional[str]
    incomplete: bool
    nonResourceRules: list[kubernetes_asyncio.client.V1NonResourceRuleDict]
    resourceRules: list[kubernetes_asyncio.client.V1ResourceRuleDict]
