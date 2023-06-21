import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1PodCondition]]
    container_statuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatus]]
    ephemeral_container_statuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatus]]
    host_ip: typing.Optional[str]
    init_container_statuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatus]]
    message: typing.Optional[str]
    nominated_node_name: typing.Optional[str]
    phase: typing.Optional[str]
    pod_ip: typing.Optional[str]
    pod_i_ps: typing.Optional[list[kubernetes_asyncio.client.V1PodIP]]
    qos_class: typing.Optional[str]
    reason: typing.Optional[str]
    start_time: typing.Optional[datetime.datetime]
    
    def __init__(self, *, conditions: typing.Optional[list[kubernetes_asyncio.client.V1PodCondition]] = ..., container_statuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatus]] = ..., ephemeral_container_statuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatus]] = ..., host_ip: typing.Optional[str] = ..., init_container_statuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatus]] = ..., message: typing.Optional[str] = ..., nominated_node_name: typing.Optional[str] = ..., phase: typing.Optional[str] = ..., pod_ip: typing.Optional[str] = ..., pod_i_ps: typing.Optional[list[kubernetes_asyncio.client.V1PodIP]] = ..., qos_class: typing.Optional[str] = ..., reason: typing.Optional[str] = ..., start_time: typing.Optional[datetime.datetime] = ...) -> None:
        ...
    def to_dict(self) -> V1PodStatusDict:
        ...
class V1PodStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1PodConditionDict]]
    containerStatuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatusDict]]
    ephemeralContainerStatuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatusDict]]
    hostIP: typing.Optional[str]
    initContainerStatuses: typing.Optional[list[kubernetes_asyncio.client.V1ContainerStatusDict]]
    message: typing.Optional[str]
    nominatedNodeName: typing.Optional[str]
    phase: typing.Optional[str]
    podIP: typing.Optional[str]
    podIPs: typing.Optional[list[kubernetes_asyncio.client.V1PodIPDict]]
    qosClass: typing.Optional[str]
    reason: typing.Optional[str]
    startTime: typing.Optional[datetime.datetime]
