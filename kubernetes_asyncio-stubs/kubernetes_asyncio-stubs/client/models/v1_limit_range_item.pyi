import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LimitRangeItem:
    default: typing.Optional[dict[str, str]]
    default_request: typing.Optional[dict[str, str]]
    max: typing.Optional[dict[str, str]]
    max_limit_request_ratio: typing.Optional[dict[str, str]]
    min: typing.Optional[dict[str, str]]
    type: str
    
    def __init__(self, *, default: typing.Optional[dict[str, str]] = ..., default_request: typing.Optional[dict[str, str]] = ..., max: typing.Optional[dict[str, str]] = ..., max_limit_request_ratio: typing.Optional[dict[str, str]] = ..., min: typing.Optional[dict[str, str]] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V1LimitRangeItemDict:
        ...
class V1LimitRangeItemDict(typing.TypedDict, total=False):
    default: typing.Optional[dict[str, str]]
    defaultRequest: typing.Optional[dict[str, str]]
    max: typing.Optional[dict[str, str]]
    maxLimitRequestRatio: typing.Optional[dict[str, str]]
    min: typing.Optional[dict[str, str]]
    type: str
