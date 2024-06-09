import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ContainerPort:
    container_port: int
    host_ip: typing.Optional[str]
    host_port: typing.Optional[int]
    name: typing.Optional[str]
    protocol: typing.Optional[str]
    
    def __init__(self, *, container_port: int, host_ip: typing.Optional[str] = ..., host_port: typing.Optional[int] = ..., name: typing.Optional[str] = ..., protocol: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1ContainerPortDict:
        ...
class V1ContainerPortDict(typing.TypedDict, total=False):
    containerPort: int
    hostIP: typing.Optional[str]
    hostPort: typing.Optional[int]
    name: typing.Optional[str]
    protocol: typing.Optional[str]
