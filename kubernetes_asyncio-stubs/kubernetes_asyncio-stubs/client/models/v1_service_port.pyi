import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ServicePort:
    app_protocol: typing.Optional[str]
    name: typing.Optional[str]
    node_port: typing.Optional[int]
    port: int
    protocol: typing.Optional[str]
    target_port: typing.Optional[typing.Any]
    
    def __init__(self, *, app_protocol: typing.Optional[str] = ..., name: typing.Optional[str] = ..., node_port: typing.Optional[int] = ..., port: int, protocol: typing.Optional[str] = ..., target_port: typing.Optional[typing.Any] = ...) -> None:
        ...
    def to_dict(self) -> V1ServicePortDict:
        ...
class V1ServicePortDict(typing.TypedDict, total=False):
    appProtocol: typing.Optional[str]
    name: typing.Optional[str]
    nodePort: typing.Optional[int]
    port: int
    protocol: typing.Optional[str]
    targetPort: typing.Optional[typing.Any]
