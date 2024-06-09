import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LoadBalancerStatus:
    ingress: typing.Optional[list[kubernetes_asyncio.client.V1LoadBalancerIngress]]
    
    def __init__(self, *, ingress: typing.Optional[list[kubernetes_asyncio.client.V1LoadBalancerIngress]] = ...) -> None:
        ...
    def to_dict(self) -> V1LoadBalancerStatusDict:
        ...
class V1LoadBalancerStatusDict(typing.TypedDict, total=False):
    ingress: typing.Optional[list[kubernetes_asyncio.client.V1LoadBalancerIngressDict]]
