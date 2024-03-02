import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ReplicationControllerStatus:
    available_replicas: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ReplicationControllerCondition]]
    fully_labeled_replicas: typing.Optional[int]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    
    def __init__(self, *, available_replicas: typing.Optional[int] = ..., conditions: typing.Optional[list[kubernetes_asyncio.client.V1ReplicationControllerCondition]] = ..., fully_labeled_replicas: typing.Optional[int] = ..., observed_generation: typing.Optional[int] = ..., ready_replicas: typing.Optional[int] = ..., replicas: int) -> None:
        ...
    def to_dict(self) -> V1ReplicationControllerStatusDict:
        ...
class V1ReplicationControllerStatusDict(typing.TypedDict, total=False):
    availableReplicas: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ReplicationControllerConditionDict]]
    fullyLabeledReplicas: typing.Optional[int]
    observedGeneration: typing.Optional[int]
    readyReplicas: typing.Optional[int]
    replicas: int
