import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ServiceStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    load_balancer: typing.Optional[kubernetes_asyncio.client.V1LoadBalancerStatus]
    
    def __init__(self, *, conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ..., load_balancer: typing.Optional[kubernetes_asyncio.client.V1LoadBalancerStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1ServiceStatusDict:
        ...
class V1ServiceStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ConditionDict]]
    loadBalancer: typing.Optional[kubernetes_asyncio.client.V1LoadBalancerStatusDict]
