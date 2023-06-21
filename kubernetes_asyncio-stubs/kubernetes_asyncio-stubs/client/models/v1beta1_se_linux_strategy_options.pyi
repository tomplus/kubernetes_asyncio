import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1SELinuxStrategyOptions:
    rule: str
    se_linux_options: typing.Optional[kubernetes_asyncio.client.V1SELinuxOptions]
    
    def __init__(self, *, rule: str, se_linux_options: typing.Optional[kubernetes_asyncio.client.V1SELinuxOptions] = ...) -> None:
        ...
    def to_dict(self) -> V1beta1SELinuxStrategyOptionsDict:
        ...
class V1beta1SELinuxStrategyOptionsDict(typing.TypedDict, total=False):
    rule: str
    seLinuxOptions: typing.Optional[kubernetes_asyncio.client.V1SELinuxOptionsDict]
