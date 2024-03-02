import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1CSIStorageCapacity:
    api_version: typing.Optional[str]
    capacity: typing.Optional[str]
    kind: typing.Optional[str]
    maximum_volume_size: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    node_topology: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    storage_class_name: str
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., capacity: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., maximum_volume_size: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., node_topology: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., storage_class_name: str) -> None:
        ...
    def to_dict(self) -> V1beta1CSIStorageCapacityDict:
        ...
class V1beta1CSIStorageCapacityDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    capacity: typing.Optional[str]
    kind: typing.Optional[str]
    maximumVolumeSize: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    nodeTopology: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    storageClassName: str
