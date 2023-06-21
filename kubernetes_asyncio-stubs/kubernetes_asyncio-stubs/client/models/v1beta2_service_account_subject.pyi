import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2ServiceAccountSubject:
    name: str
    namespace: str
    
    def __init__(self, *, name: str, namespace: str) -> None:
        ...
    def to_dict(self) -> V1beta2ServiceAccountSubjectDict:
        ...
class V1beta2ServiceAccountSubjectDict(typing.TypedDict, total=False):
    name: str
    namespace: str
