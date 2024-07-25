from typing import Any, Optional

from kubernetes_asyncio.client.rest import RESTResponse

class OpenApiException(Exception): ...

class ApiTypeError(OpenApiException, TypeError):
    path_to_item: Optional[list[str]]
    valid_classes: Optional[tuple[Any, ...]]
    key_type: Optional[bool]
    def __init__(
        self,
        msg: str,
        path_to_item: Optional[list[str]] = ...,
        valid_classes: Optional[tuple[Any, ...]] = ...,
        key_type: Optional[bool] = ...,
    ) -> None: ...

class ApiValueError(OpenApiException, ValueError):
    path_to_item: Optional[list[Any]]
    def __init__(self, msg: str, path_to_item: Optional[list[Any]] = ...) -> None: ...

class ApiKeyError(OpenApiException, KeyError):
    path_to_item: Optional[list[Any]]
    def __init__(self, msg: str, path_to_item: Optional[list[Any]] = ...) -> None: ...

class ApiException(OpenApiException):
    status: Optional[int]
    reason: Optional[str]
    body: Optional[str]
    headers: dict[str, str]
    def __init__(
        self,
        status: Optional[int] = ...,
        reason: Optional[str] = ...,
        http_resp: Optional[RESTResponse] = ...,
    ) -> None: ...
