import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1PodsMetricStatus:
    current_average_value: str
    metric_name: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    
    def __init__(self, *, current_average_value: str, metric_name: str, selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ...) -> None:
        ...
    def to_dict(self) -> V2beta1PodsMetricStatusDict:
        ...
class V2beta1PodsMetricStatusDict(typing.TypedDict, total=False):
    currentAverageValue: str
    metricName: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
