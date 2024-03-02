import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RollingUpdateDaemonSet:
    max_surge: typing.Optional[typing.Any]
    max_unavailable: typing.Optional[typing.Any]
    
    def __init__(self, *, max_surge: typing.Optional[typing.Any] = ..., max_unavailable: typing.Optional[typing.Any] = ...) -> None:
        ...
    def to_dict(self) -> V1RollingUpdateDaemonSetDict:
        ...
class V1RollingUpdateDaemonSetDict(typing.TypedDict, total=False):
    maxSurge: typing.Optional[typing.Any]
    maxUnavailable: typing.Optional[typing.Any]
