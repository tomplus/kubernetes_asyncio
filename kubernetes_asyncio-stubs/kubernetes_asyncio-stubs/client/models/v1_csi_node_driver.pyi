import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CSINodeDriver:
    allocatable: typing.Optional[kubernetes_asyncio.client.V1VolumeNodeResources]
    name: str
    node_id: str
    topology_keys: typing.Optional[list[str]]
    
    def __init__(self, *, allocatable: typing.Optional[kubernetes_asyncio.client.V1VolumeNodeResources] = ..., name: str, node_id: str, topology_keys: typing.Optional[list[str]] = ...) -> None:
        ...
    def to_dict(self) -> V1CSINodeDriverDict:
        ...
class V1CSINodeDriverDict(typing.TypedDict, total=False):
    allocatable: typing.Optional[kubernetes_asyncio.client.V1VolumeNodeResourcesDict]
    name: str
    nodeID: str
    topologyKeys: typing.Optional[list[str]]
