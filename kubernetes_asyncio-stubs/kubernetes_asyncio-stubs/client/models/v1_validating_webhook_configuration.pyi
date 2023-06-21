import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ValidatingWebhookConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    webhooks: typing.Optional[list[kubernetes_asyncio.client.V1ValidatingWebhook]]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., webhooks: typing.Optional[list[kubernetes_asyncio.client.V1ValidatingWebhook]] = ...) -> None:
        ...
    def to_dict(self) -> V1ValidatingWebhookConfigurationDict:
        ...
class V1ValidatingWebhookConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    webhooks: typing.Optional[list[kubernetes_asyncio.client.V1ValidatingWebhookDict]]
