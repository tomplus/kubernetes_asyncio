import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Volume:
    aws_elastic_block_store: typing.Optional[kubernetes_asyncio.client.V1AWSElasticBlockStoreVolumeSource]
    azure_disk: typing.Optional[kubernetes_asyncio.client.V1AzureDiskVolumeSource]
    azure_file: typing.Optional[kubernetes_asyncio.client.V1AzureFileVolumeSource]
    cephfs: typing.Optional[kubernetes_asyncio.client.V1CephFSVolumeSource]
    cinder: typing.Optional[kubernetes_asyncio.client.V1CinderVolumeSource]
    config_map: typing.Optional[kubernetes_asyncio.client.V1ConfigMapVolumeSource]
    csi: typing.Optional[kubernetes_asyncio.client.V1CSIVolumeSource]
    downward_api: typing.Optional[kubernetes_asyncio.client.V1DownwardAPIVolumeSource]
    empty_dir: typing.Optional[kubernetes_asyncio.client.V1EmptyDirVolumeSource]
    ephemeral: typing.Optional[kubernetes_asyncio.client.V1EphemeralVolumeSource]
    fc: typing.Optional[kubernetes_asyncio.client.V1FCVolumeSource]
    flex_volume: typing.Optional[kubernetes_asyncio.client.V1FlexVolumeSource]
    flocker: typing.Optional[kubernetes_asyncio.client.V1FlockerVolumeSource]
    gce_persistent_disk: typing.Optional[kubernetes_asyncio.client.V1GCEPersistentDiskVolumeSource]
    git_repo: typing.Optional[kubernetes_asyncio.client.V1GitRepoVolumeSource]
    glusterfs: typing.Optional[kubernetes_asyncio.client.V1GlusterfsVolumeSource]
    host_path: typing.Optional[kubernetes_asyncio.client.V1HostPathVolumeSource]
    iscsi: typing.Optional[kubernetes_asyncio.client.V1ISCSIVolumeSource]
    name: str
    nfs: typing.Optional[kubernetes_asyncio.client.V1NFSVolumeSource]
    persistent_volume_claim: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimVolumeSource]
    photon_persistent_disk: typing.Optional[kubernetes_asyncio.client.V1PhotonPersistentDiskVolumeSource]
    portworx_volume: typing.Optional[kubernetes_asyncio.client.V1PortworxVolumeSource]
    projected: typing.Optional[kubernetes_asyncio.client.V1ProjectedVolumeSource]
    quobyte: typing.Optional[kubernetes_asyncio.client.V1QuobyteVolumeSource]
    rbd: typing.Optional[kubernetes_asyncio.client.V1RBDVolumeSource]
    scale_io: typing.Optional[kubernetes_asyncio.client.V1ScaleIOVolumeSource]
    secret: typing.Optional[kubernetes_asyncio.client.V1SecretVolumeSource]
    storageos: typing.Optional[kubernetes_asyncio.client.V1StorageOSVolumeSource]
    vsphere_volume: typing.Optional[kubernetes_asyncio.client.V1VsphereVirtualDiskVolumeSource]
    
    def __init__(self, *, aws_elastic_block_store: typing.Optional[kubernetes_asyncio.client.V1AWSElasticBlockStoreVolumeSource] = ..., azure_disk: typing.Optional[kubernetes_asyncio.client.V1AzureDiskVolumeSource] = ..., azure_file: typing.Optional[kubernetes_asyncio.client.V1AzureFileVolumeSource] = ..., cephfs: typing.Optional[kubernetes_asyncio.client.V1CephFSVolumeSource] = ..., cinder: typing.Optional[kubernetes_asyncio.client.V1CinderVolumeSource] = ..., config_map: typing.Optional[kubernetes_asyncio.client.V1ConfigMapVolumeSource] = ..., csi: typing.Optional[kubernetes_asyncio.client.V1CSIVolumeSource] = ..., downward_api: typing.Optional[kubernetes_asyncio.client.V1DownwardAPIVolumeSource] = ..., empty_dir: typing.Optional[kubernetes_asyncio.client.V1EmptyDirVolumeSource] = ..., ephemeral: typing.Optional[kubernetes_asyncio.client.V1EphemeralVolumeSource] = ..., fc: typing.Optional[kubernetes_asyncio.client.V1FCVolumeSource] = ..., flex_volume: typing.Optional[kubernetes_asyncio.client.V1FlexVolumeSource] = ..., flocker: typing.Optional[kubernetes_asyncio.client.V1FlockerVolumeSource] = ..., gce_persistent_disk: typing.Optional[kubernetes_asyncio.client.V1GCEPersistentDiskVolumeSource] = ..., git_repo: typing.Optional[kubernetes_asyncio.client.V1GitRepoVolumeSource] = ..., glusterfs: typing.Optional[kubernetes_asyncio.client.V1GlusterfsVolumeSource] = ..., host_path: typing.Optional[kubernetes_asyncio.client.V1HostPathVolumeSource] = ..., iscsi: typing.Optional[kubernetes_asyncio.client.V1ISCSIVolumeSource] = ..., name: str, nfs: typing.Optional[kubernetes_asyncio.client.V1NFSVolumeSource] = ..., persistent_volume_claim: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimVolumeSource] = ..., photon_persistent_disk: typing.Optional[kubernetes_asyncio.client.V1PhotonPersistentDiskVolumeSource] = ..., portworx_volume: typing.Optional[kubernetes_asyncio.client.V1PortworxVolumeSource] = ..., projected: typing.Optional[kubernetes_asyncio.client.V1ProjectedVolumeSource] = ..., quobyte: typing.Optional[kubernetes_asyncio.client.V1QuobyteVolumeSource] = ..., rbd: typing.Optional[kubernetes_asyncio.client.V1RBDVolumeSource] = ..., scale_io: typing.Optional[kubernetes_asyncio.client.V1ScaleIOVolumeSource] = ..., secret: typing.Optional[kubernetes_asyncio.client.V1SecretVolumeSource] = ..., storageos: typing.Optional[kubernetes_asyncio.client.V1StorageOSVolumeSource] = ..., vsphere_volume: typing.Optional[kubernetes_asyncio.client.V1VsphereVirtualDiskVolumeSource] = ...) -> None:
        ...
    def to_dict(self) -> V1VolumeDict:
        ...
