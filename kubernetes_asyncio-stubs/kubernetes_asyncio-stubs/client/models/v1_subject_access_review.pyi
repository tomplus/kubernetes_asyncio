import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SubjectAccessReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1SubjectAccessReviewSpec
    status: typing.Optional[kubernetes_asyncio.client.V1SubjectAccessReviewStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: kubernetes_asyncio.client.V1SubjectAccessReviewSpec, status: typing.Optional[kubernetes_asyncio.client.V1SubjectAccessReviewStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1SubjectAccessReviewDict:
        ...
class V1SubjectAccessReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1SubjectAccessReviewSpecDict
    status: typing.Optional[kubernetes_asyncio.client.V1SubjectAccessReviewStatusDict]
