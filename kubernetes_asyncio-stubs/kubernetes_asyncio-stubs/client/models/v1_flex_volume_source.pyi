import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1FlexVolumeSource:
    driver: str
    fs_type: typing.Optional[str]
    options: typing.Optional[dict[str, str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference]
    
    def __init__(self, *, driver: str, fs_type: typing.Optional[str] = ..., options: typing.Optional[dict[str, str]] = ..., read_only: typing.Optional[bool] = ..., secret_ref: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReference] = ...) -> None:
        ...
    def to_dict(self) -> V1FlexVolumeSourceDict:
        ...
class V1FlexVolumeSourceDict(typing.TypedDict, total=False):
    driver: str
    fsType: typing.Optional[str]
    options: typing.Optional[dict[str, str]]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[kubernetes_asyncio.client.V1LocalObjectReferenceDict]
