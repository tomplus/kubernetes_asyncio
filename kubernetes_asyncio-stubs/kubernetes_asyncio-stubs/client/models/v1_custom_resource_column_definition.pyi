import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceColumnDefinition:
    description: typing.Optional[str]
    format: typing.Optional[str]
    json_path: str
    name: str
    priority: typing.Optional[int]
    type: str
    
    def __init__(self, *, description: typing.Optional[str] = ..., format: typing.Optional[str] = ..., json_path: str, name: str, priority: typing.Optional[int] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V1CustomResourceColumnDefinitionDict:
        ...
class V1CustomResourceColumnDefinitionDict(typing.TypedDict, total=False):
    description: typing.Optional[str]
    format: typing.Optional[str]
    jsonPath: str
    name: str
    priority: typing.Optional[int]
    type: str
