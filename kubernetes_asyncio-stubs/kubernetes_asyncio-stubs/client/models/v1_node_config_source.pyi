import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeConfigSource:
    config_map: typing.Optional[kubernetes_asyncio.client.V1ConfigMapNodeConfigSource]
    
    def __init__(self, *, config_map: typing.Optional[kubernetes_asyncio.client.V1ConfigMapNodeConfigSource] = ...) -> None:
        ...
    def to_dict(self) -> V1NodeConfigSourceDict:
        ...
class V1NodeConfigSourceDict(typing.TypedDict, total=False):
    configMap: typing.Optional[kubernetes_asyncio.client.V1ConfigMapNodeConfigSourceDict]
