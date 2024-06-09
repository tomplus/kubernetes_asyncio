import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1GRPCAction:
    port: int
    service: typing.Optional[str]
    
    def __init__(self, *, port: int, service: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1GRPCActionDict:
        ...
class V1GRPCActionDict(typing.TypedDict, total=False):
    port: int
    service: typing.Optional[str]
