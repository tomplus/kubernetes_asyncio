from os import PathLike
from typing import Sequence, Any, Union

from typing_extensions import Unpack, TypedDict, Literal

from kubernetes_asyncio.client.api_client import ApiClient

StrPath = Union[str, PathLike[str]]
class Params(TypedDict, total=False):
    async_req: bool
    include_uninitialized: bool
    pretty: Literal["true", "false"]
    dry_run: str

async def create_from_yaml(
        k8s_client: ApiClient,
        yaml_file : StrPath,
        verbose: bool=...,
        namespace: str = ...,
        **kwargs: Unpack[Params]) -> Sequence[Any]: ...

async def create_from_dict(
        k8s_client: ApiClient,
        data: dict[str, Any],
        verbose: bool=...,
        namespace: str= ...,
        **kwargs: Unpack[Params]) -> Sequence[Any]: ...
async def create_from_yaml_single_item(
        k8s_client : ApiClient,
        yml_object: dict[str, Any],
        verbose: bool= ...,
        namespace: str= ...,
        **kwargs: Unpack[Params]) -> Any: ...