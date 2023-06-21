import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1TokenReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1TokenReviewSpec
    status: typing.Optional[kubernetes_asyncio.client.V1TokenReviewStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: kubernetes_asyncio.client.V1TokenReviewSpec, status: typing.Optional[kubernetes_asyncio.client.V1TokenReviewStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1TokenReviewDict:
        ...
class V1TokenReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1TokenReviewSpecDict
    status: typing.Optional[kubernetes_asyncio.client.V1TokenReviewStatusDict]
