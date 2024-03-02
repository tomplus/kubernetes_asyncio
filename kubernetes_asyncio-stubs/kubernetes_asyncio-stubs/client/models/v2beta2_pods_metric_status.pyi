import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2PodsMetricStatus:
    current: kubernetes_asyncio.client.V2beta2MetricValueStatus
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifier
    
    def __init__(self, *, current: kubernetes_asyncio.client.V2beta2MetricValueStatus, metric: kubernetes_asyncio.client.V2beta2MetricIdentifier) -> None:
        ...
    def to_dict(self) -> V2beta2PodsMetricStatusDict:
        ...
class V2beta2PodsMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes_asyncio.client.V2beta2MetricValueStatusDict
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifierDict
