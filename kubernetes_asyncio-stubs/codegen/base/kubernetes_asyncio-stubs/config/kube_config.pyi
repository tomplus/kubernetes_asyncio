from os import PathLike
from typing import Any, Optional, TypedDict, Union

from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.client.configuration import Configuration

KUBE_CONFIG_DEFAULT_LOCATION: str = ...
StrPath = Union[str, PathLike[str]]
class Context(TypedDict):
    name: str
    context: dict[str, Any]

def list_kube_config_contexts(
    config_file: Optional[StrPath] = ...,
) -> tuple[list[Context], Context]: ...
async def load_kube_config(
    config_file: Optional[StrPath] = ...,
    context: Optional[str] = ...,
    client_configuration: Optional[Configuration] = ...,
    persist_config: bool = ...,
) -> None: ...
async def load_kube_config_from_dict(
    config_dict: dict[Any, Any] = ...,
    context: Optional[str] = ...,
    client_configuration: Optional[Configuration] = ...,
    persist_config: bool = ...,
    temp_file_path: Optional[StrPath] = ...,
) -> None: ...
async def new_client_from_config(
    config_file: Optional[StrPath] = ...,
    context: Optional[str] = ...,
    persist_config: bool = ...,
) -> ApiClient: ...
