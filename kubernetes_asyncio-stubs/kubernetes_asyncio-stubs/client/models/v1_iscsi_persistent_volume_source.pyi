import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ISCSIPersistentVolumeSource:
    chap_auth_discovery: typing.Optional[bool]
    chap_auth_session: typing.Optional[bool]
    fs_type: typing.Optional[str]
    initiator_name: typing.Optional[str]
    iqn: str
    iscsi_interface: typing.Optional[str]
    lun: int
    portals: typing.Optional[list[str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference]
    target_portal: str
    
    def __init__(self, *, chap_auth_discovery: typing.Optional[bool] = ..., chap_auth_session: typing.Optional[bool] = ..., fs_type: typing.Optional[str] = ..., initiator_name: typing.Optional[str] = ..., iqn: str, iscsi_interface: typing.Optional[str] = ..., lun: int, portals: typing.Optional[list[str]] = ..., read_only: typing.Optional[bool] = ..., secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference] = ..., target_portal: str) -> None:
        ...
    def to_dict(self) -> V1ISCSIPersistentVolumeSourceDict:
        ...
class V1ISCSIPersistentVolumeSourceDict(typing.TypedDict, total=False):
    chapAuthDiscovery: typing.Optional[bool]
    chapAuthSession: typing.Optional[bool]
    fsType: typing.Optional[str]
    initiatorName: typing.Optional[str]
    iqn: str
    iscsiInterface: typing.Optional[str]
    lun: int
    portals: typing.Optional[list[str]]
    readOnly: typing.Optional[bool]
    secretRef: typing.Optional[kubernetes_asyncio.client.V1SecretReferenceDict]
    targetPortal: str
