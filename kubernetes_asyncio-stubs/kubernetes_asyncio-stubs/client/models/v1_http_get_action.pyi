import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1HTTPGetAction:
    host: typing.Optional[str]
    http_headers: typing.Optional[list[kubernetes_asyncio.client.V1HTTPHeader]]
    path: typing.Optional[str]
    port: typing.Any
    scheme: typing.Optional[str]
    
    def __init__(self, *, host: typing.Optional[str] = ..., http_headers: typing.Optional[list[kubernetes_asyncio.client.V1HTTPHeader]] = ..., path: typing.Optional[str] = ..., port: typing.Any, scheme: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1HTTPGetActionDict:
        ...
class V1HTTPGetActionDict(typing.TypedDict, total=False):
    host: typing.Optional[str]
    httpHeaders: typing.Optional[list[kubernetes_asyncio.client.V1HTTPHeaderDict]]
    path: typing.Optional[str]
    port: typing.Any
    scheme: typing.Optional[str]
