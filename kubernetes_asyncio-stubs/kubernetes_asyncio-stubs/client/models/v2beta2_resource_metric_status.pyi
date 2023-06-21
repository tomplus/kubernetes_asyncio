import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2ResourceMetricStatus:
    current: kubernetes_asyncio.client.V2beta2MetricValueStatus
    name: str
    
    def __init__(self, *, current: kubernetes_asyncio.client.V2beta2MetricValueStatus, name: str) -> None:
        ...
    def to_dict(self) -> V2beta2ResourceMetricStatusDict:
        ...
class V2beta2ResourceMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes_asyncio.client.V2beta2MetricValueStatusDict
    name: str
