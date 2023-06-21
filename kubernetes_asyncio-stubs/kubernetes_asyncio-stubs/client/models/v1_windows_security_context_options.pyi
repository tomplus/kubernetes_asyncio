import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1WindowsSecurityContextOptions:
    gmsa_credential_spec: typing.Optional[str]
    gmsa_credential_spec_name: typing.Optional[str]
    host_process: typing.Optional[bool]
    run_as_user_name: typing.Optional[str]
    
    def __init__(self, *, gmsa_credential_spec: typing.Optional[str] = ..., gmsa_credential_spec_name: typing.Optional[str] = ..., host_process: typing.Optional[bool] = ..., run_as_user_name: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1WindowsSecurityContextOptionsDict:
        ...
class V1WindowsSecurityContextOptionsDict(typing.TypedDict, total=False):
    gmsaCredentialSpec: typing.Optional[str]
    gmsaCredentialSpecName: typing.Optional[str]
    hostProcess: typing.Optional[bool]
    runAsUserName: typing.Optional[str]
