import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1LimitedPriorityLevelConfiguration:
    assured_concurrency_shares: typing.Optional[int]
    limit_response: typing.Optional[kubernetes_asyncio.client.V1beta1LimitResponse]
    
    def __init__(self, *, assured_concurrency_shares: typing.Optional[int] = ..., limit_response: typing.Optional[kubernetes_asyncio.client.V1beta1LimitResponse] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1LimitedPriorityLevelConfigurationDict:
        ...
class V1beta1LimitedPriorityLevelConfigurationDict(typing.TypedDict, total=False):
    assuredConcurrencyShares: typing.Optional[int]
    limitResponse: typing.Optional[kubernetes_asyncio.client.V1beta1LimitResponseDict]
