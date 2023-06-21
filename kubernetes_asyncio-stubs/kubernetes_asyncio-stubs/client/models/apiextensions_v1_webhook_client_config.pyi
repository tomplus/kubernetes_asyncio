import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class ApiextensionsV1WebhookClientConfig:
    ca_bundle: typing.Optional[str]
    service: typing.Optional[kubernetes_asyncio.client.ApiextensionsV1ServiceReference]
    url: typing.Optional[str]
    
    def __init__(self, *, ca_bundle: typing.Optional[str] = ..., service: typing.Optional[kubernetes_asyncio.client.ApiextensionsV1ServiceReference] = ..., url: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> ApiextensionsV1WebhookClientConfigDict:
        ...
class ApiextensionsV1WebhookClientConfigDict(typing.TypedDict, total=False):
    caBundle: typing.Optional[str]
    service: typing.Optional[kubernetes_asyncio.client.ApiextensionsV1ServiceReferenceDict]
    url: typing.Optional[str]
