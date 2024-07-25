import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CrossVersionObjectReference:
    api_version: typing.Optional[str]
    kind: str
    name: str
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: str, name: str) -> None:
        ...
    def to_dict(self) -> V1CrossVersionObjectReferenceDict:
        ...
class V1CrossVersionObjectReferenceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: str
    name: str
