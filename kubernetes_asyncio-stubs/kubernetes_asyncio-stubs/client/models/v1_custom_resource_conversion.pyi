import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceConversion:
    strategy: str
    webhook: typing.Optional[kubernetes_asyncio.client.V1WebhookConversion]
    
    def __init__(self, *, strategy: str, webhook: typing.Optional[kubernetes_asyncio.client.V1WebhookConversion] = ...) -> None:
        ...
    def to_dict(self) -> V1CustomResourceConversionDict:
        ...
class V1CustomResourceConversionDict(typing.TypedDict, total=False):
    strategy: str
    webhook: typing.Optional[kubernetes_asyncio.client.V1WebhookConversionDict]
