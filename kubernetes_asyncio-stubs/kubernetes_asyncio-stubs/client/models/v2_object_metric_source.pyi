import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2ObjectMetricSource:
    described_object: kubernetes_asyncio.client.V2CrossVersionObjectReference
    metric: kubernetes_asyncio.client.V2MetricIdentifier
    target: kubernetes_asyncio.client.V2MetricTarget
    
    def __init__(self, *, described_object: kubernetes_asyncio.client.V2CrossVersionObjectReference, metric: kubernetes_asyncio.client.V2MetricIdentifier, target: kubernetes_asyncio.client.V2MetricTarget) -> None:
        ...
    def to_dict(self) -> V2ObjectMetricSourceDict:
        ...
class V2ObjectMetricSourceDict(typing.TypedDict, total=False):
    describedObject: kubernetes_asyncio.client.V2CrossVersionObjectReferenceDict
    metric: kubernetes_asyncio.client.V2MetricIdentifierDict
    target: kubernetes_asyncio.client.V2MetricTargetDict
