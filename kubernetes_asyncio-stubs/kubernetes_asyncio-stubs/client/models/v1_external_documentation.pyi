import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ExternalDocumentation:
    description: typing.Optional[str]
    url: typing.Optional[str]
    
    def __init__(self, *, description: typing.Optional[str] = ..., url: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1ExternalDocumentationDict:
        ...
class V1ExternalDocumentationDict(typing.TypedDict, total=False):
    description: typing.Optional[str]
    url: typing.Optional[str]
