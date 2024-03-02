import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2beta2HPAScalingRules:
    policies: typing.Optional[list[kubernetes_asyncio.client.V2beta2HPAScalingPolicy]]
    select_policy: typing.Optional[str]
    stabilization_window_seconds: typing.Optional[int]
    
    def __init__(self, *, policies: typing.Optional[list[kubernetes_asyncio.client.V2beta2HPAScalingPolicy]] = ..., select_policy: typing.Optional[str] = ..., stabilization_window_seconds: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V2beta2HPAScalingRulesDict:
        ...
class V2beta2HPAScalingRulesDict(typing.TypedDict, total=False):
    policies: typing.Optional[list[kubernetes_asyncio.client.V2beta2HPAScalingPolicyDict]]
    selectPolicy: typing.Optional[str]
    stabilizationWindowSeconds: typing.Optional[int]
