import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1AllowedFlexVolume:
    driver: str
    
    def __init__(self, *, driver: str) -> None:
        ...
    def to_dict(self) -> V1beta1AllowedFlexVolumeDict:
        ...
class V1beta1AllowedFlexVolumeDict(typing.TypedDict, total=False):
    driver: str
