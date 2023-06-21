import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PreferredSchedulingTerm:
    preference: kubernetes_asyncio.client.V1NodeSelectorTerm
    weight: int
    
    def __init__(self, *, preference: kubernetes_asyncio.client.V1NodeSelectorTerm, weight: int) -> None:
        ...
    def to_dict(self) -> V1PreferredSchedulingTermDict:
        ...
class V1PreferredSchedulingTermDict(typing.TypedDict, total=False):
    preference: kubernetes_asyncio.client.V1NodeSelectorTermDict
    weight: int
