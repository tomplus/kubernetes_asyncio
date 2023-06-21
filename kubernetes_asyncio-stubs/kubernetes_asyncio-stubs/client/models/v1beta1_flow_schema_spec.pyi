import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1FlowSchemaSpec:
    distinguisher_method: typing.Optional[kubernetes_asyncio.client.V1beta1FlowDistinguisherMethod]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationReference
    rules: typing.Optional[list[kubernetes_asyncio.client.V1beta1PolicyRulesWithSubjects]]
    
    def __init__(self, *, distinguisher_method: typing.Optional[kubernetes_asyncio.client.V1beta1FlowDistinguisherMethod] = ..., matching_precedence: typing.Optional[int] = ..., priority_level_configuration: kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationReference, rules: typing.Optional[list[kubernetes_asyncio.client.V1beta1PolicyRulesWithSubjects]] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1FlowSchemaSpecDict:
        ...
class V1beta1FlowSchemaSpecDict(typing.TypedDict, total=False):
    distinguisherMethod: typing.Optional[kubernetes_asyncio.client.V1beta1FlowDistinguisherMethodDict]
    matchingPrecedence: typing.Optional[int]
    priorityLevelConfiguration: kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationReferenceDict
    rules: typing.Optional[list[kubernetes_asyncio.client.V1beta1PolicyRulesWithSubjectsDict]]
