import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2ResourceMetricStatus:
    current: kubernetes_asyncio.client.V2MetricValueStatus
    name: str
    
    def __init__(self, *, current: kubernetes_asyncio.client.V2MetricValueStatus, name: str) -> None:
        ...
    def to_dict(self) -> V2ResourceMetricStatusDict:
        ...
class V2ResourceMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes_asyncio.client.V2MetricValueStatusDict
    name: str
