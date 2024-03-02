import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2ContainerResourceMetricStatus:
    container: str
    current: kubernetes_asyncio.client.V2MetricValueStatus
    name: str
    
    def __init__(self, *, container: str, current: kubernetes_asyncio.client.V2MetricValueStatus, name: str) -> None:
        ...
    def to_dict(self) -> V2ContainerResourceMetricStatusDict:
        ...
class V2ContainerResourceMetricStatusDict(typing.TypedDict, total=False):
    container: str
    current: kubernetes_asyncio.client.V2MetricValueStatusDict
    name: str
