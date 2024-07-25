import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1ObjectMetricSource:
    average_value: typing.Optional[str]
    metric_name: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    target: kubernetes_asyncio.client.V2beta1CrossVersionObjectReference
    target_value: str
    
    def __init__(self, *, average_value: typing.Optional[str] = ..., metric_name: str, selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., target: kubernetes_asyncio.client.V2beta1CrossVersionObjectReference, target_value: str) -> None:
        ...
    def to_dict(self) -> V2beta1ObjectMetricSourceDict:
        ...
class V2beta1ObjectMetricSourceDict(typing.TypedDict, total=False):
    averageValue: typing.Optional[str]
    metricName: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    target: kubernetes_asyncio.client.V2beta1CrossVersionObjectReferenceDict
    targetValue: str
