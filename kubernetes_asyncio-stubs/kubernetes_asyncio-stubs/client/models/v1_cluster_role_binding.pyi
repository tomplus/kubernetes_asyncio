import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ClusterRoleBinding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    role_ref: kubernetes_asyncio.client.V1RoleRef
    subjects: typing.Optional[list[kubernetes_asyncio.client.V1Subject]]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ..., role_ref: kubernetes_asyncio.client.V1RoleRef, subjects: typing.Optional[list[kubernetes_asyncio.client.V1Subject]] = ...) -> None:
        ...
    def to_dict(self) -> V1ClusterRoleBindingDict:
        ...
class V1ClusterRoleBindingDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    roleRef: kubernetes_asyncio.client.V1RoleRefDict
    subjects: typing.Optional[list[kubernetes_asyncio.client.V1SubjectDict]]
