import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NetworkPolicyStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    
    def __init__(self, *, conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...) -> None:
        ...
    def to_dict(self) -> V1NetworkPolicyStatusDict:
        ...
class V1NetworkPolicyStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ConditionDict]]
