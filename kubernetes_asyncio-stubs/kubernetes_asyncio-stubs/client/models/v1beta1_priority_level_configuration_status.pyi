import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1PriorityLevelConfigurationStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationCondition]]
    
    def __init__(self, *, conditions: typing.Optional[list[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationCondition]] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1PriorityLevelConfigurationStatusDict:
        ...
class V1beta1PriorityLevelConfigurationStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationConditionDict]]
