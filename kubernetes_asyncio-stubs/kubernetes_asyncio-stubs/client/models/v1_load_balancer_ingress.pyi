import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1PortStatus]]
    
    def __init__(self, *, hostname: typing.Optional[str] = ..., ip: typing.Optional[str] = ..., ports: typing.Optional[list[kubernetes_asyncio.client.V1PortStatus]] = ...) -> None:
        ...
    def to_dict(self) -> V1LoadBalancerIngressDict:
        ...
class V1LoadBalancerIngressDict(typing.TypedDict, total=False):
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1PortStatusDict]]
