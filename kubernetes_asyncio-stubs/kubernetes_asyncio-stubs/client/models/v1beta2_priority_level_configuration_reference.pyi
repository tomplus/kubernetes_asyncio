import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2PriorityLevelConfigurationReference:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1beta2PriorityLevelConfigurationReferenceDict:
        ...
class V1beta2PriorityLevelConfigurationReferenceDict(typing.TypedDict, total=False):
    name: str
