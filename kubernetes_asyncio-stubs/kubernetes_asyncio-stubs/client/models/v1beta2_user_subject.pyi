import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2UserSubject:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1beta2UserSubjectDict:
        ...
class V1beta2UserSubjectDict(typing.TypedDict, total=False):
    name: str
