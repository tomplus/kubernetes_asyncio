import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1StatefulSetStatus:
    available_replicas: typing.Optional[int]
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1StatefulSetCondition]]
    current_replicas: typing.Optional[int]
    current_revision: typing.Optional[str]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    update_revision: typing.Optional[str]
    updated_replicas: typing.Optional[int]
    
    def __init__(self, *, available_replicas: typing.Optional[int] = ..., collision_count: typing.Optional[int] = ..., conditions: typing.Optional[list[kubernetes_asyncio.client.V1StatefulSetCondition]] = ..., current_replicas: typing.Optional[int] = ..., current_revision: typing.Optional[str] = ..., observed_generation: typing.Optional[int] = ..., ready_replicas: typing.Optional[int] = ..., replicas: int, update_revision: typing.Optional[str] = ..., updated_replicas: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1StatefulSetStatusDict:
        ...
class V1StatefulSetStatusDict(typing.TypedDict, total=False):
    availableReplicas: typing.Optional[int]
    collisionCount: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1StatefulSetConditionDict]]
    currentReplicas: typing.Optional[int]
    currentRevision: typing.Optional[str]
    observedGeneration: typing.Optional[int]
    readyReplicas: typing.Optional[int]
    replicas: int
    updateRevision: typing.Optional[str]
    updatedReplicas: typing.Optional[int]
