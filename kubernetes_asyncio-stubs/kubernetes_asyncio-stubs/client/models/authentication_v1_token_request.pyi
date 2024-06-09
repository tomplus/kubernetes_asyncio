import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class AuthenticationV1TokenRequest:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1TokenRequestSpec
    status: typing.Optional[kubernetes_asyncio.client.V1TokenRequestStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: kubernetes_asyncio.client.V1TokenRequestSpec, status: typing.Optional[kubernetes_asyncio.client.V1TokenRequestStatus] = ...) -> None:
        ...
    def to_dict(self) -> AuthenticationV1TokenRequestDict:
        ...
class AuthenticationV1TokenRequestDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1TokenRequestSpecDict
    status: typing.Optional[kubernetes_asyncio.client.V1TokenRequestStatusDict]
