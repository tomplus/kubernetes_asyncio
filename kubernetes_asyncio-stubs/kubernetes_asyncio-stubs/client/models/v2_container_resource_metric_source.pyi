import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2ContainerResourceMetricSource:
    container: str
    name: str
    target: kubernetes_asyncio.client.V2MetricTarget
    
    def __init__(self, *, container: str, name: str, target: kubernetes_asyncio.client.V2MetricTarget) -> None:
        ...
    def to_dict(self) -> V2ContainerResourceMetricSourceDict:
        ...
class V2ContainerResourceMetricSourceDict(typing.TypedDict, total=False):
    container: str
    name: str
    target: kubernetes_asyncio.client.V2MetricTargetDict
