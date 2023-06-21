import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ServerStorageVersion:
    api_server_id: typing.Optional[str]
    decodable_versions: typing.Optional[list[str]]
    encoding_version: typing.Optional[str]
    
    def __init__(self, *, api_server_id: typing.Optional[str] = ..., decodable_versions: typing.Optional[list[str]] = ..., encoding_version: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1alpha1ServerStorageVersionDict:
        ...
class V1alpha1ServerStorageVersionDict(typing.TypedDict, total=False):
    apiServerID: typing.Optional[str]
    decodableVersions: typing.Optional[list[str]]
    encodingVersion: typing.Optional[str]
