import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Affinity:
    node_affinity: typing.Optional[kubernetes_asyncio.client.V1NodeAffinity]
    pod_affinity: typing.Optional[kubernetes_asyncio.client.V1PodAffinity]
    pod_anti_affinity: typing.Optional[kubernetes_asyncio.client.V1PodAntiAffinity]
    
    def __init__(self, *, node_affinity: typing.Optional[kubernetes_asyncio.client.V1NodeAffinity] = ..., pod_affinity: typing.Optional[kubernetes_asyncio.client.V1PodAffinity] = ..., pod_anti_affinity: typing.Optional[kubernetes_asyncio.client.V1PodAntiAffinity] = ...) -> None:
        ...
    def to_dict(self) -> V1AffinityDict:
        ...
class V1AffinityDict(typing.TypedDict, total=False):
    nodeAffinity: typing.Optional[kubernetes_asyncio.client.V1NodeAffinityDict]
    podAffinity: typing.Optional[kubernetes_asyncio.client.V1PodAffinityDict]
    podAntiAffinity: typing.Optional[kubernetes_asyncio.client.V1PodAntiAffinityDict]
