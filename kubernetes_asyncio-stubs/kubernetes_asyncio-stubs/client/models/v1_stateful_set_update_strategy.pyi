import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1StatefulSetUpdateStrategy:
    rolling_update: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateStatefulSetStrategy]
    type: typing.Optional[str]
    
    def __init__(self, *, rolling_update: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateStatefulSetStrategy] = ..., type: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1StatefulSetUpdateStrategyDict:
        ...
class V1StatefulSetUpdateStrategyDict(typing.TypedDict, total=False):
    rollingUpdate: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateStatefulSetStrategyDict]
    type: typing.Optional[str]
