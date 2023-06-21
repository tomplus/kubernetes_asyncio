import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1TopologySpreadConstraint:
    label_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    max_skew: int
    min_domains: typing.Optional[int]
    topology_key: str
    when_unsatisfiable: str
    
    def __init__(self, *, label_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., max_skew: int, min_domains: typing.Optional[int] = ..., topology_key: str, when_unsatisfiable: str) -> None:
        ...
    def to_dict(self) -> V1TopologySpreadConstraintDict:
        ...
class V1TopologySpreadConstraintDict(typing.TypedDict, total=False):
    labelSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    maxSkew: int
    minDomains: typing.Optional[int]
    topologyKey: str
    whenUnsatisfiable: str
