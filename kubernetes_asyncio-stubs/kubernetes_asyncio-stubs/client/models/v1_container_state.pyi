import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ContainerState:
    running: typing.Optional[kubernetes_asyncio.client.V1ContainerStateRunning]
    terminated: typing.Optional[kubernetes_asyncio.client.V1ContainerStateTerminated]
    waiting: typing.Optional[kubernetes_asyncio.client.V1ContainerStateWaiting]
    
    def __init__(self, *, running: typing.Optional[kubernetes_asyncio.client.V1ContainerStateRunning] = ..., terminated: typing.Optional[kubernetes_asyncio.client.V1ContainerStateTerminated] = ..., waiting: typing.Optional[kubernetes_asyncio.client.V1ContainerStateWaiting] = ...) -> None:
        ...
    def to_dict(self) -> V1ContainerStateDict:
        ...
class V1ContainerStateDict(typing.TypedDict, total=False):
    running: typing.Optional[kubernetes_asyncio.client.V1ContainerStateRunningDict]
    terminated: typing.Optional[kubernetes_asyncio.client.V1ContainerStateTerminatedDict]
    waiting: typing.Optional[kubernetes_asyncio.client.V1ContainerStateWaitingDict]
