import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1TCPSocketAction:
    host: typing.Optional[str]
    port: typing.Any
    
    def __init__(self, *, host: typing.Optional[str] = ..., port: typing.Any) -> None:
        ...
    def to_dict(self) -> V1TCPSocketActionDict:
        ...
class V1TCPSocketActionDict(typing.TypedDict, total=False):
    host: typing.Optional[str]
    port: typing.Any
