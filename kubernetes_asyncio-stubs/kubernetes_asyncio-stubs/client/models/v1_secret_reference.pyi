import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SecretReference:
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    
    def __init__(self, *, name: typing.Optional[str] = ..., namespace: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1SecretReferenceDict:
        ...
class V1SecretReferenceDict(typing.TypedDict, total=False):
    name: typing.Optional[str]
    namespace: typing.Optional[str]
