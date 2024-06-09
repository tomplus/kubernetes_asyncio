import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RollingUpdateStatefulSetStrategy:
    max_unavailable: typing.Optional[typing.Any]
    partition: typing.Optional[int]
    
    def __init__(self, *, max_unavailable: typing.Optional[typing.Any] = ..., partition: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1RollingUpdateStatefulSetStrategyDict:
        ...
class V1RollingUpdateStatefulSetStrategyDict(typing.TypedDict, total=False):
    maxUnavailable: typing.Optional[typing.Any]
    partition: typing.Optional[int]
