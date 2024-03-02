import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1LimitResponse:
    queuing: typing.Optional[kubernetes_asyncio.client.V1beta1QueuingConfiguration]
    type: str
    
    def __init__(self, *, queuing: typing.Optional[kubernetes_asyncio.client.V1beta1QueuingConfiguration] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V1beta1LimitResponseDict:
        ...
class V1beta1LimitResponseDict(typing.TypedDict, total=False):
    queuing: typing.Optional[kubernetes_asyncio.client.V1beta1QueuingConfigurationDict]
    type: str
