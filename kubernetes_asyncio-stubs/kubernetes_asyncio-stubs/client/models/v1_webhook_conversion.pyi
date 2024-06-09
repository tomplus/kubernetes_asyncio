import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1WebhookConversion:
    client_config: typing.Optional[kubernetes_asyncio.client.ApiextensionsV1WebhookClientConfig]
    conversion_review_versions: list[str]
    
    def __init__(self, *, client_config: typing.Optional[kubernetes_asyncio.client.ApiextensionsV1WebhookClientConfig] = ..., conversion_review_versions: list[str]) -> None:
        ...
    def to_dict(self) -> V1WebhookConversionDict:
        ...
class V1WebhookConversionDict(typing.TypedDict, total=False):
    clientConfig: typing.Optional[kubernetes_asyncio.client.ApiextensionsV1WebhookClientConfigDict]
    conversionReviewVersions: list[str]
