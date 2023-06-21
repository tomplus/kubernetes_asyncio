import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeSpec:
    config_source: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource]
    external_id: typing.Optional[str]
    pod_cidr: typing.Optional[str]
    pod_cid_rs: typing.Optional[list[str]]
    provider_id: typing.Optional[str]
    taints: typing.Optional[list[kubernetes_asyncio.client.V1Taint]]
    unschedulable: typing.Optional[bool]
    
    def __init__(self, *, config_source: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSource] = ..., external_id: typing.Optional[str] = ..., pod_cidr: typing.Optional[str] = ..., pod_cid_rs: typing.Optional[list[str]] = ..., provider_id: typing.Optional[str] = ..., taints: typing.Optional[list[kubernetes_asyncio.client.V1Taint]] = ..., unschedulable: typing.Optional[bool] = ...) -> None:
        ...
    def to_dict(self) -> V1NodeSpecDict:
        ...
class V1NodeSpecDict(typing.TypedDict, total=False):
    configSource: typing.Optional[kubernetes_asyncio.client.V1NodeConfigSourceDict]
    externalID: typing.Optional[str]
    podCIDR: typing.Optional[str]
    podCIDRs: typing.Optional[list[str]]
    providerID: typing.Optional[str]
    taints: typing.Optional[list[kubernetes_asyncio.client.V1TaintDict]]
    unschedulable: typing.Optional[bool]
