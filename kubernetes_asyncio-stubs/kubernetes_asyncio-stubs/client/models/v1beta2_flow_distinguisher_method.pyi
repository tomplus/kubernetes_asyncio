import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2FlowDistinguisherMethod:
    type: str
    
    def __init__(self, *, type: str) -> None:
        ...
    def to_dict(self) -> V1beta2FlowDistinguisherMethodDict:
        ...
class V1beta2FlowDistinguisherMethodDict(typing.TypedDict, total=False):
    type: str
