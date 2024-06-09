import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EndpointAddress:
    hostname: typing.Optional[str]
    ip: str
    node_name: typing.Optional[str]
    target_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectReference]
    
    def __init__(self, *, hostname: typing.Optional[str] = ..., ip: str, node_name: typing.Optional[str] = ..., target_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectReference] = ...) -> None:
        ...
    def to_dict(self) -> V1EndpointAddressDict:
        ...
class V1EndpointAddressDict(typing.TypedDict, total=False):
    hostname: typing.Optional[str]
    ip: str
    nodeName: typing.Optional[str]
    targetRef: typing.Optional[kubernetes_asyncio.client.V1ObjectReferenceDict]
