import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CustomResourceDefinitionVersion:
    additional_printer_columns: typing.Optional[list[kubernetes_asyncio.client.V1CustomResourceColumnDefinition]]
    deprecated: typing.Optional[bool]
    deprecation_warning: typing.Optional[str]
    name: str
    schema: typing.Optional[kubernetes_asyncio.client.V1CustomResourceValidation]
    served: bool
    storage: bool
    subresources: typing.Optional[kubernetes_asyncio.client.V1CustomResourceSubresources]
    
    def __init__(self, *, additional_printer_columns: typing.Optional[list[kubernetes_asyncio.client.V1CustomResourceColumnDefinition]] = ..., deprecated: typing.Optional[bool] = ..., deprecation_warning: typing.Optional[str] = ..., name: str, schema: typing.Optional[kubernetes_asyncio.client.V1CustomResourceValidation] = ..., served: bool, storage: bool, subresources: typing.Optional[kubernetes_asyncio.client.V1CustomResourceSubresources] = ...) -> None:
        ...
    def to_dict(self) -> V1CustomResourceDefinitionVersionDict:
        ...
class V1CustomResourceDefinitionVersionDict(typing.TypedDict, total=False):
    additionalPrinterColumns: typing.Optional[list[kubernetes_asyncio.client.V1CustomResourceColumnDefinitionDict]]
    deprecated: typing.Optional[bool]
    deprecationWarning: typing.Optional[str]
    name: str
    schema: typing.Optional[kubernetes_asyncio.client.V1CustomResourceValidationDict]
    served: bool
    storage: bool
    subresources: typing.Optional[kubernetes_asyncio.client.V1CustomResourceSubresourcesDict]
