import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2ObjectMetricStatus:
    current: kubernetes_asyncio.client.V2beta2MetricValueStatus
    described_object: kubernetes_asyncio.client.V2beta2CrossVersionObjectReference
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifier
    
    def __init__(self, *, current: kubernetes_asyncio.client.V2beta2MetricValueStatus, described_object: kubernetes_asyncio.client.V2beta2CrossVersionObjectReference, metric: kubernetes_asyncio.client.V2beta2MetricIdentifier) -> None:
        ...
    def to_dict(self) -> V2beta2ObjectMetricStatusDict:
        ...
class V2beta2ObjectMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes_asyncio.client.V2beta2MetricValueStatusDict
    describedObject: kubernetes_asyncio.client.V2beta2CrossVersionObjectReferenceDict
    metric: kubernetes_asyncio.client.V2beta2MetricIdentifierDict
