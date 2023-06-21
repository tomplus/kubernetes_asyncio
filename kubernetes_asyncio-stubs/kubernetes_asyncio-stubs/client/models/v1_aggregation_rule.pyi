import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1AggregationRule:
    cluster_role_selectors: typing.Optional[list[kubernetes_asyncio.client.V1LabelSelector]]
    
    def __init__(self, *, cluster_role_selectors: typing.Optional[list[kubernetes_asyncio.client.V1LabelSelector]] = ...) -> None:
        ...
    def to_dict(self) -> V1AggregationRuleDict:
        ...
class V1AggregationRuleDict(typing.TypedDict, total=False):
    clusterRoleSelectors: typing.Optional[list[kubernetes_asyncio.client.V1LabelSelectorDict]]
