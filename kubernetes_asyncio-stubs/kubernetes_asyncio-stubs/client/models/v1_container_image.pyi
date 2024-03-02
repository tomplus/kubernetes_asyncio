import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ContainerImage:
    names: typing.Optional[list[str]]
    size_bytes: typing.Optional[int]
    
    def __init__(self, *, names: typing.Optional[list[str]] = ..., size_bytes: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1ContainerImageDict:
        ...
class V1ContainerImageDict(typing.TypedDict, total=False):
    names: typing.Optional[list[str]]
    sizeBytes: typing.Optional[int]
