import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodDNSConfigOption:
    name: typing.Optional[str]
    value: typing.Optional[str]
    
    def __init__(self, *, name: typing.Optional[str] = ..., value: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1PodDNSConfigOptionDict:
        ...
class V1PodDNSConfigOptionDict(typing.TypedDict, total=False):
    name: typing.Optional[str]
    value: typing.Optional[str]
