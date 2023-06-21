import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EphemeralVolumeSource:
    volume_claim_template: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimTemplate]
    
    def __init__(self, *, volume_claim_template: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimTemplate] = ...) -> None:
        ...
    def to_dict(self) -> V1EphemeralVolumeSourceDict:
        ...
class V1EphemeralVolumeSourceDict(typing.TypedDict, total=False):
    volumeClaimTemplate: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimTemplateDict]
