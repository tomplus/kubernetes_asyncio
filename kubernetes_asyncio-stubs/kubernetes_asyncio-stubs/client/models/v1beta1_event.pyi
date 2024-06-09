import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1Event:
    action: typing.Optional[str]
    api_version: typing.Optional[str]
    deprecated_count: typing.Optional[int]
    deprecated_first_timestamp: typing.Optional[datetime.datetime]
    deprecated_last_timestamp: typing.Optional[datetime.datetime]
    deprecated_source: typing.Optional[kubernetes_asyncio.client.V1EventSource]
    event_time: datetime.datetime
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    note: typing.Optional[str]
    reason: typing.Optional[str]
    regarding: typing.Optional[kubernetes_asyncio.client.V1ObjectReference]
    related: typing.Optional[kubernetes_asyncio.client.V1ObjectReference]
    reporting_controller: typing.Optional[str]
    reporting_instance: typing.Optional[str]
    series: typing.Optional[kubernetes_asyncio.client.V1beta1EventSeries]
    type: typing.Optional[str]
    
    def __init__(self, *, action: typing.Optional[str] = ..., api_version: typing.Optional[str] = ..., deprecated_count: typing.Optional[int] = ..., deprecated_first_timestamp: typing.Optional[datetime.datetime] = ..., deprecated_last_timestamp: typing.Optional[datetime.datetime] = ..., deprecated_source: typing.Optional[kubernetes_asyncio.client.V1EventSource] = ..., event_time: datetime.datetime, kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., note: typing.Optional[str] = ..., reason: typing.Optional[str] = ..., regarding: typing.Optional[kubernetes_asyncio.client.V1ObjectReference] = ..., related: typing.Optional[kubernetes_asyncio.client.V1ObjectReference] = ..., reporting_controller: typing.Optional[str] = ..., reporting_instance: typing.Optional[str] = ..., series: typing.Optional[kubernetes_asyncio.client.V1beta1EventSeries] = ..., type: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1EventDict:
        ...
class V1beta1EventDict(typing.TypedDict, total=False):
    action: typing.Optional[str]
    apiVersion: typing.Optional[str]
    deprecatedCount: typing.Optional[int]
    deprecatedFirstTimestamp: typing.Optional[datetime.datetime]
    deprecatedLastTimestamp: typing.Optional[datetime.datetime]
    deprecatedSource: typing.Optional[kubernetes_asyncio.client.V1EventSourceDict]
    eventTime: datetime.datetime
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    note: typing.Optional[str]
    reason: typing.Optional[str]
    regarding: typing.Optional[kubernetes_asyncio.client.V1ObjectReferenceDict]
    related: typing.Optional[kubernetes_asyncio.client.V1ObjectReferenceDict]
    reportingController: typing.Optional[str]
    reportingInstance: typing.Optional[str]
    series: typing.Optional[kubernetes_asyncio.client.V1beta1EventSeriesDict]
    type: typing.Optional[str]
