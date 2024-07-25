import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EndpointConditions:
    ready: typing.Optional[bool]
    serving: typing.Optional[bool]
    terminating: typing.Optional[bool]
    
    def __init__(self, *, ready: typing.Optional[bool] = ..., serving: typing.Optional[bool] = ..., terminating: typing.Optional[bool] = ...) -> None:
        ...
    def to_dict(self) -> V1EndpointConditionsDict:
        ...
class V1EndpointConditionsDict(typing.TypedDict, total=False):
    ready: typing.Optional[bool]
    serving: typing.Optional[bool]
    terminating: typing.Optional[bool]
