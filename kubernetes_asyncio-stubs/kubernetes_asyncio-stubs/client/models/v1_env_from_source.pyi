import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EnvFromSource:
    config_map_ref: typing.Optional[kubernetes_asyncio.client.V1ConfigMapEnvSource]
    prefix: typing.Optional[str]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretEnvSource]
    
    def __init__(self, *, config_map_ref: typing.Optional[kubernetes_asyncio.client.V1ConfigMapEnvSource] = ..., prefix: typing.Optional[str] = ..., secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretEnvSource] = ...) -> None:
        ...
    def to_dict(self) -> V1EnvFromSourceDict:
        ...
class V1EnvFromSourceDict(typing.TypedDict, total=False):
    configMapRef: typing.Optional[kubernetes_asyncio.client.V1ConfigMapEnvSourceDict]
    prefix: typing.Optional[str]
    secretRef: typing.Optional[kubernetes_asyncio.client.V1SecretEnvSourceDict]
