import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeSelectorTerm:
    match_expressions: typing.Optional[list[kubernetes_asyncio.client.V1NodeSelectorRequirement]]
    match_fields: typing.Optional[list[kubernetes_asyncio.client.V1NodeSelectorRequirement]]
    
    def __init__(self, *, match_expressions: typing.Optional[list[kubernetes_asyncio.client.V1NodeSelectorRequirement]] = ..., match_fields: typing.Optional[list[kubernetes_asyncio.client.V1NodeSelectorRequirement]] = ...) -> None:
        ...
    def to_dict(self) -> V1NodeSelectorTermDict:
        ...
class V1NodeSelectorTermDict(typing.TypedDict, total=False):
    matchExpressions: typing.Optional[list[kubernetes_asyncio.client.V1NodeSelectorRequirementDict]]
    matchFields: typing.Optional[list[kubernetes_asyncio.client.V1NodeSelectorRequirementDict]]
