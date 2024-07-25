import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2PriorityLevelConfigurationSpec:
    limited: typing.Optional[kubernetes_asyncio.client.V1beta2LimitedPriorityLevelConfiguration]
    type: str
    
    def __init__(self, *, limited: typing.Optional[kubernetes_asyncio.client.V1beta2LimitedPriorityLevelConfiguration] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V1beta2PriorityLevelConfigurationSpecDict:
        ...
class V1beta2PriorityLevelConfigurationSpecDict(typing.TypedDict, total=False):
    limited: typing.Optional[kubernetes_asyncio.client.V1beta2LimitedPriorityLevelConfigurationDict]
    type: str
