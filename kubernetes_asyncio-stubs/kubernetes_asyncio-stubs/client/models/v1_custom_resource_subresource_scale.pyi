import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceSubresourceScale:
    label_selector_path: typing.Optional[str]
    spec_replicas_path: str
    status_replicas_path: str
    
    def __init__(self, *, label_selector_path: typing.Optional[str] = ..., spec_replicas_path: str, status_replicas_path: str) -> None:
        ...
    def to_dict(self) -> V1CustomResourceSubresourceScaleDict:
        ...
class V1CustomResourceSubresourceScaleDict(typing.TypedDict, total=False):
    labelSelectorPath: typing.Optional[str]
    specReplicasPath: str
    statusReplicasPath: str
