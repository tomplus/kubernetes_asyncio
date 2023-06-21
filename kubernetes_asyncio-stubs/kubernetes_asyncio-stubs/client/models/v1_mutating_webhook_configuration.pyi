import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1MutatingWebhookConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    webhooks: typing.Optional[list[kubernetes_asyncio.client.V1MutatingWebhook]]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., webhooks: typing.Optional[list[kubernetes_asyncio.client.V1MutatingWebhook]] = ...) -> None:
        ...
    def to_dict(self) -> V1MutatingWebhookConfigurationDict:
        ...
class V1MutatingWebhookConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    webhooks: typing.Optional[list[kubernetes_asyncio.client.V1MutatingWebhookDict]]
