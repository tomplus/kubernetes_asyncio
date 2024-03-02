import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1ResourceMetricSource:
    name: str
    target_average_utilization: typing.Optional[int]
    target_average_value: typing.Optional[str]
    
    def __init__(self, *, name: str, target_average_utilization: typing.Optional[int] = ..., target_average_value: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V2beta1ResourceMetricSourceDict:
        ...
class V2beta1ResourceMetricSourceDict(typing.TypedDict, total=False):
    name: str
    targetAverageUtilization: typing.Optional[int]
    targetAverageValue: typing.Optional[str]
