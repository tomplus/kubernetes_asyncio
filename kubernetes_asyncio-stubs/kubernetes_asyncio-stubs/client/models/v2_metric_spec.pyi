import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2MetricSpec:
    container_resource: typing.Optional[kubernetes_asyncio.client.V2ContainerResourceMetricSource]
    external: typing.Optional[kubernetes_asyncio.client.V2ExternalMetricSource]
    object: typing.Optional[kubernetes_asyncio.client.V2ObjectMetricSource]
    pods: typing.Optional[kubernetes_asyncio.client.V2PodsMetricSource]
    resource: typing.Optional[kubernetes_asyncio.client.V2ResourceMetricSource]
    type: str
    
    def __init__(self, *, container_resource: typing.Optional[kubernetes_asyncio.client.V2ContainerResourceMetricSource] = ..., external: typing.Optional[kubernetes_asyncio.client.V2ExternalMetricSource] = ..., object: typing.Optional[kubernetes_asyncio.client.V2ObjectMetricSource] = ..., pods: typing.Optional[kubernetes_asyncio.client.V2PodsMetricSource] = ..., resource: typing.Optional[kubernetes_asyncio.client.V2ResourceMetricSource] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V2MetricSpecDict:
        ...
class V2MetricSpecDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[kubernetes_asyncio.client.V2ContainerResourceMetricSourceDict]
    external: typing.Optional[kubernetes_asyncio.client.V2ExternalMetricSourceDict]
    object: typing.Optional[kubernetes_asyncio.client.V2ObjectMetricSourceDict]
    pods: typing.Optional[kubernetes_asyncio.client.V2PodsMetricSourceDict]
    resource: typing.Optional[kubernetes_asyncio.client.V2ResourceMetricSourceDict]
    type: str
