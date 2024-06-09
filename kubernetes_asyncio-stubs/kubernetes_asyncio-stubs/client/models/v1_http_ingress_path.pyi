import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1HTTPIngressPath:
    backend: kubernetes_asyncio.client.V1IngressBackend
    path: typing.Optional[str]
    path_type: str
    
    def __init__(self, *, backend: kubernetes_asyncio.client.V1IngressBackend, path: typing.Optional[str] = ..., path_type: str) -> None:
        ...
    def to_dict(self) -> V1HTTPIngressPathDict:
        ...
class V1HTTPIngressPathDict(typing.TypedDict, total=False):
    backend: kubernetes_asyncio.client.V1IngressBackendDict
    path: typing.Optional[str]
    pathType: str
