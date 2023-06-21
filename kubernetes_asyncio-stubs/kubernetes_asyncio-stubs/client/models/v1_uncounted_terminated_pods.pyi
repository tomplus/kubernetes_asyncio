import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1UncountedTerminatedPods:
    failed: typing.Optional[list[str]]
    succeeded: typing.Optional[list[str]]
    
    def __init__(self, *, failed: typing.Optional[list[str]] = ..., succeeded: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1UncountedTerminatedPodsDict:
        ...
class V1UncountedTerminatedPodsDict(typing.TypedDict, total=False):
    failed: typing.Optional[list[str]]
    succeeded: typing.Optional[list[str]]
