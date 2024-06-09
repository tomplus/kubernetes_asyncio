import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1ExternalMetricStatus:
    current_average_value: typing.Optional[str]
    current_value: str
    metric_name: str
    metric_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    
    def __init__(self, *, current_average_value: typing.Optional[str] = ..., current_value: str, metric_name: str, metric_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ...) -> None:
        ...
    def to_dict(self) -> V2beta1ExternalMetricStatusDict:
        ...
class V2beta1ExternalMetricStatusDict(typing.TypedDict, total=False):
    currentAverageValue: typing.Optional[str]
    currentValue: str
    metricName: str
    metricSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
