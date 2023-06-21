import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ValidatingWebhook:
    admission_review_versions: list[str]
    client_config: kubernetes_asyncio.client.AdmissionregistrationV1WebhookClientConfig
    failure_policy: typing.Optional[str]
    match_policy: typing.Optional[str]
    name: str
    namespace_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    rules: typing.Optional[list[kubernetes_asyncio.client.V1RuleWithOperations]]
    side_effects: str
    timeout_seconds: typing.Optional[int]
    
    def __init__(self, *, admission_review_versions: list[str], client_config: kubernetes_asyncio.client.AdmissionregistrationV1WebhookClientConfig, failure_policy: typing.Optional[str] = ..., match_policy: typing.Optional[str] = ..., name: str, namespace_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., object_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ..., rules: typing.Optional[list[kubernetes_asyncio.client.V1RuleWithOperations]] = ..., side_effects: str, timeout_seconds: typing.Optional[int] = ...) -> None:
        ...
    def to_dict(self) -> V1ValidatingWebhookDict:
        ...
class V1ValidatingWebhookDict(typing.TypedDict, total=False):
    admissionReviewVersions: list[str]
    clientConfig: kubernetes_asyncio.client.AdmissionregistrationV1WebhookClientConfigDict
    failurePolicy: typing.Optional[str]
    matchPolicy: typing.Optional[str]
    name: str
    namespaceSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    objectSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    rules: typing.Optional[list[kubernetes_asyncio.client.V1RuleWithOperationsDict]]
    sideEffects: str
    timeoutSeconds: typing.Optional[int]
