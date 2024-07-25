import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1ObjectMetricStatus:
    average_value: typing.Optional[str]
    current_value: str
    metric_name: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    target: kubernetes_asyncio.client.V2beta1CrossVersionObjectReference
    
    def __init__(self, *, average_value: typing.Optional[str] = ..., current_value: str, metric_name: str, selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., target: kubernetes_asyncio.client.V2beta1CrossVersionObjectReference) -> None:
        ...
    def to_dict(self) -> V2beta1ObjectMetricStatusDict:
        ...
class V2beta1ObjectMetricStatusDict(typing.TypedDict, total=False):
    averageValue: typing.Optional[str]
    currentValue: str
    metricName: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    target: kubernetes_asyncio.client.V2beta1CrossVersionObjectReferenceDict
