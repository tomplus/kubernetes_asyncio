import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ServerAddressByClientCIDR:
    client_cidr: str
    server_address: str
    
    def __init__(self, *, client_cidr: str, server_address: str) -> None:
        ...
    def to_dict(self) -> V1ServerAddressByClientCIDRDict:
        ...
class V1ServerAddressByClientCIDRDict(typing.TypedDict, total=False):
    clientCIDR: str
    serverAddress: str
