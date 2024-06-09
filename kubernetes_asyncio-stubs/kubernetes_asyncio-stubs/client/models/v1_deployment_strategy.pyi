import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeploymentStrategy:
    rolling_update: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateDeployment]
    type: typing.Optional[str]
    
    def __init__(self, *, rolling_update: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateDeployment] = ..., type: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1DeploymentStrategyDict:
        ...
class V1DeploymentStrategyDict(typing.TypedDict, total=False):
    rollingUpdate: typing.Optional[kubernetes_asyncio.client.V1RollingUpdateDeploymentDict]
    type: typing.Optional[str]
