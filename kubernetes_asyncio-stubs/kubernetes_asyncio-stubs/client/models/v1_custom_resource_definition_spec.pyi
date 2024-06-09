import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceDefinitionSpec:
    conversion: typing.Optional[kubernetes_asyncio.client.V1CustomResourceConversion]
    group: str
    names: kubernetes_asyncio.client.V1CustomResourceDefinitionNames
    preserve_unknown_fields: typing.Optional[bool]
    scope: str
    versions: list[kubernetes_asyncio.client.V1CustomResourceDefinitionVersion]
    
    def __init__(self, *, conversion: typing.Optional[kubernetes_asyncio.client.V1CustomResourceConversion] = ..., group: str, names: kubernetes_asyncio.client.V1CustomResourceDefinitionNames, preserve_unknown_fields: typing.Optional[bool] = ..., scope: str, versions: list[kubernetes_asyncio.client.V1CustomResourceDefinitionVersion]) -> None:
        ...
    def to_dict(self) -> V1CustomResourceDefinitionSpecDict:
        ...
class V1CustomResourceDefinitionSpecDict(typing.TypedDict, total=False):
    conversion: typing.Optional[kubernetes_asyncio.client.V1CustomResourceConversionDict]
    group: str
    names: kubernetes_asyncio.client.V1CustomResourceDefinitionNamesDict
    preserveUnknownFields: typing.Optional[bool]
    scope: str
    versions: list[kubernetes_asyncio.client.V1CustomResourceDefinitionVersionDict]
