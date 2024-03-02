import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1HTTPIngressRuleValue:
    paths: list[kubernetes_asyncio.client.V1HTTPIngressPath]
    
    def __init__(self, *, paths: list[kubernetes_asyncio.client.V1HTTPIngressPath]) -> None:
        ...
    def to_dict(self) -> V1HTTPIngressRuleValueDict:
        ...
class V1HTTPIngressRuleValueDict(typing.TypedDict, total=False):
    paths: list[kubernetes_asyncio.client.V1HTTPIngressPathDict]
