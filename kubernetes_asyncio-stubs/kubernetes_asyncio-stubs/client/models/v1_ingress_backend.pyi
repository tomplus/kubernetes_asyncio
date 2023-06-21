import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1IngressBackend:
    resource: typing.Optional[kubernetes_asyncio.client.V1TypedLocalObjectReference]
    service: typing.Optional[kubernetes_asyncio.client.V1IngressServiceBackend]
    
    def __init__(self, *, resource: typing.Optional[kubernetes_asyncio.client.V1TypedLocalObjectReference] = ..., service: typing.Optional[kubernetes_asyncio.client.V1IngressServiceBackend] = ...) -> None:
        ...
    def to_dict(self) -> V1IngressBackendDict:
        ...
class V1IngressBackendDict(typing.TypedDict, total=False):
    resource: typing.Optional[kubernetes_asyncio.client.V1TypedLocalObjectReferenceDict]
    service: typing.Optional[kubernetes_asyncio.client.V1IngressServiceBackendDict]