class V1VolumeDict(typing.TypedDict, total=False):
    awsElasticBlockStore: typing.Optional[kubernetes_asyncio.client.V1AWSElasticBlockStoreVolumeSourceDict]
    azureDisk: typing.Optional[kubernetes_asyncio.client.V1AzureDiskVolumeSourceDict]
    azureFile: typing.Optional[kubernetes_asyncio.client.V1AzureFileVolumeSourceDict]
    cephfs: typing.Optional[kubernetes_asyncio.client.V1CephFSVolumeSourceDict]
    cinder: typing.Optional[kubernetes_asyncio.client.V1CinderVolumeSourceDict]
    configMap: typing.Optional[kubernetes_asyncio.client.V1ConfigMapVolumeSourceDict]
    csi: typing.Optional[kubernetes_asyncio.client.V1CSIVolumeSourceDict]
    downwardAPI: typing.Optional[kubernetes_asyncio.client.V1DownwardAPIVolumeSourceDict]
    emptyDir: typing.Optional[kubernetes_asyncio.client.V1EmptyDirVolumeSourceDict]
    ephemeral: typing.Optional[kubernetes_asyncio.client.V1EphemeralVolumeSourceDict]
    fc: typing.Optional[kubernetes_asyncio.client.V1FCVolumeSourceDict]
    flexVolume: typing.Optional[kubernetes_asyncio.client.V1FlexVolumeSourceDict]
    flocker: typing.Optional[kubernetes_asyncio.client.V1FlockerVolumeSourceDict]
    gcePersistentDisk: typing.Optional[kubernetes_asyncio.client.V1GCEPersistentDiskVolumeSourceDict]
    gitRepo: typing.Optional[kubernetes_asyncio.client.V1GitRepoVolumeSourceDict]
    glusterfs: typing.Optional[kubernetes_asyncio.client.V1GlusterfsVolumeSourceDict]
    hostPath: typing.Optional[kubernetes_asyncio.client.V1HostPathVolumeSourceDict]
    iscsi: typing.Optional[kubernetes_asyncio.client.V1ISCSIVolumeSourceDict]
    name: str
    nfs: typing.Optional[kubernetes_asyncio.client.V1NFSVolumeSourceDict]
    persistentVolumeClaim: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeClaimVolumeSourceDict]
    photonPersistentDisk: typing.Optional[kubernetes_asyncio.client.V1PhotonPersistentDiskVolumeSourceDict]
    portworxVolume: typing.Optional[kubernetes_asyncio.client.V1PortworxVolumeSourceDict]
    projected: typing.Optional[kubernetes_asyncio.client.V1ProjectedVolumeSourceDict]
    quobyte: typing.Optional[kubernetes_asyncio.client.V1QuobyteVolumeSourceDict]
    rbd: typing.Optional[kubernetes_asyncio.client.V1RBDVolumeSourceDict]
    scaleIO: typing.Optional[kubernetes_asyncio.client.V1ScaleIOVolumeSourceDict]
    secret: typing.Optional[kubernetes_asyncio.client.V1SecretVolumeSourceDict]
    storageos: typing.Optional[kubernetes_asyncio.client.V1StorageOSVolumeSourceDict]
    vsphereVolume: typing.Optional[kubernetes_asyncio.client.V1VsphereVirtualDiskVolumeSourceDict]
