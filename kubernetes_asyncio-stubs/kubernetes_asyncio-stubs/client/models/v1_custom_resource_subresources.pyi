import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceSubresources:
    scale: typing.Optional[kubernetes_asyncio.client.V1CustomResourceSubresourceScale]
    status: typing.Optional[typing.Any]
    
    def __init__(self, *, scale: typing.Optional[kubernetes_asyncio.client.V1CustomResourceSubresourceScale] = ..., status: typing.Optional[typing.Any] = ...) -> None:
        ...
    def to_dict(self) -> V1CustomResourceSubresourcesDict:
        ...
class V1CustomResourceSubresourcesDict(typing.TypedDict, total=False):
    scale: typing.Optional[kubernetes_asyncio.client.V1CustomResourceSubresourceScaleDict]
    status: typing.Optional[typing.Any]
