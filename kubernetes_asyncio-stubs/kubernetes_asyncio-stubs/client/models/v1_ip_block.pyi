import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1IPBlock:
    cidr: str
    _except: typing.Optional[list[str]]
    
    def __init__(self, *, cidr: str, _except: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1IPBlockDict:
        ...
class V1IPBlockDict(typing.TypedDict, total=False):
    cidr: str
    _except: typing.Optional[list[str]]
