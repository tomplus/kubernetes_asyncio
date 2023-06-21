import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DaemonEndpoint:
    port: int
    
    def __init__(self, *, port: int) -> None:
        ...
    def to_dict(self) -> V1DaemonEndpointDict:
        ...
class V1DaemonEndpointDict(typing.TypedDict, total=False):
    Port: int
