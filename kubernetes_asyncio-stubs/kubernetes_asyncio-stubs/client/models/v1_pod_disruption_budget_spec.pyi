import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodDisruptionBudgetSpec:
    max_unavailable: typing.Optional[typing.Any]
    min_available: typing.Optional[typing.Any]
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    
    def __init__(self, *, max_unavailable: typing.Optional[typing.Any] = ..., min_available: typing.Optional[typing.Any] = ..., selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ...) -> None:
        ...
    def to_dict(self) -> V1PodDisruptionBudgetSpecDict:
        ...
class V1PodDisruptionBudgetSpecDict(typing.TypedDict, total=False):
    maxUnavailable: typing.Optional[typing.Any]
    minAvailable: typing.Optional[typing.Any]
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
