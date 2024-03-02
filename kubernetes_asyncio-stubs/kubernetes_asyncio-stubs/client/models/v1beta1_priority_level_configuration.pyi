import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1PriorityLevelConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1PriorityLevelConfigurationDict:
        ...
class V1beta1PriorityLevelConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1beta1PriorityLevelConfigurationStatusDict]
