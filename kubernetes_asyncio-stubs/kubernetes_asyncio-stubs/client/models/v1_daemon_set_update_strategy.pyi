import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DaemonSetUpdateStrategy:
    rolling_update: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateDaemonSet]
    type: typing.Optional[str]
    
    def __init__(self, *, rolling_update: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateDaemonSet] = ..., type: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1DaemonSetUpdateStrategyDict:
        ...
class V1DaemonSetUpdateStrategyDict(typing.TypedDict, total=False):
    rollingUpdate: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateDaemonSetDict]
    type: typing.Optional[str]
