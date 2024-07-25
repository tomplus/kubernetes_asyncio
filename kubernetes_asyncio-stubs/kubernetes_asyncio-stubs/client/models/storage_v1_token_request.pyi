import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class StorageV1TokenRequest:
    audience: str
    expiration_seconds: typing.Optional[int]
    
    def __init__(self, *, audience: str, expiration_seconds: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> StorageV1TokenRequestDict:
        ...
class StorageV1TokenRequestDict(typing.TypedDict, total=False):
    audience: str
    expirationSeconds: typing.Optional[int]
