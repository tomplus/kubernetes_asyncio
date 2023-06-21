import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SeccompProfile:
    localhost_profile: typing.Optional[str]
    type: str
    
    def __init__(self, *, localhost_profile: typing.Optional[str] = ..., type: str) -> None:
        ...
    def to_dict(self) -> V1SeccompProfileDict:
        ...
class V1SeccompProfileDict(typing.TypedDict, total=False):
    localhostProfile: typing.Optional[str]
    type: str
