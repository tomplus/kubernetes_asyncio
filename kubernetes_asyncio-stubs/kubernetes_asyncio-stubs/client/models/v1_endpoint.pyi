import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Endpoint:
    addresses: list[str]
    conditions: typing.Optional[kubernetes_asyncio.client.V1EndpointConditions]
    deprecated_topology: typing.Optional[dict[str, str]]
    hints: typing.Optional[kubernetes_asyncio.client.V1EndpointHints]
    hostname: typing.Optional[str]
    node_name: typing.Optional[str]
    target_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectReference]
    zone: typing.Optional[str]
    
    def __init__(self, *, addresses: list[str], conditions: typing.Optional[kubernetes_asyncio.client.V1EndpointConditions] = ..., deprecated_topology: typing.Optional[dict[str, str]] = ..., hints: typing.Optional[kubernetes_asyncio.client.V1EndpointHints] = ..., hostname: typing.Optional[str] = ..., node_name: typing.Optional[str] = ..., target_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectReference] = ..., zone: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1EndpointDict:
        ...
class V1EndpointDict(typing.TypedDict, total=False):
    addresses: list[str]
    conditions: typing.Optional[kubernetes_asyncio.client.V1EndpointConditionsDict]
    deprecatedTopology: typing.Optional[dict[str, str]]
    hints: typing.Optional[kubernetes_asyncio.client.V1EndpointHintsDict]
    hostname: typing.Optional[str]
    nodeName: typing.Optional[str]
    targetRef: typing.Optional[kubernetes_asyncio.client.V1ObjectReferenceDict]
    zone: typing.Optional[str]
