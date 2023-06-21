import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2PodsMetricSource:
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifier
    target: kubernetes_asyncio.client.V2beta2MetricTarget
    
    def __init__(self, *, metric: kubernetes_asyncio.client.V2beta2MetricIdentifier, target: kubernetes_asyncio.client.V2beta2MetricTarget) -> None:
        ...
    def to_dict(self) -> V2beta2PodsMetricSourceDict:
        ...
class V2beta2PodsMetricSourceDict(typing.TypedDict, total=False):
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifierDict
    target: kubernetes_asyncio.client.V2beta2MetricTargetDict
