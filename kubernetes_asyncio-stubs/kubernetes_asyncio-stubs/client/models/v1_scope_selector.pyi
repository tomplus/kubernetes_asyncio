import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ScopeSelector:
    match_expressions: typing.Optional[list[kubernetes_asyncio.client.V1ScopedResourceSelectorRequirement]]
    
    def __init__(self, *, match_expressions: typing.Optional[list[kubernetes_asyncio.client.V1ScopedResourceSelectorRequirement]] = ...) -> None:
        ...
    def to_dict(self) -> V1ScopeSelectorDict:
        ...
class V1ScopeSelectorDict(typing.TypedDict, total=False):
    matchExpressions: typing.Optional[list[kubernetes_asyncio.client.V1ScopedResourceSelectorRequirementDict]]
