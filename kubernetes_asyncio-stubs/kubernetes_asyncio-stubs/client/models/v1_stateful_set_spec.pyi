import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1StatefulSetSpec:
    min_ready_seconds: typing.Optional[int]
    persistent_volume_claim_retention_policy: typing.Optional[kubernetes_asyncio.client.V1StatefulSetPersistentVolumeClaimRetentionPolicy]
    pod_management_policy: typing.Optional[str]
    replicas: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: kubernetes_asyncio.client.V1LabelSelector
    service_name: str
    template: kubernetes_asyncio.client.V1PodTemplateSpec
    update_strategy: typing.Optional[kubernetes_asyncio.client.V1StatefulSetUpdateStrategy]
    volume_claim_templates: typing.Optional[list[kubernetes_asyncio.client.V1PersistentVolumeClaim]]
    
    def __init__(self, *, min_ready_seconds: typing.Optional[int] = ..., persistent_volume_claim_retention_policy: typing.Optional[kubernetes_asyncio.client.V1StatefulSetPersistentVolumeClaimRetentionPolicy] = ..., pod_management_policy: typing.Optional[str] = ..., replicas: typing.Optional[int] = ..., revision_history_limit: typing.Optional[int] = ..., selector: kubernetes_asyncio.client.V1LabelSelector, service_name: str, template: kubernetes_asyncio.client.V1PodTemplateSpec, update_strategy: typing.Optional[kubernetes_asyncio.client.V1StatefulSetUpdateStrategy] = ..., volume_claim_templates: typing.Optional[list[kubernetes_asyncio.client.V1PersistentVolumeClaim]] = ...) -> None:
        ...
    def to_dict(self) -> V1StatefulSetSpecDict:
        ...
class V1StatefulSetSpecDict(typing.TypedDict, total=False):
    minReadySeconds: typing.Optional[int]
    persistentVolumeClaimRetentionPolicy: typing.Optional[kubernetes_asyncio.client.V1StatefulSetPersistentVolumeClaimRetentionPolicyDict]
    podManagementPolicy: typing.Optional[str]
    replicas: typing.Optional[int]
    revisionHistoryLimit: typing.Optional[int]
    selector: kubernetes_asyncio.client.V1LabelSelectorDict
    serviceName: str
    template: kubernetes_asyncio.client.V1PodTemplateSpecDict
    updateStrategy: typing.Optional[kubernetes_asyncio.client.V1StatefulSetUpdateStrategyDict]
    volumeClaimTemplates: typing.Optional[list[kubernetes_asyncio.client.V1PersistentVolumeClaimDict]]
