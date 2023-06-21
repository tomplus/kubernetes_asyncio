import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1AzureFileVolumeSource:
    read_only: typing.Optional[bool]
    secret_name: str
    share_name: str
    
    def __init__(self, *, read_only: typing.Optional[bool] = ..., secret_name: str, share_name: str) -> None:
        ...
    def to_dict(self) -> V1AzureFileVolumeSourceDict:
        ...
class V1AzureFileVolumeSourceDict(typing.TypedDict, total=False):
    readOnly: typing.Optional[bool]
    secretName: str
    shareName: str
