import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CertificateSigningRequestSpec:
    expiration_seconds: typing.Optional[int]
    extra: typing.Optional[dict[str, list[str]]]
    groups: typing.Optional[list[str]]
    request: str
    signer_name: str
    uid: typing.Optional[str]
    usages: typing.Optional[list[str]]
    username: typing.Optional[str]
    
    def __init__(self, *, expiration_seconds: typing.Optional[int] = ..., extra: typing.Optional[dict[str, list[str]]] = ..., groups: typing.Optional[list[str]] = ..., request: str, signer_name: str, uid: typing.Optional[str] = ..., usages: typing.Optional[list[str]] = ..., username: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1CertificateSigningRequestSpecDict:
        ...
class V1CertificateSigningRequestSpecDict(typing.TypedDict, total=False):
    expirationSeconds: typing.Optional[int]
    extra: typing.Optional[dict[str, list[str]]]
    groups: typing.Optional[list[str]]
    request: str
    signerName: str
    uid: typing.Optional[str]
    usages: typing.Optional[list[str]]
    username: typing.Optional[str]
