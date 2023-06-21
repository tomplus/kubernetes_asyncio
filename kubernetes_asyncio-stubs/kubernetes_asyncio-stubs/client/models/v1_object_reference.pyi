import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ObjectReference:
    api_version: typing.Optional[str]
    field_path: typing.Optional[str]
    kind: typing.Optional[str]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    resource_version: typing.Optional[str]
    uid: typing.Optional[str]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., field_path: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., name: typing.Optional[str] = ..., namespace: typing.Optional[str] = ..., resource_version: typing.Optional[str] = ..., uid: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1ObjectReferenceDict:
        ...
class V1ObjectReferenceDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    fieldPath: typing.Optional[str]
    kind: typing.Optional[str]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    resourceVersion: typing.Optional[str]
    uid: typing.Optional[str]
