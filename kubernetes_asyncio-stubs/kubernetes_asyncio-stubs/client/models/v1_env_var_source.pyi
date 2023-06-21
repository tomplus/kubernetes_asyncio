import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EnvVarSource:
    config_map_key_ref: typing.Optional[kubernetes_asyncio.client.V1ConfigMapKeySelector]
    field_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectFieldSelector]
    resource_field_ref: typing.Optional[kubernetes_asyncio.client.V1ResourceFieldSelector]
    secret_key_ref: typing.Optional[kubernetes_asyncio.client.V1SecretKeySelector]
    
    def __init__(self, *, config_map_key_ref: typing.Optional[kubernetes_asyncio.client.V1ConfigMapKeySelector] = ..., field_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectFieldSelector] = ..., resource_field_ref: typing.Optional[kubernetes_asyncio.client.V1ResourceFieldSelector] = ..., secret_key_ref: typing.Optional[kubernetes_asyncio.client.V1SecretKeySelector] = ...) -> None:
        ...
    def to_dict(self) -> V1EnvVarSourceDict:
        ...
class V1EnvVarSourceDict(typing.TypedDict, total=False):
    configMapKeyRef: typing.Optional[kubernetes_asyncio.client.V1ConfigMapKeySelectorDict]
    fieldRef: typing.Optional[kubernetes_asyncio.client.V1ObjectFieldSelectorDict]
    resourceFieldRef: typing.Optional[kubernetes_asyncio.client.V1ResourceFieldSelectorDict]
    secretKeyRef: typing.Optional[kubernetes_asyncio.client.V1SecretKeySelectorDict]
