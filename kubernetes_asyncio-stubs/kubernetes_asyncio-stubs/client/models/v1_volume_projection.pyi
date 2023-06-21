import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VolumeProjection:
    config_map: typing.Optional[kubernetes_asyncio.client.V1ConfigMapProjection]
    downward_api: typing.Optional[kubernetes_asyncio.client.V1DownwardAPIProjection]
    secret: typing.Optional[kubernetes_asyncio.client.V1SecretProjection]
    service_account_token: typing.Optional[kubernetes_asyncio.client.V1ServiceAccountTokenProjection]
    
    def __init__(self, *, config_map: typing.Optional[kubernetes_asyncio.client.V1ConfigMapProjection] = ..., downward_api: typing.Optional[kubernetes_asyncio.client.V1DownwardAPIProjection] = ..., secret: typing.Optional[kubernetes_asyncio.client.V1SecretProjection] = ..., service_account_token: typing.Optional[kubernetes_asyncio.client.V1ServiceAccountTokenProjection] = ...) -> None:
        ...
    def to_dict(self) -> V1VolumeProjectionDict:
        ...
class V1VolumeProjectionDict(typing.TypedDict, total=False):
    configMap: typing.Optional[kubernetes_asyncio.client.V1ConfigMapProjectionDict]
    downwardAPI: typing.Optional[kubernetes_asyncio.client.V1DownwardAPIProjectionDict]
    secret: typing.Optional[kubernetes_asyncio.client.V1SecretProjectionDict]
    serviceAccountToken: typing.Optional[kubernetes_asyncio.client.V1ServiceAccountTokenProjectionDict]
