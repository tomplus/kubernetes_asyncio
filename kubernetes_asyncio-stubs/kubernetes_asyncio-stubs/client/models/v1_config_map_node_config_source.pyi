import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ConfigMapNodeConfigSource:
    kubelet_config_key: str
    name: str
    namespace: str
    resource_version: typing.Optional[str]
    uid: typing.Optional[str]
    
    def __init__(self, *, kubelet_config_key: str, name: str, namespace: str, resource_version: typing.Optional[str] = ..., uid: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1ConfigMapNodeConfigSourceDict:
        ...
class V1ConfigMapNodeConfigSourceDict(typing.TypedDict, total=False):
    kubeletConfigKey: str
    name: str
    namespace: str
    resourceVersion: typing.Optional[str]
    uid: typing.Optional[str]
