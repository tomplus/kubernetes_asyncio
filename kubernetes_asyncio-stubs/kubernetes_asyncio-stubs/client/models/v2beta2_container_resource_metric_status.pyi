import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2ContainerResourceMetricStatus:
    container: str
    current: kubernetes_asyncio.client.V2beta2MetricValueStatus
    name: str
    
    def __init__(self, *, container: str, current: kubernetes_asyncio.client.V2beta2MetricValueStatus, name: str) -> None:
        ...
    def to_dict(self) -> V2beta2ContainerResourceMetricStatusDict:
        ...
class V2beta2ContainerResourceMetricStatusDict(typing.TypedDict, total=False):
    container: str
    current: kubernetes_asyncio.client.V2beta2MetricValueStatusDict
    name: str
