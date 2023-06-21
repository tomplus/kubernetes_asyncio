import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceQuotaStatus:
    hard: typing.Optional[dict[str, str]]
    used: typing.Optional[dict[str, str]]
    
    def __init__(self, *, hard: typing.Optional[dict[str, str]] = ..., used: typing.Optional[dict[str, str]] = ...) -> None:
        ...
    def to_dict(self) -> V1ResourceQuotaStatusDict:
        ...
class V1ResourceQuotaStatusDict(typing.TypedDict, total=False):
    hard: typing.Optional[dict[str, str]]
    used: typing.Optional[dict[str, str]]
