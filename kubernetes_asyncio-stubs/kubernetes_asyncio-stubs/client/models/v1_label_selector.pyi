import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LabelSelector:
    match_expressions: typing.Optional[list[kubernetes_asyncio.client.V1LabelSelectorRequirement]]
    match_labels: typing.Optional[dict[str, str]]
    
    def __init__(self, *, match_expressions: typing.Optional[list[kubernetes_asyncio.client.V1LabelSelectorRequirement]] = ..., match_labels: typing.Optional[dict[str, str]] = ...) -> None:
        ...
    def to_dict(self) -> V1LabelSelectorDict:
        ...
class V1LabelSelectorDict(typing.TypedDict, total=False):
    matchExpressions: typing.Optional[list[kubernetes_asyncio.client.V1LabelSelectorRequirementDict]]
    matchLabels: typing.Optional[dict[str, str]]
