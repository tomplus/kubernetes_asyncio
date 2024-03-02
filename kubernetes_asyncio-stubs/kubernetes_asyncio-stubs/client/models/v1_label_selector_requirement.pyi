import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LabelSelectorRequirement:
    key: str
    operator: str
    values: typing.Optional[list[str]]
    
    def __init__(self, *, key: str, operator: str, values: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1LabelSelectorRequirementDict:
        ...
class V1LabelSelectorRequirementDict(typing.TypedDict, total=False):
    key: str
    operator: str
    values: typing.Optional[list[str]]
