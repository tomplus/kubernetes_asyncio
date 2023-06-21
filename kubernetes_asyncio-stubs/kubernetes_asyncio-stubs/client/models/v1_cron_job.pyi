import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CronJob:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1CronJobSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1CronJobStatus]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., spec: typing.Optional[kubernetes_asyncio.client.V1CronJobSpec] = ..., status: typing.Optional[kubernetes_asyncio.client.V1CronJobStatus] = ...) -> None:
        ...
    def to_dict(self) -> V1CronJobDict:
        ...
class V1CronJobDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1CronJobSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1CronJobStatusDict]
