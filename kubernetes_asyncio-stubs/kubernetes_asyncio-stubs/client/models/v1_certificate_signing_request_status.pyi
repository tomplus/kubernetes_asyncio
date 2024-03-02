import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CertificateSigningRequestStatus:
    certificate: typing.Optional[str]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1CertificateSigningRequestCondition]]
    
    def __init__(self, *, certificate: typing.Optional[str] = ..., conditions: typing.Optional[list[kubernetes_asyncio.client.V1CertificateSigningRequestCondition]] = ...) -> None:
        ...
    def to_dict(self) -> V1CertificateSigningRequestStatusDict:
        ...
class V1CertificateSigningRequestStatusDict(typing.TypedDict, total=False):
    certificate: typing.Optional[str]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1CertificateSigningRequestConditionDict]]
