import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1TokenReviewSpec:
    audiences: typing.Optional[list[str]]
    token: typing.Optional[str]
    
    def __init__(self, *, audiences: typing.Optional[list[str]] = ..., token: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1TokenReviewSpecDict:
        ...
class V1TokenReviewSpecDict(typing.TypedDict, total=False):
    audiences: typing.Optional[list[str]]
    token: typing.Optional[str]
