import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1FlowDistinguisherMethod:
    type: str
    
    def __init__(self, *, type: str) -> None:
        ...
    def to_dict(self) -> V1beta1FlowDistinguisherMethodDict:
        ...
class V1beta1FlowDistinguisherMethodDict(typing.TypedDict, total=False):
    type: str
