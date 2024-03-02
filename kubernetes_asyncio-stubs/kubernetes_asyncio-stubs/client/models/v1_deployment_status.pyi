import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeploymentStatus:
    available_replicas: typing.Optional[int]
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1DeploymentCondition]]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: typing.Optional[int]
    unavailable_replicas: typing.Optional[int]
    updated_replicas: typing.Optional[int]
    
    def __init__(self, *, available_replicas: typing.Optional[int] = ..., collision_count: typing.Optional[int] = ..., conditions: typing.Optional[list[kubernetes_asyncio.client.V1DeploymentCondition]] = ..., observed_generation: typing.Optional[int] = ..., ready_replicas: typing.Optional[int] = ..., replicas: typing.Optional[int] = ..., unavailable_replicas: typing.Optional[int] = ..., updated_replicas: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1DeploymentStatusDict:
        ...
class V1DeploymentStatusDict(typing.TypedDict, total=False):
    availableReplicas: typing.Optional[int]
    collisionCount: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1DeploymentConditionDict]]
    observedGeneration: typing.Optional[int]
    readyReplicas: typing.Optional[int]
    replicas: typing.Optional[int]
    unavailableReplicas: typing.Optional[int]
    updatedReplicas: typing.Optional[int]
