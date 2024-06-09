import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1GlusterfsPersistentVolumeSource:
    endpoints: str
    endpoints_namespace: typing.Optional[str]
    path: str
    read_only: typing.Optional[bool]
    
    def __init__(self, *, endpoints: str, endpoints_namespace: typing.Optional[str] = ..., path: str, read_only: typing.Optional[bool] = ...) -> None:
        ...
    def to_dict(self) -> V1GlusterfsPersistentVolumeSourceDict:
        ...
class V1GlusterfsPersistentVolumeSourceDict(typing.TypedDict, total=False):
    endpoints: str
    endpointsNamespace: typing.Optional[str]
    path: str
    readOnly: typing.Optional[bool]
