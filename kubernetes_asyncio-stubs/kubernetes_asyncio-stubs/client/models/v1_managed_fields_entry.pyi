import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ManagedFieldsEntry:
    api_version: typing.Optional[str]
    fields_type: typing.Optional[str]
    fields_v1: typing.Optional[typing.Any]
    manager: typing.Optional[str]
    operation: typing.Optional[str]
    subresource: typing.Optional[str]
    time: typing.Optional[datetime.datetime]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., fields_type: typing.Optional[str] = ..., fields_v1: typing.Optional[typing.Any] = ..., manager: typing.Optional[str] = ..., operation: typing.Optional[str] = ..., subresource: typing.Optional[str] = ..., time: typing.Optional[datetime.datetime] = ...) -> None:
        ...
    def to_dict(self) -> V1ManagedFieldsEntryDict:
        ...
class V1ManagedFieldsEntryDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    fieldsType: typing.Optional[str]
    fieldsV1: typing.Optional[typing.Any]
    manager: typing.Optional[str]
    operation: typing.Optional[str]
    subresource: typing.Optional[str]
    time: typing.Optional[datetime.datetime]
