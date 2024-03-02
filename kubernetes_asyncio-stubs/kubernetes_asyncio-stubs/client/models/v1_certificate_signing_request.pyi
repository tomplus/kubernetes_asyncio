import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CertificateSigningRequest:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1CertificateSigningRequestSpec
    status: typing.Optional[kubernetes_asyncio.client.V1CertificateSigningRequestStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: kubernetes_asyncio.client.V1CertificateSigningRequestSpec, status: typing.Optional[kubernetes_asyncio.client.V1CertificateSigningRequestStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1CertificateSigningRequestDict:
        ...
class V1CertificateSigningRequestDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1CertificateSigningRequestSpecDict
    status: typing.Optional[kubernetes_asyncio.client.V1CertificateSigningRequestStatusDict]
