import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1ContainerResourceMetricStatus:
    container: str
    current_average_utilization: typing.Optional[int]
    current_average_value: str
    name: str
    
    def __init__(self, *, container: str, current_average_utilization: typing.Optional[int] = ..., current_average_value: str, name: str) -> None:
        ...
    def to_dict(self) -> V2beta1ContainerResourceMetricStatusDict:
        ...
class V2beta1ContainerResourceMetricStatusDict(typing.TypedDict, total=False):
    container: str
    currentAverageUtilization: typing.Optional[int]
    currentAverageValue: str
    name: str
