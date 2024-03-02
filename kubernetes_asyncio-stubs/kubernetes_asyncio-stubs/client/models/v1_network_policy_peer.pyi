import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NetworkPolicyPeer:
    ip_block: typing.Optional[kubernetes_asyncio.client.V1IPBlock]
    namespace_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    pod_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    
    def __init__(self, *, ip_block: typing.Optional[kubernetes_asyncio.client.V1IPBlock] = ..., namespace_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., pod_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ...) -> None:
        ...
    def to_dict(self) -> V1NetworkPolicyPeerDict:
        ...
class V1NetworkPolicyPeerDict(typing.TypedDict, total=False):
    ipBlock: typing.Optional[kubernetes_asyncio.client.V1IPBlockDict]
    namespaceSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    podSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
