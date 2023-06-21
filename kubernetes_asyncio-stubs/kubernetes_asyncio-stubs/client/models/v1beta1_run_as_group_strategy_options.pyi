import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1RunAsGroupStrategyOptions:
    ranges: typing.Optional[list[kubernetes_asyncio.client.V1beta1IDRange]]
    rule: str
    
    def __init__(self, *, ranges: typing.Optional[list[kubernetes_asyncio.client.V1beta1IDRange]] = ..., rule: str) -> None:
        ...
    def to_dict(self) -> V1beta1RunAsGroupStrategyOptionsDict:
        ...
class V1beta1RunAsGroupStrategyOptionsDict(typing.TypedDict, total=False):
    ranges: typing.Optional[list[kubernetes_asyncio.client.V1beta1IDRangeDict]]
    rule: str
