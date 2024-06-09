import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ObjectFieldSelector:
    api_version: typing.Optional[str]
    field_path: str
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., field_path: str) -> None:
        ...
    def to_dict(self) -> V1ObjectFieldSelectorDict:
        ...
class V1ObjectFieldSelectorDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    fieldPath: str
