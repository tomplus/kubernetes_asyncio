import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LifecycleHandler:
    exec: typing.Optional[kubernetes_asyncio.client.V1ExecAction]
    http_get: typing.Optional[kubernetes_asyncio.client.V1HTTPGetAction]
    tcp_socket: typing.Optional[kubernetes_asyncio.client.V1TCPSocketAction]
    
    def __init__(self, *, exec: typing.Optional[kubernetes_asyncio.client.V1ExecAction] = ..., http_get: typing.Optional[kubernetes_asyncio.client.V1HTTPGetAction] = ..., tcp_socket: typing.Optional[kubernetes_asyncio.client.V1TCPSocketAction] = ...) -> None:
        ...
    def to_dict(self) -> V1LifecycleHandlerDict:
        ...
class V1LifecycleHandlerDict(typing.TypedDict, total=False):
    exec: typing.Optional[kubernetes_asyncio.client.V1ExecActionDict]
    httpGet: typing.Optional[kubernetes_asyncio.client.V1HTTPGetActionDict]
    tcpSocket: typing.Optional[kubernetes_asyncio.client.V1TCPSocketActionDict]
