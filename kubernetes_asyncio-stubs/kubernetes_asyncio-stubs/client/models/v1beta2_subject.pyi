import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2Subject:
    group: typing.Optional[kubernetes_asyncio.client.V1beta2GroupSubject]
    kind: str
    service_account: typing.Optional[kubernetes_asyncio.client.V1beta2ServiceAccountSubject]
    user: typing.Optional[kubernetes_asyncio.client.V1beta2UserSubject]
    
    def __init__(self, *, group: typing.Optional[kubernetes_asyncio.client.V1beta2GroupSubject] = ..., kind: str, service_account: typing.Optional[kubernetes_asyncio.client.V1beta2ServiceAccountSubject] = ..., user: typing.Optional[kubernetes_asyncio.client.V1beta2UserSubject] = ...) -> None:
        ...
    def to_dict(self) -> V1beta2SubjectDict:
        ...
class V1beta2SubjectDict(typing.TypedDict, total=False):
    group: typing.Optional[kubernetes_asyncio.client.V1beta2GroupSubjectDict]
    kind: str
    serviceAccount: typing.Optional[kubernetes_asyncio.client.V1beta2ServiceAccountSubjectDict]
    user: typing.Optional[kubernetes_asyncio.client.V1beta2UserSubjectDict]
