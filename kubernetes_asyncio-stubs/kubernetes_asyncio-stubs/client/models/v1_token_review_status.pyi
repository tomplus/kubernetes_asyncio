import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1TokenReviewStatus:
    audiences: typing.Optional[list[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[kubernetes_asyncio.client.V1UserInfo]
    
    def __init__(self, *, audiences: typing.Optional[list[str]] = ..., authenticated: typing.Optional[bool] = ..., error: typing.Optional[str] = ..., user: typing.Optional[kubernetes_asyncio.client.V1UserInfo] = ...) -> None:
        ...
    def to_dict(self) -> V1TokenReviewStatusDict:
        ...
class V1TokenReviewStatusDict(typing.TypedDict, total=False):
    audiences: typing.Optional[list[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[kubernetes_asyncio.client.V1UserInfoDict]
