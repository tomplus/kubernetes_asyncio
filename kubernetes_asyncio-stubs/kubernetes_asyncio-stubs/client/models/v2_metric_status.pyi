import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2MetricStatus:
    container_resource: typing.Optional[kubernetes_asyncio.client.V2ContainerResourceMetricStatus]
    external: typing.Optional[kubernetes_asyncio.client.V2ExternalMetricStatus]
    object: typing.Optional[kubernetes_asyncio.client.V2ObjectMetricStatus]
    pods: typing.Optional[kubernetes_asyncio.client.V2PodsMetricStatus]
    resource: typing.Optional[kubernetes_asyncio.client.V2ResourceMetricStatus]
    type: str
    
    def __init__(self, *, container_resource: typing.Optional[kubernetes_asyncio.client.V2ContainerResourceMetricStatus] = ..., external: typing.Optional[kubernetes_asyncio.client.V2ExternalMetricStatus] = ..., object: typing.Optional[kubernetes_asyncio.client.V2ObjectMetricStatus] = ..., pods: typing.Optional[kubernetes_asyncio.client.V2PodsMetricStatus] = ..., resource: typing.Optional[kubernetes_asyncio.client.V2ResourceMetricStatus] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V2MetricStatusDict:
        ...
class V2MetricStatusDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[kubernetes_asyncio.client.V2ContainerResourceMetricStatusDict]
    external: typing.Optional[kubernetes_asyncio.client.V2ExternalMetricStatusDict]
    object: typing.Optional[kubernetes_asyncio.client.V2ObjectMetricStatusDict]
    pods: typing.Optional[kubernetes_asyncio.client.V2PodsMetricStatusDict]
    resource: typing.Optional[kubernetes_asyncio.client.V2ResourceMetricStatusDict]
    type: str
