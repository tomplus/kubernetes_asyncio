import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeSystemInfo:
    architecture: str
    boot_id: str
    container_runtime_version: str
    kernel_version: str
    kube_proxy_version: str
    kubelet_version: str
    machine_id: str
    operating_system: str
    os_image: str
    system_uuid: str
    
    def __init__(self, *, architecture: str, boot_id: str, container_runtime_version: str, kernel_version: str, kube_proxy_version: str, kubelet_version: str, machine_id: str, operating_system: str, os_image: str, system_uuid: str) -> None:
        ...
    def to_dict(self) -> V1NodeSystemInfoDict:
        ...
class V1NodeSystemInfoDict(typing.TypedDict, total=False):
    architecture: str
    bootID: str
    containerRuntimeVersion: str
    kernelVersion: str
    kubeProxyVersion: str
    kubeletVersion: str
    machineID: str
    operatingSystem: str
    osImage: str
    systemUUID: str
