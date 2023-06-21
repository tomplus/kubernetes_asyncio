import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Lifecycle:
    post_start: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler]
    pre_stop: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler]
    
    def __init__(self, *, post_start: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler] = ..., pre_stop: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler] = ...) -> None:
        ...
    def to_dict(self) -> V1LifecycleDict:
        ...
class V1LifecycleDict(typing.TypedDict, total=False):
    postStart: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandlerDict]
    preStop: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandlerDict]
