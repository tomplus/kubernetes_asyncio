import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1TokenRequestSpec:
    audiences: list[str]
    bound_object_ref: typing.Optional[kubernetes_asyncio.client.V1BoundObjectReference]
    expiration_seconds: typing.Optional[int]
    
    def __init__(self, *, audiences: list[str], bound_object_ref: typing.Optional[kubernetes_asyncio.client.V1BoundObjectReference] = ..., expiration_seconds: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1TokenRequestSpecDict:
        ...
class V1TokenRequestSpecDict(typing.TypedDict, total=False):
    audiences: list[str]
    boundObjectRef: typing.Optional[kubernetes_asyncio.client.V1BoundObjectReferenceDict]
    expirationSeconds: typing.Optional[int]
