import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SelfSubjectRulesReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1SelfSubjectRulesReviewSpec
    status: typing.Optional[kubernetes_asyncio.client.V1SubjectRulesReviewStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: kubernetes_asyncio.client.V1SelfSubjectRulesReviewSpec, status: typing.Optional[kubernetes_asyncio.client.V1SubjectRulesReviewStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1SelfSubjectRulesReviewDict:
        ...
class V1SelfSubjectRulesReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1SelfSubjectRulesReviewSpecDict
    status: typing.Optional[kubernetes_asyncio.client.V1SubjectRulesReviewStatusDict]
