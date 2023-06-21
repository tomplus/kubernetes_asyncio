import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RoleRef:
    api_group: str
    kind: str
    name: str
    
    def __init__(self, *, api_group: str, kind: str, name: str) -> None:
        ...
    def to_dict(self) -> V1RoleRefDict:
        ...
class V1RoleRefDict(typing.TypedDict, total=False):
    apiGroup: str
    kind: str
    name: str
