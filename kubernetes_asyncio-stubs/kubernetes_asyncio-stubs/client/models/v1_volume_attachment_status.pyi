import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VolumeAttachmentStatus:
    attach_error: typing.Optional[kubernetes_asyncio.client.V1VolumeError]
    attached: bool
    attachment_metadata: typing.Optional[dict[str, str]]
    detach_error: typing.Optional[kubernetes_asyncio.client.V1VolumeError]
    
    def __init__(self, *, attach_error: typing.Optional[kubernetes_asyncio.client.V1VolumeError] = ..., attached: bool, attachment_metadata: typing.Optional[dict[str, str]] = ..., detach_error: typing.Optional[kubernetes_asyncio.client.V1VolumeError] = ...) -> None:
        ...
    def to_dict(self) -> V1VolumeAttachmentStatusDict:
        ...
class V1VolumeAttachmentStatusDict(typing.TypedDict, total=False):
    attachError: typing.Optional[kubernetes_asyncio.client.V1VolumeErrorDict]
    attached: bool
    attachmentMetadata: typing.Optional[dict[str, str]]
    detachError: typing.Optional[kubernetes_asyncio.client.V1VolumeErrorDict]
