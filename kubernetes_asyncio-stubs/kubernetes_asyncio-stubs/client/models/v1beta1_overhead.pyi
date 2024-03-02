import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1Overhead:
    pod_fixed: typing.Optional[dict[str, str]]
    
    def __init__(self, *, pod_fixed: typing.Optional[dict[str, str]] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1OverheadDict:
        ...
class V1beta1OverheadDict(typing.TypedDict, total=False):
    podFixed: typing.Optional[dict[str, str]]
