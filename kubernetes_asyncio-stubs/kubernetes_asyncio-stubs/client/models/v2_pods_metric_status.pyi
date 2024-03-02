import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2PodsMetricStatus:
    current: kubernetes_asyncio.client.V2MetricValueStatus
    metric: kubernetes_asyncio.client.V2MetricIdentifier
    
    def __init__(self, *, current: kubernetes_asyncio.client.V2MetricValueStatus, metric: kubernetes_asyncio.client.V2MetricIdentifier) -> None:
        ...
    def to_dict(self) -> V2PodsMetricStatusDict:
        ...
class V2PodsMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes_asyncio.client.V2MetricValueStatusDict
    metric: kubernetes_asyncio.client.V2MetricIdentifierDict
