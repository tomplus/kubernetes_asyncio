import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Subject:
    api_group: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
    
    def __init__(self, *, api_group: typing.Optional[str] = ..., kind: str, name: str, namespace: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1SubjectDict:
        ...
class V1SubjectDict(typing.TypedDict, total=False):
    apiGroup: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
