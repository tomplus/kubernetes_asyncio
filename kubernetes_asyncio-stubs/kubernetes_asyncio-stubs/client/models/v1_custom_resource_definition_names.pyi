import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceDefinitionNames:
    categories: typing.Optional[list[str]]
    kind: str
    list_kind: typing.Optional[str]
    plural: str
    short_names: typing.Optional[list[str]]
    singular: typing.Optional[str]
    
    def __init__(self, *, categories: typing.Optional[list[str]] = ..., kind: str, list_kind: typing.Optional[str] = ..., plural: str, short_names: typing.Optional[list[str]] = ..., singular: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1CustomResourceDefinitionNamesDict:
        ...
class V1CustomResourceDefinitionNamesDict(typing.TypedDict, total=False):
    categories: typing.Optional[list[str]]
    kind: str
    listKind: typing.Optional[str]
    plural: str
    shortNames: typing.Optional[list[str]]
    singular: typing.Optional[str]
