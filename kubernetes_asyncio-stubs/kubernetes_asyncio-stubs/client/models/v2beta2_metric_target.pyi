import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2MetricTarget:
    average_utilization: typing.Optional[int]
    average_value: typing.Optional[str]
    type: str
    value: typing.Optional[str]
    
    def __init__(self, *, average_utilization: typing.Optional[int] = ..., average_value: typing.Optional[str] = ..., type: str, value: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V2beta2MetricTargetDict:
        ...
class V2beta2MetricTargetDict(typing.TypedDict, total=False):
    averageUtilization: typing.Optional[int]
    averageValue: typing.Optional[str]
    type: str
    value: typing.Optional[str]
