import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2FlowSchemaSpec:
    distinguisher_method: typing.Optional[kubernetes_asyncio.client.V1beta2FlowDistinguisherMethod]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: kubernetes_asyncio.client.V1beta2PriorityLevelConfigurationReference
    rules: typing.Optional[list[kubernetes_asyncio.client.V1beta2PolicyRulesWithSubjects]]
    
    def __init__(self, *, distinguisher_method: typing.Optional[kubernetes_asyncio.client.V1beta2FlowDistinguisherMethod] = ..., matching_precedence: typing.Optional[int] = ..., priority_level_configuration: kubernetes_asyncio.client.V1beta2PriorityLevelConfigurationReference, rules: typing.Optional[list[kubernetes_asyncio.client.V1beta2PolicyRulesWithSubjects]] = ...) -> None:
        ...
    def to_dict(self) -> V1beta2FlowSchemaSpecDict:
        ...
class V1beta2FlowSchemaSpecDict(typing.TypedDict, total=False):
    distinguisherMethod: typing.Optional[kubernetes_asyncio.client.V1beta2FlowDistinguisherMethodDict]
    matchingPrecedence: typing.Optional[int]
    priorityLevelConfiguration: kubernetes_asyncio.client.V1beta2PriorityLevelConfigurationReferenceDict
    rules: typing.Optional[list[kubernetes_asyncio.client.V1beta2PolicyRulesWithSubjectsDict]]
