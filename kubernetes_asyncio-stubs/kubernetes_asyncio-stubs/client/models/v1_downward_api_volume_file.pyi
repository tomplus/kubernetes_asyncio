import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DownwardAPIVolumeFile:
    field_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectFieldSelector]
    mode: typing.Optional[int]
    path: str
    resource_field_ref: typing.Optional[kubernetes_asyncio.client.V1ResourceFieldSelector]
    
    def __init__(self, *, field_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectFieldSelector] = ..., mode: typing.Optional[int] = ..., path: str, resource_field_ref: typing.Optional[kubernetes_asyncio.client.V1ResourceFieldSelector] = ...) -> None:
        ...
    def to_dict(self) -> V1DownwardAPIVolumeFileDict:
        ...
class V1DownwardAPIVolumeFileDict(typing.TypedDict, total=False):
    fieldRef: typing.Optional[kubernetes_asyncio.client.V1ObjectFieldSelectorDict]
    mode: typing.Optional[int]
    path: str
    resourceFieldRef: typing.Optional[kubernetes_asyncio.client.V1ResourceFieldSelectorDict]
