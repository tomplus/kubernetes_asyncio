import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RuleWithOperations:
    api_groups: typing.Optional[list[str]]
    api_versions: typing.Optional[list[str]]
    operations: typing.Optional[list[str]]
    resources: typing.Optional[list[str]]
    scope: typing.Optional[str]
    
    def __init__(self, *, api_groups: typing.Optional[list[str]] = ..., api_versions: typing.Optional[list[str]] = ..., operations: typing.Optional[list[str]] = ..., resources: typing.Optional[list[str]] = ..., scope: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1RuleWithOperationsDict:
        ...
class V1RuleWithOperationsDict(typing.TypedDict, total=False):
    apiGroups: typing.Optional[list[str]]
    apiVersions: typing.Optional[list[str]]
    operations: typing.Optional[list[str]]
    resources: typing.Optional[list[str]]
    scope: typing.Optional[str]
