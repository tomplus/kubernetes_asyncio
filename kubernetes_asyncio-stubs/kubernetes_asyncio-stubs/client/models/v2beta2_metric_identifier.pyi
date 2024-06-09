import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2MetricIdentifier:
    name: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    
    def __init__(self, *, name: str, selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ...) -> None:
        ...
    def to_dict(self) -> V2beta2MetricIdentifierDict:
        ...
class V2beta2MetricIdentifierDict(typing.TypedDict, total=False):
    name: str
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
