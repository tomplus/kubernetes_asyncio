import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RBDVolumeSource:
    fs_type: typing.Optional[str]
    image: str
    keyring: typing.Optional[str]
    monitors: list[str]
    pool: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference]
    user: typing.Optional[str]
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., image: str, keyring: typing.Optional[str] = ..., monitors: list[str], pool: typing.Optional[str] = ..., read_only: typing.Optional[bool] = ..., secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference] = ..., user: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1RBDVolumeSourceDict:
        ...
class V1RBDVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    image: str
    keyring: typing.Optional[str]
    monitors: list[str]
    pool: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReferenceDict]
    user: typing.Optional[str]
