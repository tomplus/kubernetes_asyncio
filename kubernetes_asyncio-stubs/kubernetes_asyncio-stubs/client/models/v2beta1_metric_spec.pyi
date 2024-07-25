import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta1MetricSpec:
    container_resource: typing.Optional[kubernetes_asyncio.client.V2beta1ContainerResourceMetricSource]
    external: typing.Optional[kubernetes_asyncio.client.V2beta1ExternalMetricSource]
    object: typing.Optional[kubernetes_asyncio.client.V2beta1ObjectMetricSource]
    pods: typing.Optional[kubernetes_asyncio.client.V2beta1PodsMetricSource]
    resource: typing.Optional[kubernetes_asyncio.client.V2beta1ResourceMetricSource]
    type: str
    
    def __init__(self, *, container_resource: typing.Optional[kubernetes_asyncio.client.V2beta1ContainerResourceMetricSource] = ..., external: typing.Optional[kubernetes_asyncio.client.V2beta1ExternalMetricSource] = ..., object: typing.Optional[kubernetes_asyncio.client.V2beta1ObjectMetricSource] = ..., pods: typing.Optional[kubernetes_asyncio.client.V2beta1PodsMetricSource] = ..., resource: typing.Optional[kubernetes_asyncio.client.V2beta1ResourceMetricSource] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V2beta1MetricSpecDict:
        ...
class V2beta1MetricSpecDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[kubernetes_asyncio.client.V2beta1ContainerResourceMetricSourceDict]
    external: typing.Optional[kubernetes_asyncio.client.V2beta1ExternalMetricSourceDict]
    object: typing.Optional[kubernetes_asyncio.client.V2beta1ObjectMetricSourceDict]
    pods: typing.Optional[kubernetes_asyncio.client.V2beta1PodsMetricSourceDict]
    resource: typing.Optional[kubernetes_asyncio.client.V2beta1ResourceMetricSourceDict]
    type: str
