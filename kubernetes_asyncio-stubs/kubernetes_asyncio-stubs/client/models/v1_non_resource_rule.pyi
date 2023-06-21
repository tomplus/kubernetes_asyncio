import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NonResourceRule:
    non_resource_ur_ls: typing.Optional[list[str]]
    verbs: list[str]
    
    def __init__(self, *, non_resource_ur_ls: typing.Optional[list[str]] = ..., verbs: list[str]) -> None:
        ...
    def to_dict(self) -> V1NonResourceRuleDict:
        ...
class V1NonResourceRuleDict(typing.TypedDict, total=False):
    nonResourceURLs: typing.Optional[list[str]]
    verbs: list[str]
