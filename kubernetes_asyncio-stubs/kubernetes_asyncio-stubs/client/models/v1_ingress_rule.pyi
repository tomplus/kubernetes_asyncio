import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1IngressRule:
    host: typing.Optional[str]
    http: typing.Optional[kubernetes_asyncio.client.V1HTTPIngressRuleValue]
    
    def __init__(self, *, host: typing.Optional[str] = ..., http: typing.Optional[kubernetes_asyncio.client.V1HTTPIngressRuleValue] = ...) -> None:
        ...
    def to_dict(self) -> V1IngressRuleDict:
        ...
class V1IngressRuleDict(typing.TypedDict, total=False):
    host: typing.Optional[str]
    http: typing.Optional[kubernetes_asyncio.client.V1HTTPIngressRuleValueDict]
