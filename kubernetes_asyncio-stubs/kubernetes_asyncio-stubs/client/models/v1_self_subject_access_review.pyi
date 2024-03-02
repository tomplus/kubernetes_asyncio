import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SelfSubjectAccessReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1SelfSubjectAccessReviewSpec
    status: typing.Optional[kubernetes_asyncio.client.V1SubjectAccessReviewStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: kubernetes_asyncio.client.V1SelfSubjectAccessReviewSpec, status: typing.Optional[kubernetes_asyncio.client.V1SubjectAccessReviewStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1SelfSubjectAccessReviewDict:
        ...
class V1SelfSubjectAccessReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1SelfSubjectAccessReviewSpecDict
    status: typing.Optional[kubernetes_asyncio.client.V1SubjectAccessReviewStatusDict]
