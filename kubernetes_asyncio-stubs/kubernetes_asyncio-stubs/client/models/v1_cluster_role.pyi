import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ClusterRole:
    aggregation_rule: typing.Optional[kubernetes_asyncio.client.V1AggregationRule]
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    rules: typing.Optional[list[kubernetes_asyncio.client.V1PolicyRule]]
    
    def __init__(self, *, aggregation_rule: typing.Optional[kubernetes_asyncio.client.V1AggregationRule] = ..., api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., rules: typing.Optional[list[kubernetes_asyncio.client.V1PolicyRule]] = ...) -> None:
        ...
    def to_dict(self) -> V1ClusterRoleDict:
        ...
class V1ClusterRoleDict(typing.TypedDict, total=False):
    aggregationRule: typing.Optional[kubernetes_asyncio.client.V1AggregationRuleDict]
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    rules: typing.Optional[list[kubernetes_asyncio.client.V1PolicyRuleDict]]
