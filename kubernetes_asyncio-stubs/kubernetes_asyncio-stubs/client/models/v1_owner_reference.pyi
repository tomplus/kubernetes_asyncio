import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1OwnerReference:
    api_version: str
    block_owner_deletion: typing.Optional[bool]
    controller: typing.Optional[bool]
    kind: str
    name: str
    uid: str
    
    def __init__(self, *, api_version: str, block_owner_deletion: typing.Optional[bool] = ..., controller: typing.Optional[bool] = ..., kind: str, name: str, uid: str) -> None:
        ...
    def to_dict(self) -> V1OwnerReferenceDict:
        ...
class V1OwnerReferenceDict(typing.TypedDict, total=False):
    apiVersion: str
    blockOwnerDeletion: typing.Optional[bool]
    controller: typing.Optional[bool]
    kind: str
    name: str
    uid: str
