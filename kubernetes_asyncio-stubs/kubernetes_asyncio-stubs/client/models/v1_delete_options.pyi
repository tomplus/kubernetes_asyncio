import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeleteOptions:
    api_version: typing.Optional[str]
    dry_run: typing.Optional[list[str]]
    grace_period_seconds: typing.Optional[int]
    kind: typing.Optional[str]
    orphan_dependents: typing.Optional[bool]
    preconditions: typing.Optional[kubernetes_asyncio.client.V1Preconditions]
    propagation_policy: typing.Optional[str]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., dry_run: typing.Optional[list[str]] = ..., grace_period_seconds: typing.Optional[int] = ..., kind: typing.Optional[str] = ..., orphan_dependents: typing.Optional[bool] = ..., preconditions: typing.Optional[kubernetes_asyncio.client.V1Preconditions] = ..., propagation_policy: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1DeleteOptionsDict:
        ...
class V1DeleteOptionsDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    dryRun: typing.Optional[list[str]]
    gracePeriodSeconds: typing.Optional[int]
    kind: typing.Optional[str]
    orphanDependents: typing.Optional[bool]
    preconditions: typing.Optional[kubernetes_asyncio.client.V1PreconditionsDict]
    propagationPolicy: typing.Optional[str]
