import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2PodsMetricSource:
    metric: kubernetes_asyncio.client.V2MetricIdentifier
    target: kubernetes_asyncio.client.V2MetricTarget
    
    def __init__(self, *, metric: kubernetes_asyncio.client.V2MetricIdentifier, target: kubernetes_asyncio.client.V2MetricTarget) -> None:
        ...
    def to_dict(self) -> V2PodsMetricSourceDict:
        ...
class V2PodsMetricSourceDict(typing.TypedDict, total=False):
    metric: kubernetes_asyncio.client.V2MetricIdentifierDict
    target: kubernetes_asyncio.client.V2MetricTargetDict
