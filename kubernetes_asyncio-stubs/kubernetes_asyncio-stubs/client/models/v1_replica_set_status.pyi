import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ReplicaSetStatus:
    available_replicas: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ReplicaSetCondition]]
    fully_labeled_replicas: typing.Optional[int]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    
    def __init__(self, *, available_replicas: typing.Optional[int] = ..., conditions: typing.Optional[list[kubernetes_asyncio.client.V1ReplicaSetCondition]] = ..., fully_labeled_replicas: typing.Optional[int] = ..., observed_generation: typing.Optional[int] = ..., ready_replicas: typing.Optional[int] = ..., replicas: int) -> None:
        ...
    def to_dict(self) -> V1ReplicaSetStatusDict:
        ...
class V1ReplicaSetStatusDict(typing.TypedDict, total=False):
    availableReplicas: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ReplicaSetConditionDict]]
    fullyLabeledReplicas: typing.Optional[int]
    observedGeneration: typing.Optional[int]
    readyReplicas: typing.Optional[int]
    replicas: int
