import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ListMeta:
    _continue: typing.Optional[str]
    remaining_item_count: typing.Optional[int]
    resource_version: typing.Optional[str]
    self_link: typing.Optional[str]
    
    def __init__(self, *, _continue: typing.Optional[str] = ..., remaining_item_count: typing.Optional[int] = ..., resource_version: typing.Optional[str] = ..., self_link: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1ListMetaDict:
        ...
class V1ListMetaDict(typing.TypedDict, total=False):
    _continue: typing.Optional[str]
    remainingItemCount: typing.Optional[int]
    resourceVersion: typing.Optional[str]
    selfLink: typing.Optional[str]
