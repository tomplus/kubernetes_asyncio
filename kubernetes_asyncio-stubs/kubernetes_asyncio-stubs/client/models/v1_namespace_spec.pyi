import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NamespaceSpec:
    finalizers: typing.Optional[list[str]]
    
    def __init__(self, *, finalizers: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1NamespaceSpecDict:
        ...
class V1NamespaceSpecDict(typing.TypedDict, total=False):
    finalizers: typing.Optional[list[str]]
