import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1QueuingConfiguration:
    hand_size: typing.Optional[int]
    queue_length_limit: typing.Optional[int]
    queues: typing.Optional[int]
    
    def __init__(self, *, hand_size: typing.Optional[int] = ..., queue_length_limit: typing.Optional[int] = ..., queues: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1QueuingConfigurationDict:
        ...
class V1beta1QueuingConfigurationDict(typing.TypedDict, total=False):
    handSize: typing.Optional[int]
    queueLengthLimit: typing.Optional[int]
    queues: typing.Optional[int]
