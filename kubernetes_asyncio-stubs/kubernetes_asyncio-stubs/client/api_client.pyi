from typing import Any, Optional, Protocol, Type, TypeVar

from kubernetes_asyncio.client.configuration import Configuration

_T = TypeVar("_T")

class Response(Protocol):
    data: str

class ApiClient:
    def __init__(self, configuration: Optional[Configuration] = ...) -> None: ...
    def sanitize_for_serialization(self, obj: Any) -> dict[Any, Any]: ...
    def deserialize(self, response: Response, response_type: Type[_T]) -> _T: ...
