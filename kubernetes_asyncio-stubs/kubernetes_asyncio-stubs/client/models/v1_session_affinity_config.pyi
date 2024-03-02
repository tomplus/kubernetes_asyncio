import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SessionAffinityConfig:
    client_ip: typing.Optional[kubernetes_asyncio.client.V1ClientIPConfig]
    
    def __init__(self, *, client_ip: typing.Optional[kubernetes_asyncio.client.V1ClientIPConfig] = ...) -> None:
        ...
    def to_dict(self) -> V1SessionAffinityConfigDict:
        ...
class V1SessionAffinityConfigDict(typing.TypedDict, total=False):
    clientIP: typing.Optional[kubernetes_asyncio.client.V1ClientIPConfigDict]
