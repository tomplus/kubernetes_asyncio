import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1IngressServiceBackend:
    name: str
    port: typing.Optional[kubernetes_asyncio.client.V1ServiceBackendPort]
    
    def __init__(self, *, name: str, port: typing.Optional[kubernetes_asyncio.client.V1ServiceBackendPort] = ...) -> None:
        ...
    def to_dict(self) -> V1IngressServiceBackendDict:
        ...
class V1IngressServiceBackendDict(typing.TypedDict, total=False):
    name: str
    port: typing.Optional[kubernetes_asyncio.client.V1ServiceBackendPortDict]
