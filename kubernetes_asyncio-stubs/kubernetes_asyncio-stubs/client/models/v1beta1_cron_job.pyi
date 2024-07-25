import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1CronJob:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta1CronJobSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1beta1CronJobStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1beta1CronJobSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1beta1CronJobStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1CronJobDict:
        ...
class V1beta1CronJobDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta1CronJobSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1beta1CronJobStatusDict]
