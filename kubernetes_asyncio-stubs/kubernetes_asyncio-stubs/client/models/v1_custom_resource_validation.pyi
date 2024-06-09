import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceValidation:
    open_apiv3_schema: typing.Optional[kubernetes_asyncio.client.V1JSONSchemaProps]
    
    def __init__(self, *, open_apiv3_schema: typing.Optional[kubernetes_asyncio.client.V1JSONSchemaProps] = ...) -> None:
        ...
    def to_dict(self) -> V1CustomResourceValidationDict:
        ...
class V1CustomResourceValidationDict(typing.TypedDict, total=False):
    openAPIV3Schema: typing.Optional[kubernetes_asyncio.client.V1JSONSchemaPropsDict]
