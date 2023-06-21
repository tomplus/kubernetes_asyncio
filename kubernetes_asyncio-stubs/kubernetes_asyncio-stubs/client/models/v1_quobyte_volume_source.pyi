import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1QuobyteVolumeSource:
    group: typing.Optional[str]
    read_only: typing.Optional[bool]
    registry: str
    tenant: typing.Optional[str]
    user: typing.Optional[str]
    volume: str
    
    def __init__(self, *, group: typing.Optional[str] = ..., read_only: typing.Optional[bool] = ..., registry: str, tenant: typing.Optional[str] = ..., user: typing.Optional[str] = ..., volume: str) -> None:
        ...
    def to_dict(self) -> V1QuobyteVolumeSourceDict:
        ...
class V1QuobyteVolumeSourceDict(typing.TypedDict, total=False):
    group: typing.Optional[str]
    readOnly: typing.Optional[bool]
    registry: str
    tenant: typing.Optional[str]
    user: typing.Optional[str]
    volume: str
