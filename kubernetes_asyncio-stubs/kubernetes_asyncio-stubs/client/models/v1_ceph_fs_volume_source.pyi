import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CephFSVolumeSource:
    monitors: list[str]
    path: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_file: typing.Optional[str]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference]
    user: typing.Optional[str]
    
    def __init__(self, *, monitors: list[str], path: typing.Optional[str] = ..., read_only: typing.Optional[bool] = ..., secret_file: typing.Optional[str] = ..., secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference] = ..., user: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1CephFSVolumeSourceDict:
        ...
class V1CephFSVolumeSourceDict(typing.TypedDict, total=False):
    monitors: list[str]
    path: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretFile: typing.Optional[str]
    secretRef: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReferenceDict]
    user: typing.Optional[str]
