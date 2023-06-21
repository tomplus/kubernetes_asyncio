import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2ObjectMetricSource:
    described_object: kubernetes_asyncio.client.V2beta2CrossVersionObjectReference
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifier
    target: kubernetes_asyncio.client.V2beta2MetricTarget
    
    def __init__(self, *, described_object: kubernetes_asyncio.client.V2beta2CrossVersionObjectReference, metric: kubernetes_asyncio.client.V2beta2MetricIdentifier, target: kubernetes_asyncio.client.V2beta2MetricTarget) -> None:
        ...
    def to_dict(self) -> V2beta2ObjectMetricSourceDict:
        ...
class V2beta2ObjectMetricSourceDict(typing.TypedDict, total=False):
    describedObject: kubernetes_asyncio.client.V2beta2CrossVersionObjectReferenceDict
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifierDict
    target: kubernetes_asyncio.client.V2beta2MetricTargetDict
