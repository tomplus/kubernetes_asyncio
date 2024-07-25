import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2ObjectMetricStatus:
    current: kubernetes_asyncio.client.V2MetricValueStatus
    described_object: kubernetes_asyncio.client.V2CrossVersionObjectReference
    metric: kubernetes_asyncio.client.V2MetricIdentifier
    
    def __init__(self, *, current: kubernetes_asyncio.client.V2MetricValueStatus, described_object: kubernetes_asyncio.client.V2CrossVersionObjectReference, metric: kubernetes_asyncio.client.V2MetricIdentifier) -> None:
        ...
    def to_dict(self) -> V2ObjectMetricStatusDict:
        ...
class V2ObjectMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes_asyncio.client.V2MetricValueStatusDict
    describedObject: kubernetes_asyncio.client.V2CrossVersionObjectReferenceDict
    metric: kubernetes_asyncio.client.V2MetricIdentifierDict
