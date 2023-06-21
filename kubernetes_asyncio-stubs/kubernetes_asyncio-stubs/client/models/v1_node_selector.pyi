import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeSelector:
    node_selector_terms: list[kubernetes_asyncio.client.V1NodeSelectorTerm]
    
    def __init__(self, *, node_selector_terms: list[kubernetes_asyncio.client.V1NodeSelectorTerm]) -> None:
        ...
    def to_dict(self) -> V1NodeSelectorDict:
        ...
class V1NodeSelectorDict(typing.TypedDict, total=False):
    nodeSelectorTerms: list[kubernetes_asyncio.client.V1NodeSelectorTermDict]
