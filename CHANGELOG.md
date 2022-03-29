# v22.6.2

* fix: add patch to update read buffer size ([#192](https://github.com/tomplus/kubernetes_asyncio/pull/192), [@tomplus](https://github.com/tomplus))

# v22.6.1

* fix: passing Bearer token in authorization header ([#190](https://github.com/tomplus/kubernetes_asyncio/pull/190), [@tomplus](https://github.com/tomplus))

# v22.6.0

* feat: regenerate library with OpenAPI Generator v5.4.0 ([#185](https://github.com/tomplus/kubernetes_asyncio/pull/185), [@tomplus](https://github.com/tomplus))
  Some changes from [OpenAPI Generator Changelog](https://github.com/OpenAPITools/openapi-generator/releases/) (previous version v4.3.0):
  - feat(python-asyncio): add support for proxy config using system env vars
  - add option to select/detect content-type
  - add `socket_options` to configuration for the rest client
  - correct return types if multiple responses are defined
  - subclass Python exceptions
  - fix Python UTF-8 Encoding Issue
* feat: add support for aiohttp proxy config using env vars ([#173](https://github.com/tomplus/kubernetes_asyncio/pull/173), [@icamposrivera](https://github.com/icamposrivera))

### API Change
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums (#104988, @liggitt) [SIG API Machinery, Apps and Network]
- A new score extension for NodeResourcesFit plugin that merges the functionality of `NodeResourcesLeastAllocated`, `NodeResourcesMostAllocated`, `RequestedToCapacityRatio` plugins, which are marked as deprecated as of v1beta2. In v1beta1, the three plugins can still be used in v1beta1 but not at the same time with the score extension of `NodeResourcesFit`. ([kubernetes/kubernetes#101822](https://github.com/kubernetes/kubernetes/pull/101822), [@yuzhiquan](https://github.com/yuzhiquan))
- A value of `Auto` is now a valid for the `service.kubernetes.io/topology-aware-hints` annotation. ([kubernetes/kubernetes#100728](https://github.com/kubernetes/kubernetes/pull/100728), [@robscott](https://github.com/robscott))
- Add `DataSourceRef` alpha field to PVC spec, which allows contents other than `PVCs` and `VolumeSnapshots` to be data sources. ([kubernetes/kubernetes#103276](https://github.com/kubernetes/kubernetes/pull/103276), [@bswartz](https://github.com/bswartz))
- Add `PersistentVolumeClaimDeletePoilcy` to StatefulSet API. ([kubernetes/kubernetes#99378](https://github.com/kubernetes/kubernetes/pull/99378), [@mattcary](https://github.com/mattcary))
- Add a new Priority and Fairness rule that exempts all probes (`/readyz`, `/healthz`, `/livez`) to prevent restarting of healthy `kube-apiserver` instance by kubelet. ([kubernetes/kubernetes#100678](https://github.com/kubernetes/kubernetes/pull/100678), [@tkashem](https://github.com/tkashem))
- Add alpha support for HostProcess containers on Windows ([kubernetes/kubernetes#99576](https://github.com/kubernetes/kubernetes/pull/99576), [@marosset](https://github.com/marosset)) [SIG API Machinery, Apps, Node, Testing and Windows]
- Add distributed tracing to the `kube-apiserver`. It is can be enabled with the feature gate `APIServerTracing` ([kubernetes/kubernetes#94942](https://github.com/kubernetes/kubernetes/pull/94942), [@dashpole](https://github.com/dashpole))
- Add three metrics to the job controller to monitor if a job works in healthy condition.
  `IndexedJob` has been promoted to Beta. ([kubernetes/kubernetes#101292](https://github.com/kubernetes/kubernetes/pull/101292), [@AliceZhang2016](https://github.com/AliceZhang2016))
- Added field `.status.uncountedTerminatedPods` to the Job resource. This field is used by the job controller to keep track of finished pods before adding them to the Job status counters. Pods created by the job controller get the finalizer `batch.kubernetes.io/job-tracking`
  Jobs that are tracked using this mechanism get the annotation `batch.kubernetes.io/job-tracking`. This is a temporary measure. Two releases after this feature graduates to beta, the annotation won't be added to Jobs anymore. ([kubernetes/kubernetes#98817](https://github.com/kubernetes/kubernetes/pull/98817), [@alculquicondor](https://github.com/alculquicondor))
- Added new kubelet alpha feature `SeccompDefault`. This feature enables falling back to
  the `RuntimeDefault` (former `runtime/default`) seccomp profile if nothing else is specified
  in the pod/container `SecurityContext` or the pod annotation level. To use the feature, enable
  the feature gate as well as set the kubelet configuration option `SeccompDefault`
  (`--seccomp-default`) to `true`. ([kubernetes/kubernetes#101943](https://github.com/kubernetes/kubernetes/pull/101943), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node]
- Adds the `ReadWriteOncePod` access mode for `PersistentVolumes` and `PersistentVolumeClaims`. Restricts volume access to a single pod on a single node. ([kubernetes/kubernetes#102028](https://github.com/kubernetes/kubernetes/pull/102028), [@chrishenzie](https://github.com/chrishenzie))
- Alpha swap support can now be enabled on Kubernetes nodes with the `NodeSwapEnabled` feature flag. See [KEP-2400](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2400-node-swap/README.md#design-details) for details. ([kubernetes/kubernetes#102823](https://github.com/kubernetes/kubernetes/pull/102823), [@ehashman](https://github.com/ehashman))
- Because of the implementation logic of `time.Format` in golang, the displayed time zone is not consistent. ([kubernetes/kubernetes#102366](https://github.com/kubernetes/kubernetes/pull/102366), [@cndoit18](https://github.com/cndoit18))
- Corrected the documentation for escaping dollar signs in a container's env, command and args property. ([kubernetes/kubernetes#101916](https://github.com/kubernetes/kubernetes/pull/101916), [@MartinKanters](https://github.com/MartinKanters)) [SIG Apps]
- Enable `MaxSurge` for `DaemonSet` by default. ([kubernetes/kubernetes#101742](https://github.com/kubernetes/kubernetes/pull/101742), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Enforce the `ReadWriteOncePod` PVC access mode during scheduling ([kubernetes/kubernetes#103082](https://github.com/kubernetes/kubernetes/pull/103082), [@chrishenzie](https://github.com/chrishenzie))
- Ephemeral containers are now allowed to configure a `securityContext` that differs from that of the Pod. Cluster administrators should ensure that security policy controllers support `EphemeralContainers` before enabling this feature in clusters. ([kubernetes/kubernetes#99023](https://github.com/kubernetes/kubernetes/pull/99023), [@verb](https://github.com/verb))
- Exec plugin authors can override default handling of standard input via new `interactiveMode` kubeconfig field. ([kubernetes/kubernetes#99310](https://github.com/kubernetes/kubernetes/pull/99310), [@ankeesler](https://github.com/ankeesler))
- If someone had the `ProbeTerminationGracePeriod` alpha feature enabled in 1.21, they should update/delete any workloads/pods with probe `terminationGracePeriods` < 1 before upgrading ([kubernetes/kubernetes#103245](https://github.com/kubernetes/kubernetes/pull/103245), [@wzshiming](https://github.com/wzshiming))
- Improved parsing of label selectors ([kubernetes/kubernetes#102188](https://github.com/kubernetes/kubernetes/pull/102188), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery]
- Introduce `minReadySeconds` api to the `StatefulSets`. ([kubernetes/kubernetes#100842](https://github.com/kubernetes/kubernetes/pull/100842), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Introducing Memory quality of service support with `cgroups v2 (Alpha)`. The `MemoryQoS` feature is now in Alpha. This allows `kubelet` running with `cgroups v2` to set memory QoS at container, pod and QoS level to protect and guarantee better memory quality. This feature can be enabled through feature gate Memory QoS. ([kubernetes/kubernetes#102970](https://github.com/kubernetes/kubernetes/pull/102970), [@borgerli](https://github.com/borgerli))
- Kube API server accepts `Impersonate-Uid` header to impersonate a user with a specific UID, in the same way that you can currently use `Impersonate-User`, `Impersonate-Group` and `Impersonate-Extra`. ([kubernetes/kubernetes#99961](https://github.com/kubernetes/kubernetes/pull/99961), [@margocrawf](https://github.com/margocrawf))
- Kube-apiserver: `--service-account-issuer` can be specified multiple times now, to enable non-disruptive change of issuer. ([kubernetes/kubernetes#101155](https://github.com/kubernetes/kubernetes/pull/101155), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Node and Testing]
- Kube-controller-manager: the `--horizontal-pod-autoscaler-use-rest-clients` flag and Heapster support in the horizontal pod autoscaler, deprecated since 1.12, is removed. ([kubernetes/kubernetes#90368](https://github.com/kubernetes/kubernetes/pull/90368), [@serathius](https://github.com/serathius))
- Kube-scheduler: a plugin enabled in a v1beta2 configuration file takes precedence over the default configuration for that plugin. This simplifies enabling default plugins with custom configuration without needing to explicitly disable those default plugins. ([kubernetes/kubernetes#99582](https://github.com/kubernetes/kubernetes/pull/99582), [@chendave](https://github.com/chendave))
- New `node-high` priority-level has been added to Suggested API Priority and ([kubernetes/kubernetes#101151](https://github.com/kubernetes/kubernetes/pull/101151), [@mborsz](https://github.com/mborsz))
- NodeSwapEnabled feature flag was renamed to NodeSwap
  
  The flag was only available in the 1.22.0-beta.1 release, and the new flag should be used going forward. ([kubernetes/kubernetes#103553](https://github.com/kubernetes/kubernetes/pull/103553), [@ehashman](https://github.com/ehashman)) [SIG Node]
- Omit comparison with boolean constant ([kubernetes/kubernetes#101523](https://github.com/kubernetes/kubernetes/pull/101523), [@chuntaochen](https://github.com/chuntaochen)) [SIG CLI and Cloud Provider]
- Removed the feature flag for probe-level termination grace period from Kubelet. If a user wants to disable this feature on already created pods, they will have to delete and recreate the pods. ([kubernetes/kubernetes#103168](https://github.com/kubernetes/kubernetes/pull/103168), [@raisaat](https://github.com/raisaat)) [SIG Apps and Node]
- Revert addition of Add `PersistentVolumeClaimDeletePoilcy` to `StatefulSet`API. ([kubernetes/kubernetes#103747](https://github.com/kubernetes/kubernetes/pull/103747), [@mattcary](https://github.com/mattcary))
- Scheduler could be configured  to consider new resources beside CPU and memory,  GPU for example, for the score plugin of `NodeResourcesBalancedAllocation`. ([kubernetes/kubernetes#101946](https://github.com/kubernetes/kubernetes/pull/101946), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- Server Side Apply now treats all <Some>Selector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#97989](https://github.com/kubernetes/kubernetes/pull/97989), [@Danil-Grigorev](https://github.com/Danil-Grigorev)) [SIG API Machinery]
- Suspend Job feature graduated to beta. Added the `action` label to Job controller sync metrics `job_sync_total` and `job_sync_duration_seconds`. ([kubernetes/kubernetes#102022](https://github.com/kubernetes/kubernetes/pull/102022), [@adtac](https://github.com/adtac))
- The API documentation for the DaemonSet's `spec.updateStrategy.rollingUpdate.maxUnavailable` field was corrected to state that the value is rounded up. ([kubernetes/kubernetes#101296](https://github.com/kubernetes/kubernetes/pull/101296), [@Miciah](https://github.com/Miciah))
- The `CSIServiceAccountToken` graduates to Ga and is unconditionally enabled. ([kubernetes/kubernetes#103001](https://github.com/kubernetes/kubernetes/pull/103001), [@zshihang](https://github.com/zshihang))
- The `CertificateSigningRequest.certificates.k8s.io` API supports an optional expirationSeconds field to allow the client to request a particular duration for the issued certificate.  The default signer implementations provided by the Kubernetes controller manager will honor this field as long as it does not exceed the --cluster-signing-duration flag. ([kubernetes/kubernetes#99494](https://github.com/kubernetes/kubernetes/pull/99494), [@enj](https://github.com/enj))
- The `EndpointSlicen Mirroring controller` no longer mirrors the `last-applied-configuration` annotation created by `kubectl` to update `EndpointSlices`. ([kubernetes/kubernetes#102731](https://github.com/kubernetes/kubernetes/pull/102731), [@sharmarajdaksh](https://github.com/sharmarajdaksh))
- The `NetworkPolicyEndPort` is graduated to beta and is enabled by default. ([kubernetes/kubernetes#102834](https://github.com/kubernetes/kubernetes/pull/102834), [@rikatz](https://github.com/rikatz))
- The `PodDeletionCost` feature has been promoted to beta, and enabled by default. ([kubernetes/kubernetes#101080](https://github.com/kubernetes/kubernetes/pull/101080), [@ahg-g](https://github.com/ahg-g))
- The `Server Side Apply` treats certain structs as atomic. Meaning the entire selector field is managed by a single writer and updated together. ([kubernetes/kubernetes#100684](https://github.com/kubernetes/kubernetes/pull/100684), [@Jefftree](https://github.com/Jefftree))
- The `ServiceAppProtocol` feature gate has been removed. It reached GA in Kubernetes ([kubernetes/kubernetes#103190](https://github.com/kubernetes/kubernetes/pull/103190), [@robscott](https://github.com/robscott))
- The `TerminationGracePeriodSeconds` on pod specs and container probes should not be negative. Negative values of `TerminationGracePeriodSeconds` will be treated as the value `1s` on the delete path. Immutable field validation will be relaxed in order to update negative values. In a future release, negative values will not be permitted. ([kubernetes/kubernetes#98866](https://github.com/kubernetes/kubernetes/pull/98866), [@wzshiming](https://github.com/wzshiming))
- The `kube-scheduler` component config `v1beta2` API available
  Three scheduler plugins deprecated (`NodeLabel`, `ServiceAffinity`, `NodePreferAvoidPods`). ([kubernetes/kubernetes#99597](https://github.com/kubernetes/kubernetes/pull/99597), [@adtac](https://github.com/adtac))
- The `pod/eviction` subresource now accepts `policy/v1` eviction requests in addition to `policy/v1beta1` eviction requests ([kubernetes/kubernetes#100724](https://github.com/kubernetes/kubernetes/pull/100724), [@liggitt](https://github.com/liggitt))
- The `podAffinity`, `NamespaceSelector` and the associated `CrossNamespaceAffinity` quota scope features graduate to Beta and they are now enabled by default. ([kubernetes/kubernetes#101496](https://github.com/kubernetes/kubernetes/pull/101496), [@ahg-g](https://github.com/ahg-g))
- The `pods/ephemeralcontainers` API now returns and expects a `Pod` object instead of `EphemeralContainers`. This is incompatible with the previous alpha-level API. ([kubernetes/kubernetes#101034](https://github.com/kubernetes/kubernetes/pull/101034), [@verb](https://github.com/verb)) [SIG Apps, Auth, CLI and Testing]
- The `v1.Node` and `.status.images[].names` are  now optional. ([kubernetes/kubernetes#102159](https://github.com/kubernetes/kubernetes/pull/102159), [@roycaihw](https://github.com/roycaihw))
- The deprecated flag `--algorithm-provider` has been removed from `kube-scheduler`. Use instead `ComponentConfig` to configure the set of enabled plugins. ([kubernetes/kubernetes#102239](https://github.com/kubernetes/kubernetes/pull/102239), [@Haleygo](https://github.com/Haleygo))
- The options `--ssh-user` and `--ssh-key` are removed. They only functioned on GCE, and only in-tree. Use the apiserver network proxy instead. ([kubernetes/kubernetes#102297](https://github.com/kubernetes/kubernetes/pull/102297), [@deads2k](https://github.com/deads2k))
- Track Job completion through status and Pod finalizers, removing dependency on Pod tombstones. ([kubernetes/kubernetes#98238](https://github.com/kubernetes/kubernetes/pull/98238), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps, Auth and Testing]
- Track ownership of scale subresource for all scalable resources i.e. Deployment, ReplicaSet, StatefulSet, ReplicationController, and Custom Resources. ([kubernetes/kubernetes#98377](https://github.com/kubernetes/kubernetes/pull/98377), [@nodo](https://github.com/nodo)) [SIG API Machinery and Testing]
- Revert addition of Add PersistentVolumeClaimDeletePoilcy to StatefulSet API. ([kubernetes/kubernetes#103747](https://github.com/kubernetes/kubernetes/pull/103747), [@mattcary](https://github.com/mattcary)) [SIG API Machinery and Apps]
- Added field .status.uncountedTerminatedPods to the Job resource. This field is used by the job controller to keep track of finished pods before adding them to the Job status counters.
  
  Pods created by the job controller get the finalizer batch.kubernetes.io/job-tracking
  
  Jobs that are tracked using this mechanism get the annotation batch.kubernetes.io/job-tracking. This is a temporary measure. Two releases after this feature graduates to beta, the annotation won't be added to Jobs anymore. ([kubernetes/kubernetes#98817](https://github.com/kubernetes/kubernetes/pull/98817), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps, Auth and CLI]
- Ephemeral containers are now allowed to configure a securityContext that differs from that of the Pod.
  
  Cluster administrators should ensure that security policy controllers support EphemeralContainers before enabling this feature in clusters. ([kubernetes/kubernetes#99023](https://github.com/kubernetes/kubernetes/pull/99023), [@verb](https://github.com/verb)) [SIG API Machinery, Apps, Auth and Node]
- If someone had the ProbeTerminationGracePeriod alpha feature enabled in 1.21, they should update/delete any workloads/pods with probe terminationGracePeriods < 1 before upgrading ([kubernetes/kubernetes#103245](https://github.com/kubernetes/kubernetes/pull/103245), [@wzshiming](https://github.com/wzshiming)) [SIG Apps and Node]
- Introducing Memory QoS support with cgroups v2 (Alpha)
  The MemoryQoS feature is now in Alpha. This allows kubelet running with cgroups v2 to set memory QoS at container, pod and QoS level to protect and guarantee better memory quality. This feature can be enabled through feature gate MemoryQoS. ([kubernetes/kubernetes#102970](https://github.com/kubernetes/kubernetes/pull/102970), [@borgerli](https://github.com/borgerli)) [SIG Node and Storage]
- NodeSwapEnabled feature flag was renamed to NodeSwap
  
  The flag was only available in the 1.22.0-beta.1 release, and the new flag should be used going forward. ([kubernetes/kubernetes#103553](https://github.com/kubernetes/kubernetes/pull/103553), [@ehashman](https://github.com/ehashman)) [SIG Node]
- Removed the feature flag for probe-level termination grace period from Kubelet. If a user wants to disable this feature on already created pods, they will have to delete and recreate the pods. ([kubernetes/kubernetes#103168](https://github.com/kubernetes/kubernetes/pull/103168), [@raisaat](https://github.com/raisaat)) [SIG Apps and Node]
- Track Job completion through status and Pod finalizers, removing dependency on Pod tombstones. ([kubernetes/kubernetes#98238](https://github.com/kubernetes/kubernetes/pull/98238), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps, Auth and Testing]
- When using `kubectl replace` (or the equivalent API call) on a Service, the caller no longer needs to do a read-modify-write cycle to fetch the allocated values for `.spec.clusterIP` and `.spec.ports[].nodePort`.  Instead the API server will automatically carry these forward from the original object when the new object does not specify them. ([kubernetes/kubernetes#103532](https://github.com/kubernetes/kubernetes/pull/103532), [@thockin](https://github.com/thockin)) [SIG Apps and Network]
- A new score extension for NodeResourcesFit plugin that merges the functionality of NodeResourcesLeastAllocated,NodeResourcesMostAllocated,RequestedToCapacityRatio plugins, which are marked as deprecated as of v1beta2. In v1beta1, the three plugins can still be used in v1beta1 but not at the same time with the score extension of NodeResourcesFit
- Add DataSourceRef alpha field to PVC spec, which allows contents other than PVCs and VolumeSnapshots to be data sources. ([kubernetes/kubernetes#103276](https://github.com/kubernetes/kubernetes/pull/103276), [@bswartz](https://github.com/bswartz)) [SIG API Machinery, Apps and Storage]
- Add PersistentVolumeClaimDeletePoilcy to StatefulSet API. ([kubernetes/kubernetes#99378](https://github.com/kubernetes/kubernetes/pull/99378), [@mattcary](https://github.com/mattcary)) [SIG API Machinery and Apps]
- Add distributed tracing to the kube-apiserver.  It is can be enabled with the feature gate: APIServerTracing=true ([kubernetes/kubernetes#94942](https://github.com/kubernetes/kubernetes/pull/94942), [@dashpole](https://github.com/dashpole)) [SIG API Machinery, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node, Storage and Testing]
- Added new kubelet alpha feature `SeccompDefault`. This feature enables falling back to
  the `RuntimeDefault` (former `runtime/default`) seccomp profile if nothing else is specified
  in the pod/container `SecurityContext` or the pod annotation level. To use the feature, enable
  the feature gate as well as set the kubelet configuration option `SeccompDefault`
  (`--seccomp-default`) to `true`. ([kubernetes/kubernetes#101943](https://github.com/kubernetes/kubernetes/pull/101943), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node]
- Adds the ReadWriteOncePod access mode for PersistentVolumes and PersistentVolumeClaims. Restricts volume access to a single pod on a single node. ([kubernetes/kubernetes#102028](https://github.com/kubernetes/kubernetes/pull/102028), [@chrishenzie](https://github.com/chrishenzie)) [SIG Apps, CLI, Node, Scheduling and Storage]
- Alpha swap support can now be enabled on Kubernetes nodes with the NodeSwapEnabled feature flag. See <website link> for details. ([kubernetes/kubernetes#102823](https://github.com/kubernetes/kubernetes/pull/102823), [@ehashman](https://github.com/ehashman)) [SIG Node]
- CSIServiceAccountToken is GA. ([kubernetes/kubernetes#103001](https://github.com/kubernetes/kubernetes/pull/103001), [@zshihang](https://github.com/zshihang)) [SIG Auth and Storage]
- Enforce the ReadWriteOncePod PVC access mode during scheduling ([kubernetes/kubernetes#103082](https://github.com/kubernetes/kubernetes/pull/103082), [@chrishenzie](https://github.com/chrishenzie)) [SIG Apps, CLI, Node, Scheduling and Storage]
- Improved parsing of label selectors ([kubernetes/kubernetes#102188](https://github.com/kubernetes/kubernetes/pull/102188), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery]
- Kube API server accepts Impersonate-Uid header to impersonate a user with a specific UID, in the same way that you can currently use Impersonate-User, Impersonate-Group and Impersonate-Extra ([kubernetes/kubernetes#99961](https://github.com/kubernetes/kubernetes/pull/99961), [@margocrawf](https://github.com/margocrawf)) [SIG API Machinery, Auth and Testing]
- Kube-scheduler: a plugin enabled in a v1beta2 configuration file takes precedence over the default configuration for that plugin; this simplifies enabling default plugins with custom configuration without needing to explicitly disable those default plugins. ([kubernetes/kubernetes#99582](https://github.com/kubernetes/kubernetes/pull/99582), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- Scheduler could be configured  to consider new resources beside CPU and memory,  GPU for example, for the score plugin of `NodeResourcesBalancedAllocation`. ([kubernetes/kubernetes#101946](https://github.com/kubernetes/kubernetes/pull/101946), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- Suspend Job feature graduated to beta
  Added the "action" label to Job controller sync metrics job_sync_total and job_sync_duration_seconds ([kubernetes/kubernetes#102022](https://github.com/kubernetes/kubernetes/pull/102022), [@adtac](https://github.com/adtac)) [SIG Apps, Instrumentation and Testing]
- TerminationGracePeriodSeconds on pod specs and container probes should not be negative.
  Negative values of TerminationGracePeriodSeconds will be treated as the value `1s` on the delete path.
  Immutable field validation will be relaxed in order to update negative values. 
  In a future release, negative values will not be permitted. ([kubernetes/kubernetes#98866](https://github.com/kubernetes/kubernetes/pull/98866), [@wzshiming](https://github.com/wzshiming)) [SIG API Machinery, Apps and Node]
- The API documentation for the DaemonSet's spec.updateStrategy.rollingUpdate.maxUnavailable field was corrected to state that the value is rounded up. ([kubernetes/kubernetes#101296](https://github.com/kubernetes/kubernetes/pull/101296), [@Miciah](https://github.com/Miciah)) [SIG Apps and CLI]
- The CertificateSigningRequest.certificates.k8s.io API supports an optional expirationSeconds field to allow the client to request a particular duration for the issued certificate.  The default signer implementations provided by the Kubernetes controller manager will honor this field as long as it does not exceed the --cluster-signing-duration flag. ([kubernetes/kubernetes#99494](https://github.com/kubernetes/kubernetes/pull/99494), [@enj](https://github.com/enj)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Security and Testing]
- The ServiceAppProtocol feature gate has been removed. It reached GA in Kubernetes 1.20. ([kubernetes/kubernetes#103190](https://github.com/kubernetes/kubernetes/pull/103190), [@robscott](https://github.com/robscott)) [SIG Network]
- Because of the implementation logic of time.Format in golang, the displayed time zone is not consistent ([kubernetes/kubernetes#102366](https://github.com/kubernetes/kubernetes/pull/102366), [@cndoit18](https://github.com/cndoit18)) [SIG Apps, Auth, Autoscaling, CLI, Cluster Lifecycle, Instrumentation, Network, Node and Testing]
- Endpoint slices mirroring controller no longer mirrors the last-applied-configuration annotation created by kubectl to updated endpoint slices ([kubernetes/kubernetes#102731](https://github.com/kubernetes/kubernetes/pull/102731), [@sharmarajdaksh](https://github.com/sharmarajdaksh)) [SIG API Machinery, Apps, Cloud Provider, Network, Release, Scheduling, Storage and Testing]
- Exec plugin authors can override default handling of standard input via new interactiveMode kubeconfig field ([kubernetes/kubernetes#99310](https://github.com/kubernetes/kubernetes/pull/99310), [@ankeesler](https://github.com/ankeesler)) [SIG API Machinery, Auth, CLI and Testing]
- Kube-scheduler component config v1beta2 API available
  Three scheduler plugins deprecated (NodeLabel, ServiceAffinity, NodePreferAvoidPods) ([kubernetes/kubernetes#99597](https://github.com/kubernetes/kubernetes/pull/99597), [@adtac](https://github.com/adtac)) [SIG Scheduling]
- Network Policy EndPort is graduated to beta and is enabled by default ([kubernetes/kubernetes#102834](https://github.com/kubernetes/kubernetes/pull/102834), [@rikatz](https://github.com/rikatz)) [SIG Network]
- --ssh-user and --ssh-key options are removed.  They only functioned on GCE, and only in-tree.  Use the apiserver network proxy instead. ([kubernetes/kubernetes#102297](https://github.com/kubernetes/kubernetes/pull/102297), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Cloud Provider and Testing]
- Enable MaxSurge for DS by default ([kubernetes/kubernetes#101742](https://github.com/kubernetes/kubernetes/pull/101742), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG Apps and Testing]
- Introduce minReadySeconds api to the StatefulSets. ([kubernetes/kubernetes#100842](https://github.com/kubernetes/kubernetes/pull/100842), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps and Testing]
- Kube-controller-manger: the `--horizontal-pod-autoscaler-use-rest-clients`  flag and Heapster support in the horizontal pod autoscaler, deprecated since 1.12, is removed. ([kubernetes/kubernetes#90368](https://github.com/kubernetes/kubernetes/pull/90368), [@serathius](https://github.com/serathius)) [SIG API Machinery, Apps, Autoscaling, Cloud Provider and Instrumentation]
- The deprecated flag --algorithm-provider has been removed from kube-scheduler. Use instead ComponentConfig to configure the set of enabled plugins ([kubernetes/kubernetes#102239](https://github.com/kubernetes/kubernetes/pull/102239), [@Haleygo](https://github.com/Haleygo)) [SIG Cloud Provider and Scheduling]
- Add alpha support for HostProcess containers on Windows ([kubernetes/kubernetes#99576](https://github.com/kubernetes/kubernetes/pull/99576), [@marosset](https://github.com/marosset)) [SIG API Machinery, Apps, Node, Testing and Windows]
- Add three metrics to job controller to monitor if Job works in a healthy condition.
  IndexedJob promoted to Beta ([kubernetes/kubernetes#101292](https://github.com/kubernetes/kubernetes/pull/101292), [@AliceZhang2016](https://github.com/AliceZhang2016)) [SIG Apps, Instrumentation and Testing]
- Corrected the documentation for escaping dollar signs in a container's env, command and args property. ([kubernetes/kubernetes#101916](https://github.com/kubernetes/kubernetes/pull/101916), [@MartinKanters](https://github.com/MartinKanters)) [SIG Apps]
- Omit comparison with boolean constant ([kubernetes/kubernetes#101523](https://github.com/kubernetes/kubernetes/pull/101523), [@GreenApple10](https://github.com/GreenApple10)) [SIG CLI and Cloud Provider]
- Pod Affinity NamespaceSelector and the associated CrossNamespaceAffinity quota scope graduated to beta ([kubernetes/kubernetes#101496](https://github.com/kubernetes/kubernetes/pull/101496), [@ahg-g](https://github.com/ahg-g)) [SIG API Machinery, Apps and Testing]
- V1.Node .status.images[].names is now optional ([kubernetes/kubernetes#102159](https://github.com/kubernetes/kubernetes/pull/102159), [@roycaihw](https://github.com/roycaihw)) [SIG Apps and Node]
- "Auto" is now a valid value for the `service.kubernetes.io/topology-aware-hints` annotation. ([kubernetes/kubernetes#100728](https://github.com/kubernetes/kubernetes/pull/100728), [@robscott](https://github.com/robscott)) [SIG Apps, Instrumentation and Network]
- Kube-apiserver: `--service-account-issuer` can be specified multiple times now, to enable non-disruptive change of issuer. ([kubernetes/kubernetes#101155](https://github.com/kubernetes/kubernetes/pull/101155), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Node and Testing]
- New "node-high" priority-level has been added to Suggested API Priority and Fairness configuration. ([kubernetes/kubernetes#101151](https://github.com/kubernetes/kubernetes/pull/101151), [@mborsz](https://github.com/mborsz)) [SIG API Machinery]
- PodDeletionCost promoted to Beta ([kubernetes/kubernetes#101080](https://github.com/kubernetes/kubernetes/pull/101080), [@ahg-g](https://github.com/ahg-g)) [SIG Apps]
- SSA treats certain structs as atomic ([kubernetes/kubernetes#100684](https://github.com/kubernetes/kubernetes/pull/100684), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery, Auth, Node and Storage]
- Server Side Apply now treats all <Some>Selector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#97989](https://github.com/kubernetes/kubernetes/pull/97989), [@Danil-Grigorev](https://github.com/Danil-Grigorev)) [SIG API Machinery]
- The `pods/ephemeralcontainers` API now returns and expects a `Pod` object instead of `EphemeralContainers`. This is incompatible with the previous alpha-level API. ([kubernetes/kubernetes#101034](https://github.com/kubernetes/kubernetes/pull/101034), [@verb](https://github.com/verb)) [SIG Apps, Auth, CLI and Testing]
- The pod/eviction subresource now accepts policy/v1 Eviction requests in addition to policy/v1beta1 Eviction requests ([kubernetes/kubernetes#100724](https://github.com/kubernetes/kubernetes/pull/100724), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Architecture, Auth, CLI, Storage and Testing]
- Track ownership of scale subresource for all scalable resources i.e. Deployment, ReplicaSet, StatefulSet, ReplicationController, and Custom Resources. ([kubernetes/kubernetes#98377](https://github.com/kubernetes/kubernetes/pull/98377), [@nodo](https://github.com/nodo)) [SIG API Machinery and Testing]
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#100678](https://github.com/kubernetes/kubernetes/pull/100678), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]

# v21.7.1

* fix: add missing change in latest regnerated lib ([#184](https://github.com/tomplus/kubernetes_asyncio/pull/184), [@tomplus](https://github.com/tomplus))

# v21.7.0

### API Change
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums (#104989, @liggitt) [SIG API Machinery, Apps and Network]
- "Auto" is now a valid value for the `service.kubernetes.io/topology-aware-hints` annotation. ([kubernetes/kubernetes#100728](https://github.com/kubernetes/kubernetes/pull/100728), [@robscott](https://github.com/robscott)) [SIG Apps, Instrumentation and Network]
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#101111](https://github.com/kubernetes/kubernetes/pull/101111), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]
- 1. PodAffinityTerm includes a namespaceSelector field to allow selecting eligible namespaces based on their labels. 
  2. A new CrossNamespacePodAffinity quota scope API that allows restricting which namespaces allowed to use PodAffinityTerm with corss-namespace reference via namespaceSelector or namespaces fields. ([kubernetes/kubernetes#98582](https://github.com/kubernetes/kubernetes/pull/98582), [@ahg-g](https://github.com/ahg-g)) [SIG API Machinery, Apps, Auth and Testing]
- Add Probe-level terminationGracePeriodSeconds field ([kubernetes/kubernetes#99375](https://github.com/kubernetes/kubernetes/pull/99375), [@ehashman](https://github.com/ehashman)) [SIG API Machinery, Apps, Node and Testing]
- Added `.spec.completionMode` field to Job, with accepted values `NonIndexed` (default) and `Indexed`. This is an alpha field and is only honored by servers with the `IndexedJob` feature gate enabled. ([kubernetes/kubernetes#98441](https://github.com/kubernetes/kubernetes/pull/98441), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- Adds support for endPort field in NetworkPolicy ([kubernetes/kubernetes#97058](https://github.com/kubernetes/kubernetes/pull/97058), [@rikatz](https://github.com/rikatz)) [SIG Apps and Network]
- CSIServiceAccountToken graduates to Beta and enabled by default. ([kubernetes/kubernetes#99298](https://github.com/kubernetes/kubernetes/pull/99298), [@zshihang](https://github.com/zshihang))
- Cluster admins can now turn off `/debug/pprof` and `/debug/flags/v` endpoint in kubelet by setting `enableProfilingHandler` and `enableDebugFlagsHandler` to `false` in the Kubelet configuration file. Options `enableProfilingHandler` and `enableDebugFlagsHandler` can be set to `true` only when `enableDebuggingHandlers` is also set to `true`. ([kubernetes/kubernetes#98458](https://github.com/kubernetes/kubernetes/pull/98458), [@SaranBalaji90](https://github.com/SaranBalaji90))
- DaemonSets accept a MaxSurge integer or percent on their rolling update strategy that will launch the updated pod on nodes and wait for those pods to go ready before marking the old out-of-date pods as deleted. This allows workloads to avoid downtime during upgrades when deployed using DaemonSets. This feature is alpha and is behind the DaemonSetUpdateSurge feature gate. ([kubernetes/kubernetes#96441](https://github.com/kubernetes/kubernetes/pull/96441), [@smarterclayton](https://github.com/smarterclayton)) [SIG Apps and Testing]
- Enable SPDY pings to keep connections alive, so that `kubectl exec` and `kubectl portforward` won't be interrupted. ([kubernetes/kubernetes#97083](https://github.com/kubernetes/kubernetes/pull/97083), [@knight42](https://github.com/knight42)) [SIG API Machinery and CLI]
- FieldManager no longer owns fields that get reset before the object is persisted (e.g. "status wiping"). ([kubernetes/kubernetes#99661](https://github.com/kubernetes/kubernetes/pull/99661), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Auth and Testing]
- Fixes server-side apply for APIService resources. ([kubernetes/kubernetes#98576](https://github.com/kubernetes/kubernetes/pull/98576), [@kevindelgado](https://github.com/kevindelgado))
- Generic ephemeral volumes are beta. ([kubernetes/kubernetes#99643](https://github.com/kubernetes/kubernetes/pull/99643), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Node, Storage and Testing]
- Hugepages request values are limited to integer multiples of the page size. ([kubernetes/kubernetes#98515](https://github.com/kubernetes/kubernetes/pull/98515), [@lala123912](https://github.com/lala123912)) [SIG Apps]
- Implement the GetAvailableResources in the podresources API. ([kubernetes/kubernetes#95734](https://github.com/kubernetes/kubernetes/pull/95734), [@fromanirh](https://github.com/fromanirh)) [SIG Instrumentation, Node and Testing]
- IngressClass resource can now reference a resource in a specific namespace 
  for implementation-specific configuration (previously only Cluster-level resources were allowed). 
  This feature can be enabled using the IngressClassNamespacedParams feature gate. ([kubernetes/kubernetes#99275](https://github.com/kubernetes/kubernetes/pull/99275), [@hbagdi](https://github.com/hbagdi))
- Jobs API has a new `.spec.suspend` field that can be used to suspend and resume Jobs. This is an alpha field which is only honored by servers with the `SuspendJob` feature gate enabled. ([kubernetes/kubernetes#98727](https://github.com/kubernetes/kubernetes/pull/98727), [@adtac](https://github.com/adtac))
- Kubelet Graceful Node Shutdown feature graduates to Beta and enabled by default. ([kubernetes/kubernetes#99735](https://github.com/kubernetes/kubernetes/pull/99735), [@bobbypage](https://github.com/bobbypage))
- Kubernetes is now built using go1.15.7 ([kubernetes/kubernetes#98363](https://github.com/kubernetes/kubernetes/pull/98363), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Node, Release and Testing]
- Namespace API objects now have a `kubernetes.io/metadata.name` label matching their metadata.name field to allow selecting any namespace by its name using a label selector. ([kubernetes/kubernetes#96968](https://github.com/kubernetes/kubernetes/pull/96968), [@jayunit100](https://github.com/jayunit100)) [SIG API Machinery, Apps, Cloud Provider, Storage and Testing]
- One new field "InternalTrafficPolicy" in Service is added.
  It specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only.
  "Cluster" routes internal traffic to a Service to all endpoints.
  "Local" routes traffic to node-local endpoints only, and traffic is dropped if no node-local endpoints are ready.
  The default value is "Cluster". ([kubernetes/kubernetes#96600](https://github.com/kubernetes/kubernetes/pull/96600), [@maplain](https://github.com/maplain)) [SIG API Machinery, Apps and Network]
- PodDisruptionBudget API objects can now contain conditions in status. ([kubernetes/kubernetes#98127](https://github.com/kubernetes/kubernetes/pull/98127), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Cluster Lifecycle and Instrumentation]
- PodSecurityPolicy only stores "generic" as allowed volume type if the GenericEphemeralVolume feature gate is enabled ([kubernetes/kubernetes#98918](https://github.com/kubernetes/kubernetes/pull/98918), [@pohly](https://github.com/pohly)) [SIG Auth and Security]
- Promote CronJobs to batch/v1 ([kubernetes/kubernetes#99423](https://github.com/kubernetes/kubernetes/pull/99423), [@soltysh](https://github.com/soltysh)) [SIG API Machinery, Apps, CLI and Testing]
- Promote Immutable Secrets/ConfigMaps feature to Stable. This allows to set `immutable` field in Secret or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#97615](https://github.com/kubernetes/kubernetes/pull/97615), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps, Architecture, Node and Testing]
- Remove support for building Kubernetes with bazel. ([kubernetes/kubernetes#99561](https://github.com/kubernetes/kubernetes/pull/99561), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage, Testing and Windows]
- Scheduler extender filter interface now can report unresolvable failed nodes in the new field `FailedAndUnresolvableNodes` of  `ExtenderFilterResult` struct. Nodes in this map will be skipped in the preemption phase. ([kubernetes/kubernetes#92866](https://github.com/kubernetes/kubernetes/pull/92866), [@cofyc](https://github.com/cofyc)) [SIG Scheduling]
- Services can specify loadBalancerClass to use a custom load balancer ([kubernetes/kubernetes#98277](https://github.com/kubernetes/kubernetes/pull/98277), [@XudongLiuHarold](https://github.com/XudongLiuHarold))
- Storage capacity tracking (= the CSIStorageCapacity feature) graduates to Beta and enabled by default, storage.k8s.io/v1alpha1/VolumeAttachment and storage.k8s.io/v1alpha1/CSIStorageCapacity objects are deprecated ([kubernetes/kubernetes#99641](https://github.com/kubernetes/kubernetes/pull/99641), [@pohly](https://github.com/pohly))
- Support for Indexed Job: a Job that is considered completed when Pods associated to indexes from 0 to (.spec.completions-1) have succeeded. ([kubernetes/kubernetes#98812](https://github.com/kubernetes/kubernetes/pull/98812), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- The BoundServiceAccountTokenVolume feature has been promoted to beta, and enabled by default.
  - This changes the tokens provided to containers at `/var/run/secrets/kubernetes.io/serviceaccount/token` to be time-limited, auto-refreshed, and invalidated when the containing pod is deleted.
  - Clients should reload the token from disk periodically (once per minute is recommended) to ensure they continue to use a valid token. `k8s.io/client-go` version v11.0.0+ and v0.15.0+ reload tokens automatically.
  - By default, injected tokens are given an extended lifetime so they remain valid even after a new refreshed token is provided. The metric `serviceaccount_stale_tokens_total` can be used to monitor for workloads that are depending on the extended lifetime and are continuing to use tokens even after a refreshed token is provided to the container. If that metric indicates no existing workloads are depending on extended lifetimes, injected token lifetime can be shortened to 1 hour by starting `kube-apiserver` with `--service-account-extend-token-expiration=false`. ([kubernetes/kubernetes#95667](https://github.com/kubernetes/kubernetes/pull/95667), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle and Testing]
- The EndpointSlice Controllers are now GA. The `EndpointSliceController` will not populate the `deprecatedTopology` field and will only provide topology information through the `zone` and `nodeName` fields. ([kubernetes/kubernetes#99870](https://github.com/kubernetes/kubernetes/pull/99870), [@swetharepakula](https://github.com/swetharepakula))
- The Endpoints controller will now set the `endpoints.kubernetes.io/over-capacity` annotation to "warning" when an Endpoints resource contains more than 1000 addresses. In a future release, the controller will truncate Endpoints that exceed this limit. The EndpointSlice API can be used to support significantly larger number of addresses. ([kubernetes/kubernetes#99975](https://github.com/kubernetes/kubernetes/pull/99975), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The PodDisruptionBudget API has been promoted to policy/v1 with no schema changes. The only functional change is that an empty selector (`{}`) written to a policy/v1 PodDisruptionBudget now selects all pods in the namespace. The behavior of the policy/v1beta1 API remains unchanged. The policy/v1beta1 PodDisruptionBudget API is deprecated and will no longer be served in 1.25+. ([kubernetes/kubernetes#99290](https://github.com/kubernetes/kubernetes/pull/99290), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Scheduling and Testing]
- The `EndpointSlice` API is now GA. The `EndpointSlice` topology field has been removed from the GA API and will be replaced by a new per Endpoint Zone field. If the topology field was previously used, it will be converted into an annotation in the v1 Resource. The `discovery.k8s.io/v1alpha1` API is removed. ([kubernetes/kubernetes#99662](https://github.com/kubernetes/kubernetes/pull/99662), [@swetharepakula](https://github.com/swetharepakula))
- The `controller.kubernetes.io/pod-deletion-cost` annotation can be set to offer a hint on the cost of deleting a `Pod` compared to other pods belonging to the same ReplicaSet. Pods with lower deletion cost are deleted first. This is an alpha feature. ([kubernetes/kubernetes#99163](https://github.com/kubernetes/kubernetes/pull/99163), [@ahg-g](https://github.com/ahg-g))
- The kube-apiserver now resets `managedFields` that got corrupted by a mutating admission controller. ([kubernetes/kubernetes#98074](https://github.com/kubernetes/kubernetes/pull/98074), [@kwiesmueller](https://github.com/kwiesmueller))
- Topology Aware Hints are now available in alpha and can be enabled with the `TopologyAwareHints` feature gate. ([kubernetes/kubernetes#99522](https://github.com/kubernetes/kubernetes/pull/99522), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Instrumentation, Network and Testing]
- Users might specify the `kubectl.kubernetes.io/default-exec-container` annotation in a Pod to preselect container for kubectl commands. ([kubernetes/kubernetes#97099](https://github.com/kubernetes/kubernetes/pull/97099), [@pacoxu](https://github.com/pacoxu)) [SIG CLI]
- Add Probe-level terminationGracePeriodSeconds field ([kubernetes/kubernetes#99375](https://github.com/kubernetes/kubernetes/pull/99375), [@ehashman](https://github.com/ehashman)) [SIG API Machinery, Apps, Node and Testing]
- CSIServiceAccountToken is Beta now ([kubernetes/kubernetes#99298](https://github.com/kubernetes/kubernetes/pull/99298), [@zshihang](https://github.com/zshihang)) [SIG Auth, Storage and Testing]
- Discovery.k8s.io/v1beta1 EndpointSlices are deprecated in favor of discovery.k8s.io/v1, and will no longer be served in Kubernetes v1.25. ([kubernetes/kubernetes#100472](https://github.com/kubernetes/kubernetes/pull/100472), [@liggitt](https://github.com/liggitt)) [SIG Network]
- FieldManager no longer owns fields that get reset before the object is persisted (e.g. "status wiping"). ([kubernetes/kubernetes#99661](https://github.com/kubernetes/kubernetes/pull/99661), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Auth and Testing]
- Generic ephemeral volumes are beta. ([kubernetes/kubernetes#99643](https://github.com/kubernetes/kubernetes/pull/99643), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Node, Storage and Testing]
- Implement the GetAvailableResources in the podresources API. ([kubernetes/kubernetes#95734](https://github.com/kubernetes/kubernetes/pull/95734), [@fromanirh](https://github.com/fromanirh)) [SIG Instrumentation, Node and Testing]
- The Endpoints controller will now set the `endpoints.kubernetes.io/over-capacity` annotation to "warning" when an Endpoints resource contains more than 1000 addresses. In a future release, the controller will truncate Endpoints that exceed this limit. The EndpointSlice API can be used to support significantly larger number of addresses. ([kubernetes/kubernetes#99975](https://github.com/kubernetes/kubernetes/pull/99975), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The PodDisruptionBudget API has been promoted to policy/v1 with no schema changes. The only functional change is that an empty selector (`{}`) written to a policy/v1 PodDisruptionBudget now selects all pods in the namespace. The behavior of the policy/v1beta1 API remains unchanged. The policy/v1beta1 PodDisruptionBudget API is deprecated and will no longer be served in 1.25+. ([kubernetes/kubernetes#99290](https://github.com/kubernetes/kubernetes/pull/99290), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Scheduling and Testing]
- Topology Aware Hints are now available in alpha and can be enabled with the `TopologyAwareHints` feature gate. ([kubernetes/kubernetes#99522](https://github.com/kubernetes/kubernetes/pull/99522), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Instrumentation, Network and Testing]
- 1. PodAffinityTerm includes a namespaceSelector field to allow selecting eligible namespaces based on their labels. 
  2. A new CrossNamespacePodAffinity quota scope API that allows restricting which namespaces allowed to use PodAffinityTerm with corss-namespace reference via namespaceSelector or namespaces fields. ([kubernetes/kubernetes#98582](https://github.com/kubernetes/kubernetes/pull/98582), [@ahg-g](https://github.com/ahg-g)) [SIG API Machinery, Apps, Auth and Testing]
- Add a default metadata name labels for selecting any namespace by its name. ([kubernetes/kubernetes#96968](https://github.com/kubernetes/kubernetes/pull/96968), [@jayunit100](https://github.com/jayunit100)) [SIG API Machinery, Apps, Cloud Provider, Storage and Testing]
- Added `.spec.completionMode` field to Job, with accepted values `NonIndexed` (default) and `Indexed` ([kubernetes/kubernetes#98441](https://github.com/kubernetes/kubernetes/pull/98441), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- Clarified NetworkPolicy policyTypes documentation ([kubernetes/kubernetes#97216](https://github.com/kubernetes/kubernetes/pull/97216), [@joejulian](https://github.com/joejulian)) [SIG Network]
- DaemonSets accept a MaxSurge integer or percent on their rolling update strategy that will launch the updated pod on nodes and wait for those pods to go ready before marking the old out-of-date pods as deleted. This allows workloads to avoid downtime during upgrades when deployed using DaemonSets. This feature is alpha and is behind the DaemonSetUpdateSurge feature gate. ([kubernetes/kubernetes#96441](https://github.com/kubernetes/kubernetes/pull/96441), [@smarterclayton](https://github.com/smarterclayton)) [SIG Apps and Testing]
- EndpointSlice API is now GA. The EndpointSlice topology field has been removed from the GA API and will be replaced by a new per Endpoint Zone field. If the topology field was previously used, it will be converted into an annotation in the v1 Resource. The discovery.k8s.io/v1alpha1 API is removed. ([kubernetes/kubernetes#99662](https://github.com/kubernetes/kubernetes/pull/99662), [@swetharepakula](https://github.com/swetharepakula)) [SIG API Machinery, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network and Testing]
- EndpointSlice Controllers are now GA. The EndpointSlice Controller will not populate the `deprecatedTopology` field and will only provide topology information through the `zone` and `nodeName` fields. ([kubernetes/kubernetes#99870](https://github.com/kubernetes/kubernetes/pull/99870), [@swetharepakula](https://github.com/swetharepakula)) [SIG API Machinery, Apps, Auth, Network and Testing]
- IngressClass resource can now reference a resource in a specific namespace 
  for implementation-specific configuration(previously only Cluster-level resources were allowed). 
  This feature can be enabled using the IngressClassNamespacedParams feature gate. ([kubernetes/kubernetes#99275](https://github.com/kubernetes/kubernetes/pull/99275), [@hbagdi](https://github.com/hbagdi)) [SIG API Machinery, CLI and Network]
- Introduce conditions for PodDisruptionBudget ([kubernetes/kubernetes#98127](https://github.com/kubernetes/kubernetes/pull/98127), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Cluster Lifecycle and Instrumentation]
- Jobs API has a new .spec.suspend field that can be used to suspend and resume Jobs ([kubernetes/kubernetes#98727](https://github.com/kubernetes/kubernetes/pull/98727), [@adtac](https://github.com/adtac)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Kubelet Graceful Node Shutdown feature is now beta. ([kubernetes/kubernetes#99735](https://github.com/kubernetes/kubernetes/pull/99735), [@bobbypage](https://github.com/bobbypage)) [SIG Node]
- Limit the quest value of hugepage to integer multiple of page size. ([kubernetes/kubernetes#98515](https://github.com/kubernetes/kubernetes/pull/98515), [@lala123912](https://github.com/lala123912)) [SIG Apps]
- One new field "InternalTrafficPolicy" in Service is added.
  It specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only.
  "Cluster" routes internal traffic to a Service to all endpoints.
  "Local" routes traffic to node-local endpoints only, and traffic is dropped if no node-local endpoints are ready.
  The default value is "Cluster". ([kubernetes/kubernetes#96600](https://github.com/kubernetes/kubernetes/pull/96600), [@maplain](https://github.com/maplain)) [SIG API Machinery, Apps and Network]
- PodSecurityPolicy only stores "generic" as allowed volume type if the GenericEphemeralVolume feature gate is enabled ([kubernetes/kubernetes#98918](https://github.com/kubernetes/kubernetes/pull/98918), [@pohly](https://github.com/pohly)) [SIG Auth and Security]
- Promote CronJobs to batch/v1 ([kubernetes/kubernetes#99423](https://github.com/kubernetes/kubernetes/pull/99423), [@soltysh](https://github.com/soltysh)) [SIG API Machinery, Apps, CLI and Testing]
- Remove support for building Kubernetes with bazel. ([kubernetes/kubernetes#99561](https://github.com/kubernetes/kubernetes/pull/99561), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage, Testing and Windows]
- Setting loadBalancerClass in load balancer type of service is available with this PR. 
  Users who want to use a custom load balancer can specify loadBalancerClass to achieve it. ([kubernetes/kubernetes#98277](https://github.com/kubernetes/kubernetes/pull/98277), [@XudongLiuHarold](https://github.com/XudongLiuHarold)) [SIG API Machinery, Apps, Cloud Provider and Network]
- Storage capacity tracking (= the CSIStorageCapacity feature) is beta, storage.k8s.io/v1alpha1/VolumeAttachment and storage.k8s.io/v1alpha1/CSIStorageCapacity objects are deprecated ([kubernetes/kubernetes#99641](https://github.com/kubernetes/kubernetes/pull/99641), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Scheduling, Storage and Testing]
- Support for Indexed Job: a Job that is considered completed when Pods associated to indexes from 0 to (.spec.completions-1) have succeeded. ([kubernetes/kubernetes#98812](https://github.com/kubernetes/kubernetes/pull/98812), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- The apiserver now resets managedFields that got corrupted by a mutating admission controller. ([kubernetes/kubernetes#98074](https://github.com/kubernetes/kubernetes/pull/98074), [@kwiesmueller](https://github.com/kwiesmueller)) [SIG API Machinery and Testing]
- `controller.kubernetes.io/pod-deletion-cost` annotation can be set to offer a hint on the cost of deleting a pod compared to other pods belonging to the same ReplicaSet. Pods with lower deletion cost are deleted first. This is an alpha feature. ([kubernetes/kubernetes#99163](https://github.com/kubernetes/kubernetes/pull/99163), [@ahg-g](https://github.com/ahg-g)) [SIG Apps]
- Cluster admins can now turn off /debug/pprof and /debug/flags/v endpoint in kubelet by setting enableProfilingHandler and enableDebugFlagsHandler to false in their kubelet configuration file. enableProfilingHandler and enableDebugFlagsHandler can be set to true only when enableDebuggingHandlers is also set to true. ([kubernetes/kubernetes#98458](https://github.com/kubernetes/kubernetes/pull/98458), [@SaranBalaji90](https://github.com/SaranBalaji90)) [SIG Node]
- The BoundServiceAccountTokenVolume feature has been promoted to beta, and enabled by default.
  - This changes the tokens provided to containers at `/var/run/secrets/kubernetes.io/serviceaccount/token` to be time-limited, auto-refreshed, and invalidated when the containing pod is deleted.
  - Clients should reload the token from disk periodically (once per minute is recommended) to ensure they continue to use a valid token. `k8s.io/client-go` version v11.0.0+ and v0.15.0+ reload tokens automatically.
  - By default, injected tokens are given an extended lifetime so they remain valid even after a new refreshed token is provided. The metric `serviceaccount_stale_tokens_total` can be used to monitor for workloads that are depending on the extended lifetime and are continuing to use tokens even after a refreshed token is provided to the container. If that metric indicates no existing workloads are depending on extended lifetimes, injected token lifetime can be shortened to 1 hour by starting `kube-apiserver` with `--service-account-extend-token-expiration=false`. ([kubernetes/kubernetes#95667](https://github.com/kubernetes/kubernetes/pull/95667), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle and Testing]
- Adds support for portRange / EndPort in Network Policy ([kubernetes/kubernetes#97058](https://github.com/kubernetes/kubernetes/pull/97058), [@rikatz](https://github.com/rikatz)) [SIG Apps and Network]
- Fixes using server-side apply with APIService resources ([kubernetes/kubernetes#98576](https://github.com/kubernetes/kubernetes/pull/98576), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Apps and Testing]
- Kubernetes is now built using go1.15.7 ([kubernetes/kubernetes#98363](https://github.com/kubernetes/kubernetes/pull/98363), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Node, Release and Testing]
- Scheduler extender filter interface now can report unresolvable failed nodes in the new field `FailedAndUnresolvableNodes` of  `ExtenderFilterResult` struct. Nodes in this map will be skipped in the preemption phase. ([kubernetes/kubernetes#92866](https://github.com/kubernetes/kubernetes/pull/92866), [@cofyc](https://github.com/cofyc)) [SIG Scheduling]
- Enable SPDY pings to keep connections alive, so that `kubectl exec` and `kubectl port-forward` won't be interrupted. ([kubernetes/kubernetes#97083](https://github.com/kubernetes/kubernetes/pull/97083), [@knight42](https://github.com/knight42)) [SIG API Machinery and CLI]
- Change the APIVersion proto name of BoundObjectRef from aPIVersion to apiVersion. ([kubernetes/kubernetes#97379](https://github.com/kubernetes/kubernetes/pull/97379), [@kebe7jun](https://github.com/kebe7jun)) [SIG Auth]
- Promote Immutable Secrets/ConfigMaps feature to Stable.
  This allows to set `Immutable` field in Secrets or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#97615](https://github.com/kubernetes/kubernetes/pull/97615), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps, Architecture, Node and Testing]

# v20.13.0

### API Change
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums (#104990, @liggitt) [SIG API Machinery, Apps and Network]
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#101112](https://github.com/kubernetes/kubernetes/pull/101112), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]
- Fixes using server-side apply with APIService resources ([kubernetes/kubernetes#100714](https://github.com/kubernetes/kubernetes/pull/100714), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Apps and Testing]
- Regenerate protobuf code to fix CVE-2021-3121 ([kubernetes/kubernetes#100501](https://github.com/kubernetes/kubernetes/pull/100501), [@joelsmith](https://github.com/joelsmith)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node and Storage]
- Kubernetes is now built using go1.15.8 ([kubernetes/kubernetes#98962](https://github.com/kubernetes/kubernetes/pull/98962), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Release and Testing]
- `TokenRequest` and `TokenRequestProjection` features have been promoted to GA. This feature allows generating service account tokens that are not visible in Secret objects and are tied to the lifetime of a Pod object. See https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection for details on configuring and using this feature. The `TokenRequest` and `TokenRequestProjection` feature gates will be removed in v1.21.
  - kubeadm's kube-apiserver Pod manifest now includes the following flags by default "--service-account-key-file", "--service-account-signing-key-file", "--service-account-issuer". ([kubernetes/kubernetes#93258](https://github.com/kubernetes/kubernetes/pull/93258), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle, Storage and Testing]
- A new `nofuzz` go build tag now disables gofuzz support. Release binaries enable this. ([kubernetes/kubernetes#92491](https://github.com/kubernetes/kubernetes/pull/92491), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery]
- Add WindowsContainerResources and Annotations to CRI-API UpdateContainerResourcesRequest ([kubernetes/kubernetes#95741](https://github.com/kubernetes/kubernetes/pull/95741), [@katiewasnothere](https://github.com/katiewasnothere)) [SIG Node]
- Add a `serving` and `terminating` condition to the EndpointSlice API.
  `serving` tracks the readiness of endpoints regardless of their terminating state. This is distinct from `ready` since `ready` is only true when pods are not terminating. 
  `terminating` is true when an endpoint is terminating. For pods this is any endpoint with a deletion timestamp. ([kubernetes/kubernetes#92968](https://github.com/kubernetes/kubernetes/pull/92968), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps and Network]
- Add dual-stack Services (alpha).  This is a BREAKING CHANGE to an alpha API.
  It changes the dual-stack API wrt Service from a single ipFamily field to 3
  fields: ipFamilyPolicy (SingleStack, PreferDualStack, RequireDualStack),
  ipFamilies (a list of families assigned), and clusterIPs (inclusive of
  clusterIP).  Most users do not need to set anything at all, defaulting will
  handle it for them.  Services are single-stack unless the user asks for
  dual-stack.  This is all gated by the "IPv6DualStack" feature gate. ([kubernetes/kubernetes#91824](https://github.com/kubernetes/kubernetes/pull/91824), [@khenidak](https://github.com/khenidak)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Add support for hugepages to downward API ([kubernetes/kubernetes#86102](https://github.com/kubernetes/kubernetes/pull/86102), [@derekwaynecarr](https://github.com/derekwaynecarr)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Adds kubelet alpha feature, `GracefulNodeShutdown` which makes kubelet aware of node system shutdowns and result in graceful termination of pods during a system shutdown. ([kubernetes/kubernetes#96129](https://github.com/kubernetes/kubernetes/pull/96129), [@bobbypage](https://github.com/bobbypage)) [SIG Node]
- AppProtocol is now GA for Endpoints and Services. The ServiceAppProtocol feature gate will be deprecated in 1.21. ([kubernetes/kubernetes#96327](https://github.com/kubernetes/kubernetes/pull/96327), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- Automatic allocation of NodePorts for services with type LoadBalancer can now be disabled by setting the (new) parameter
  Service.spec.allocateLoadBalancerNodePorts=false. The default is to allocate NodePorts for services with type LoadBalancer which is the existing behavior. ([kubernetes/kubernetes#92744](https://github.com/kubernetes/kubernetes/pull/92744), [@uablrek](https://github.com/uablrek)) [SIG Apps and Network]
- Certain fields on  Service objects will be automatically cleared when changing the service's `type` to a mode that does not need those fields.  For example, changing from type=LoadBalancer to type=ClusterIP will clear the NodePort assignments, rather than forcing the user to clear them. ([kubernetes/kubernetes#95196](https://github.com/kubernetes/kubernetes/pull/95196), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, Network and Testing]
- Document that ServiceTopology feature is required to use `service.spec.topologyKeys`. ([kubernetes/kubernetes#96528](https://github.com/kubernetes/kubernetes/pull/96528), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps]
- EndpointSlice has a new NodeName field guarded by the EndpointSliceNodeName feature gate.
  - EndpointSlice topology field will be deprecated in an upcoming release.
  - EndpointSlice "IP" address type is formally removed after being deprecated in Kubernetes 1.17.
  - The discovery.k8s.io/v1alpha1 API is deprecated and will be removed in Kubernetes 1.21. ([kubernetes/kubernetes#96440](https://github.com/kubernetes/kubernetes/pull/96440), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps and Network]
- External facing API podresources is now available under k8s.io/kubelet/pkg/apis/ ([kubernetes/kubernetes#92632](https://github.com/kubernetes/kubernetes/pull/92632), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node and Testing]
- Fewer candidates are enumerated for preemption to improve performance in large clusters. ([kubernetes/kubernetes#94814](https://github.com/kubernetes/kubernetes/pull/94814), [@adtac](https://github.com/adtac))
- Fix conversions for custom metrics. ([kubernetes/kubernetes#94481](https://github.com/kubernetes/kubernetes/pull/94481), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Instrumentation]
- GPU metrics provided by kubelet are now disabled by default. ([kubernetes/kubernetes#95184](https://github.com/kubernetes/kubernetes/pull/95184), [@RenaudWasTaken](https://github.com/RenaudWasTaken))
- If BoundServiceAccountTokenVolume is enabled, cluster admins can use metric `serviceaccount_stale_tokens_total` to monitor workloads that are depending on the extended tokens. If there are no such workloads, turn off extended tokens by starting `kube-apiserver` with flag `--service-account-extend-token-expiration=false` ([kubernetes/kubernetes#96273](https://github.com/kubernetes/kubernetes/pull/96273), [@zshihang](https://github.com/zshihang)) [SIG API Machinery and Auth]
- Introduce alpha support for exec-based container registry credential provider plugins in the kubelet. ([kubernetes/kubernetes#94196](https://github.com/kubernetes/kubernetes/pull/94196), [@andrewsykim](https://github.com/andrewsykim)) [SIG Node and Release]
- Introduces a metric source for HPAs which allows scaling based on container resource usage. ([kubernetes/kubernetes#90691](https://github.com/kubernetes/kubernetes/pull/90691), [@arjunrn](https://github.com/arjunrn)) [SIG API Machinery, Apps, Autoscaling and CLI]
- Kube-apiserver now deletes expired kube-apiserver Lease objects:
  - The feature is under feature gate `APIServerIdentity`.
  - A flag is added to kube-apiserver: `identity-lease-garbage-collection-check-period-seconds` ([kubernetes/kubernetes#95895](https://github.com/kubernetes/kubernetes/pull/95895), [@roycaihw](https://github.com/roycaihw)) [SIG API Machinery, Apps, Auth and Testing]
- Kube-controller-manager: volume plugins can be restricted from contacting local and loopback addresses by setting `--volume-host-allow-local-loopback=false`, or from contacting specific CIDR ranges by setting `--volume-host-cidr-denylist` (for example, `--volume-host-cidr-denylist=127.0.0.1/28,feed::/16`) ([kubernetes/kubernetes#91785](https://github.com/kubernetes/kubernetes/pull/91785), [@mattcary](https://github.com/mattcary)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Migrate scheduler, controller-manager and cloud-controller-manager to use LeaseLock ([kubernetes/kubernetes#94603](https://github.com/kubernetes/kubernetes/pull/94603), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps, Cloud Provider and Scheduling]
- Modify DNS-1123 error messages to indicate that RFC 1123 is not followed exactly ([kubernetes/kubernetes#94182](https://github.com/kubernetes/kubernetes/pull/94182), [@mattfenwick](https://github.com/mattfenwick)) [SIG API Machinery, Apps, Auth, Network and Node]
- Move configurable fsgroup change policy for pods to beta ([kubernetes/kubernetes#96376](https://github.com/kubernetes/kubernetes/pull/96376), [@gnufied](https://github.com/gnufied)) [SIG Apps and Storage]
- New flag is introduced, i.e. --topology-manager-scope=container|pod. 
  The default value is the "container" scope. ([kubernetes/kubernetes#92967](https://github.com/kubernetes/kubernetes/pull/92967), [@cezaryzukowski](https://github.com/cezaryzukowski)) [SIG Instrumentation, Node and Testing]
- New parameter `defaultingType` for `PodTopologySpread` plugin allows to use k8s defined or user provided default constraints ([kubernetes/kubernetes#95048](https://github.com/kubernetes/kubernetes/pull/95048), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling]
- NodeAffinity plugin can be configured with AddedAffinity. ([kubernetes/kubernetes#96202](https://github.com/kubernetes/kubernetes/pull/96202), [@alculquicondor](https://github.com/alculquicondor)) [SIG Node, Scheduling and Testing]
- Promote RuntimeClass feature to GA.
  Promote node.k8s.io API groups from v1beta1 to v1. ([kubernetes/kubernetes#95718](https://github.com/kubernetes/kubernetes/pull/95718), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Apps, Auth, Node, Scheduling and Testing]
- Reminder: The labels "failure-domain.beta.kubernetes.io/zone" and "failure-domain.beta.kubernetes.io/region" are deprecated in favor of "topology.kubernetes.io/zone" and "topology.kubernetes.io/region" respectively.  All users of the "failure-domain.beta..." labels should switch to the "topology..." equivalents. ([kubernetes/kubernetes#96033](https://github.com/kubernetes/kubernetes/pull/96033), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, CLI, Cloud Provider, Network, Node, Scheduling, Storage and Testing]
- Server Side Apply now treats LabelSelector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#93901](https://github.com/kubernetes/kubernetes/pull/93901), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Storage and Testing]
- Services will now have a `clusterIPs` field to go with `clusterIP`.  `clusterIPs[0]` is a synonym for `clusterIP` and will be synchronized on create and update operations. ([kubernetes/kubernetes#95894](https://github.com/kubernetes/kubernetes/pull/95894), [@thockin](https://github.com/thockin)) [SIG Network]
- The ServiceAccountIssuerDiscovery feature gate is now Beta and enabled by default. ([kubernetes/kubernetes#91921](https://github.com/kubernetes/kubernetes/pull/91921), [@mtaufen](https://github.com/mtaufen)) [SIG Auth]
- The status of v1beta1 CRDs without "preserveUnknownFields:false" now shows a violation, "spec.preserveUnknownFields: Invalid value: true: must be false". ([kubernetes/kubernetes#93078](https://github.com/kubernetes/kubernetes/pull/93078), [@vareti](https://github.com/vareti))
- The usage of mixed protocol values in the same LoadBalancer Service is possible if the new feature gate MixedProtocolLBService is enabled. The feature gate is disabled by default. The user has to enable it for the API Server. ([kubernetes/kubernetes#94028](https://github.com/kubernetes/kubernetes/pull/94028), [@janosi](https://github.com/janosi)) [SIG API Machinery and Apps]
- This PR will introduce a feature gate CSIServiceAccountToken with two additional fields in `CSIDriverSpec`. ([kubernetes/kubernetes#93130](https://github.com/kubernetes/kubernetes/pull/93130), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Users can try the CronJob controller v2 using the feature gate. This will be the default controller in future releases. ([kubernetes/kubernetes#93370](https://github.com/kubernetes/kubernetes/pull/93370), [@alaypatel07](https://github.com/alaypatel07)) [SIG API Machinery, Apps, Auth and Testing]
- VolumeSnapshotDataSource moves to GA in 1.20 release ([kubernetes/kubernetes#95282](https://github.com/kubernetes/kubernetes/pull/95282), [@xing-yang](https://github.com/xing-yang)) [SIG Apps]
- WinOverlay feature graduated to beta ([kubernetes/kubernetes#94807](https://github.com/kubernetes/kubernetes/pull/94807), [@ksubrmnn](https://github.com/ksubrmnn)) [SIG Windows]
- API priority and fairness graduated to beta
  1.19 servers with APF turned on should not be run in a multi-server cluster with 1.20+ servers. ([kubernetes/kubernetes#96527](https://github.com/kubernetes/kubernetes/pull/96527), [@adtac](https://github.com/adtac)) [SIG API Machinery and Testing]
- Add LoadBalancerIPMode feature gate ([kubernetes/kubernetes#92312](https://github.com/kubernetes/kubernetes/pull/92312), [@Sh4d1](https://github.com/Sh4d1)) [SIG Apps, CLI, Cloud Provider and Network]
- Add WindowsContainerResources and Annotations to CRI-API UpdateContainerResourcesRequest ([kubernetes/kubernetes#95741](https://github.com/kubernetes/kubernetes/pull/95741), [@katiewasnothere](https://github.com/katiewasnothere)) [SIG Node]
- Add a 'serving' and `terminating` condition to the EndpointSlice API.
  
  `serving` tracks the readiness of endpoints regardless of their terminating state. This is distinct from `ready` since `ready` is only true when pods are not terminating. 
  `terminating` is true when an endpoint is terminating. For pods this is any endpoint with a deletion timestamp. ([kubernetes/kubernetes#92968](https://github.com/kubernetes/kubernetes/pull/92968), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps and Network]
- Add support for hugepages to downward API ([kubernetes/kubernetes#86102](https://github.com/kubernetes/kubernetes/pull/86102), [@derekwaynecarr](https://github.com/derekwaynecarr)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Adds kubelet alpha feature, `GracefulNodeShutdown` which makes kubelet aware of node system shutdowns and result in graceful termination of pods during a system shutdown. ([kubernetes/kubernetes#96129](https://github.com/kubernetes/kubernetes/pull/96129), [@bobbypage](https://github.com/bobbypage)) [SIG Node]
- AppProtocol is now GA for Endpoints and Services. The ServiceAppProtocol feature gate will be deprecated in 1.21. ([kubernetes/kubernetes#96327](https://github.com/kubernetes/kubernetes/pull/96327), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- Automatic allocation of NodePorts for services with type LoadBalancer can now be disabled by setting the (new) parameter
  Service.spec.allocateLoadBalancerNodePorts=false. The default is to allocate NodePorts for services with type LoadBalancer which is the existing behavior. ([kubernetes/kubernetes#92744](https://github.com/kubernetes/kubernetes/pull/92744), [@uablrek](https://github.com/uablrek)) [SIG Apps and Network]
- Document that ServiceTopology feature is required to use `service.spec.topologyKeys`. ([kubernetes/kubernetes#96528](https://github.com/kubernetes/kubernetes/pull/96528), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps]
- EndpointSlice has a new NodeName field guarded by the EndpointSliceNodeName feature gate.
  - EndpointSlice topology field will be deprecated in an upcoming release.
  - EndpointSlice "IP" address type is formally removed after being deprecated in Kubernetes 1.17.
  - The discovery.k8s.io/v1alpha1 API is deprecated and will be removed in Kubernetes 1.21. ([kubernetes/kubernetes#96440](https://github.com/kubernetes/kubernetes/pull/96440), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps and Network]
- Fewer candidates are enumerated for preemption to improve performance in large clusters ([kubernetes/kubernetes#94814](https://github.com/kubernetes/kubernetes/pull/94814), [@adtac](https://github.com/adtac)) [SIG Scheduling]
- If BoundServiceAccountTokenVolume is enabled, cluster admins can use metric `serviceaccount_stale_tokens_total` to monitor workloads that are depending on the extended tokens. If there are no such workloads, turn off extended tokens by starting `kube-apiserver` with flag `--service-account-extend-token-expiration=false` ([kubernetes/kubernetes#96273](https://github.com/kubernetes/kubernetes/pull/96273), [@zshihang](https://github.com/zshihang)) [SIG API Machinery and Auth]
- Introduce alpha support for exec-based container registry credential provider plugins in the kubelet. ([kubernetes/kubernetes#94196](https://github.com/kubernetes/kubernetes/pull/94196), [@andrewsykim](https://github.com/andrewsykim)) [SIG Node and Release]
- Kube-apiserver now deletes expired kube-apiserver Lease objects:
  - The feature is under feature gate `APIServerIdentity`.
  - A flag is added to kube-apiserver: `identity-lease-garbage-collection-check-period-seconds` ([kubernetes/kubernetes#95895](https://github.com/kubernetes/kubernetes/pull/95895), [@roycaihw](https://github.com/roycaihw)) [SIG API Machinery, Apps, Auth and Testing]
- Move configurable fsgroup change policy for pods to beta ([kubernetes/kubernetes#96376](https://github.com/kubernetes/kubernetes/pull/96376), [@gnufied](https://github.com/gnufied)) [SIG Apps and Storage]
- New flag is introduced, i.e. --topology-manager-scope=container|pod. 
  The default value is the "container" scope. ([kubernetes/kubernetes#92967](https://github.com/kubernetes/kubernetes/pull/92967), [@cezaryzukowski](https://github.com/cezaryzukowski)) [SIG Instrumentation, Node and Testing]
- NodeAffinity plugin can be configured with AddedAffinity. ([kubernetes/kubernetes#96202](https://github.com/kubernetes/kubernetes/pull/96202), [@alculquicondor](https://github.com/alculquicondor)) [SIG Node, Scheduling and Testing]
- Promote RuntimeClass feature to GA.
  Promote node.k8s.io API groups from v1beta1 to v1. ([kubernetes/kubernetes#95718](https://github.com/kubernetes/kubernetes/pull/95718), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Apps, Auth, Node, Scheduling and Testing]
- Reminder: The labels "failure-domain.beta.kubernetes.io/zone" and "failure-domain.beta.kubernetes.io/region" are deprecated in favor of "topology.kubernetes.io/zone" and "topology.kubernetes.io/region" respectively.  All users of the "failure-domain.beta..." labels should switch to the "topology..." equivalents. ([kubernetes/kubernetes#96033](https://github.com/kubernetes/kubernetes/pull/96033), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, CLI, Cloud Provider, Network, Node, Scheduling, Storage and Testing]
- The usage of mixed protocol values in the same LoadBalancer Service is possible if the new feature gate MixedProtocolLBSVC is enabled.
  "action required"
  The feature gate is disabled by default. The user has to enable it for the API Server. ([kubernetes/kubernetes#94028](https://github.com/kubernetes/kubernetes/pull/94028), [@janosi](https://github.com/janosi)) [SIG API Machinery and Apps]
- This PR will introduce a feature gate CSIServiceAccountToken with two additional fields in `CSIDriverSpec`. ([kubernetes/kubernetes#93130](https://github.com/kubernetes/kubernetes/pull/93130), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Users can try the CronJob controller v2 using the feature gate. This will be the default controller in future releases. ([kubernetes/kubernetes#93370](https://github.com/kubernetes/kubernetes/pull/93370), [@alaypatel07](https://github.com/alaypatel07)) [SIG API Machinery, Apps, Auth and Testing]
- VolumeSnapshotDataSource moves to GA in 1.20 release ([kubernetes/kubernetes#95282](https://github.com/kubernetes/kubernetes/pull/95282), [@xing-yang](https://github.com/xing-yang)) [SIG Apps]
- + `TokenRequest` and `TokenRequestProjection` features have been promoted to GA. This feature allows generating service account tokens that are not visible in Secret objects and are tied to the lifetime of a Pod object. See https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection for details on configuring and using this feature. The `TokenRequest` and `TokenRequestProjection` feature gates will be removed in v1.21.
  + kubeadm's kube-apiserver Pod manifest now includes the following flags by default "--service-account-key-file", "--service-account-signing-key-file", "--service-account-issuer". ([kubernetes/kubernetes#93258](https://github.com/kubernetes/kubernetes/pull/93258), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle, Storage and Testing]
- Certain fields on  Service objects will be automatically cleared when changing the service's `type` to a mode that does not need those fields.  For example, changing from type=LoadBalancer to type=ClusterIP will clear the NodePort assignments, rather than forcing the user to clear them. ([kubernetes/kubernetes#95196](https://github.com/kubernetes/kubernetes/pull/95196), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, Network and Testing]
- Services will now have a `clusterIPs` field to go with `clusterIP`.  `clusterIPs[0]` is a synonym for `clusterIP` and will be synchronized on create and update operations. ([kubernetes/kubernetes#95894](https://github.com/kubernetes/kubernetes/pull/95894), [@thockin](https://github.com/thockin)) [SIG Network]
- Add dual-stack Services (alpha).  This is a BREAKING CHANGE to an alpha API.
  It changes the dual-stack API wrt Service from a single ipFamily field to 3
  fields: ipFamilyPolicy (SingleStack, PreferDualStack, RequireDualStack),
  ipFamilies (a list of families assigned), and clusterIPs (inclusive of
  clusterIP).  Most users do not need to set anything at all, defaulting will
  handle it for them.  Services are single-stack unless the user asks for
  dual-stack.  This is all gated by the "IPv6DualStack" feature gate. ([kubernetes/kubernetes#91824](https://github.com/kubernetes/kubernetes/pull/91824), [@khenidak](https://github.com/khenidak)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Introduces a metric source for HPAs which allows scaling based on container resource usage. ([kubernetes/kubernetes#90691](https://github.com/kubernetes/kubernetes/pull/90691), [@arjunrn](https://github.com/arjunrn)) [SIG API Machinery, Apps, Autoscaling and CLI]
- New parameter `defaultingType` for `PodTopologySpread` plugin allows to use k8s defined or user-provided default constraints ([kubernetes/kubernetes#95048](https://github.com/kubernetes/kubernetes/pull/95048), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling]
- GPU metrics provided by kubelet are now disabled by default ([kubernetes/kubernetes#95184](https://github.com/kubernetes/kubernetes/pull/95184), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- New parameter `defaultingType` for `PodTopologySpread` plugin allows to use k8s defined or user provided default constraints ([kubernetes/kubernetes#95048](https://github.com/kubernetes/kubernetes/pull/95048), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling]
- Server Side Apply now treats LabelSelector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#93901](https://github.com/kubernetes/kubernetes/pull/93901), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Storage and Testing]
- Status of v1beta1 CRDs without "preserveUnknownFields:false" will show violation "spec.preserveUnknownFields: Invalid value: true: must be false" ([kubernetes/kubernetes#93078](https://github.com/kubernetes/kubernetes/pull/93078), [@vareti](https://github.com/vareti)) [SIG API Machinery]
- A new `nofuzz` go build tag now disables gofuzz support. Release binaries enable this. ([kubernetes/kubernetes#92491](https://github.com/kubernetes/kubernetes/pull/92491), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery]
- A new alpha-level field, `SupportsFsGroup`, has been introduced for CSIDrivers to allow them to specify whether they support volume ownership and permission modifications. The `CSIVolumeSupportFSGroup` feature gate must be enabled to allow this field to be used. ([kubernetes/kubernetes#92001](https://github.com/kubernetes/kubernetes/pull/92001), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, CLI and Storage]
- Added pod version skew strategy for seccomp profile to synchronize the deprecated annotations with the new API Server fields. Please see the corresponding section [in the KEP](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/135-seccomp/README.md#version-skew-strategy) for more detailed explanations. ([kubernetes/kubernetes#91408](https://github.com/kubernetes/kubernetes/pull/91408), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps, Auth, CLI and Node]
- Adds the ability to disable Accelerator/GPU metrics collected by Kubelet ([kubernetes/kubernetes#91930](https://github.com/kubernetes/kubernetes/pull/91930), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- Custom Endpoints are now mirrored to EndpointSlices by a new EndpointSliceMirroring controller. ([kubernetes/kubernetes#91637](https://github.com/kubernetes/kubernetes/pull/91637), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Cloud Provider, Instrumentation, Network and Testing]
- External facing API podresources is now available under k8s.io/kubelet/pkg/apis/ ([kubernetes/kubernetes#92632](https://github.com/kubernetes/kubernetes/pull/92632), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node and Testing]
- Fix conversions for custom metrics. ([kubernetes/kubernetes#94481](https://github.com/kubernetes/kubernetes/pull/94481), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Instrumentation]
- Generic ephemeral volumes, a new alpha feature under the `GenericEphemeralVolume` feature gate, provide a more flexible alternative to `EmptyDir` volumes: as with `EmptyDir`, volumes are created and deleted for each pod automatically by Kubernetes. But because the normal provisioning process is used (`PersistentVolumeClaim`), storage can be provided by third-party storage vendors and all of the usual volume features work. Volumes don't need to be empty; for example, restoring from snapshot is supported. ([kubernetes/kubernetes#92784](https://github.com/kubernetes/kubernetes/pull/92784), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Scheduling, Storage and Testing]
- Kube-controller-manager: volume plugins can be restricted from contacting local and loopback addresses by setting `--volume-host-allow-local-loopback=false`, or from contacting specific CIDR ranges by setting `--volume-host-cidr-denylist` (for example, `--volume-host-cidr-denylist=127.0.0.1/28,feed::/16`) ([kubernetes/kubernetes#91785](https://github.com/kubernetes/kubernetes/pull/91785), [@mattcary](https://github.com/mattcary)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Kubernetes is now built with golang 1.15.0-rc.1.
  - The deprecated, legacy behavior of treating the CommonName field on X.509 serving certificates as a host name when no Subject Alternative Names are present is now disabled by default. It can be temporarily re-enabled by adding the value x509ignoreCN=0 to the GODEBUG environment variable. ([kubernetes/kubernetes#93264](https://github.com/kubernetes/kubernetes/pull/93264), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Storage and Testing]
- Migrate scheduler, controller-manager and cloud-controller-manager to use LeaseLock ([kubernetes/kubernetes#94603](https://github.com/kubernetes/kubernetes/pull/94603), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps, Cloud Provider and Scheduling]
- Modify DNS-1123 error messages to indicate that RFC 1123 is not followed exactly ([kubernetes/kubernetes#94182](https://github.com/kubernetes/kubernetes/pull/94182), [@mattfenwick](https://github.com/mattfenwick)) [SIG API Machinery, Apps, Auth, Network and Node]
- The ServiceAccountIssuerDiscovery feature gate is now Beta and enabled by default. ([kubernetes/kubernetes#91921](https://github.com/kubernetes/kubernetes/pull/91921), [@mtaufen](https://github.com/mtaufen)) [SIG Auth]
- The kube-controller-manager managed signers can now have distinct signing certificates and keys.  See the help about `--cluster-signing-[signer-name]-{cert,key}-file`.  `--cluster-signing-{cert,key}-file` is still the default. ([kubernetes/kubernetes#90822](https://github.com/kubernetes/kubernetes/pull/90822), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Apps and Auth]
- When creating a networking.k8s.io/v1 Ingress API object, `spec.tls[*].secretName` values are required to pass validation rules for Secret API object names. ([kubernetes/kubernetes#93929](https://github.com/kubernetes/kubernetes/pull/93929), [@liggitt](https://github.com/liggitt)) [SIG Network]
- WinOverlay feature graduated to beta ([kubernetes/kubernetes#94807](https://github.com/kubernetes/kubernetes/pull/94807), [@ksubrmnn](https://github.com/ksubrmnn)) [SIG Windows]

# v19.15.1

* fix: watch returns `raw_object` if detection of returned objects fail ([#177](https://github.com/tomplus/kubernetes_asyncio/pull/177), [@tomplus](https://github.com/tomplus))

# v19.15.0

* feat: Kubernetes API Version: v1.19.15

### API Change
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#101113](https://github.com/kubernetes/kubernetes/pull/101113), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]
- Fixes using server-side apply with APIService resources ([kubernetes/kubernetes#100713](https://github.com/kubernetes/kubernetes/pull/100713), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Apps, Scheduling and Testing]
- Regenerate protobuf code to fix CVE-2021-3121 ([kubernetes/kubernetes#100515](https://github.com/kubernetes/kubernetes/pull/100515), [@joelsmith](https://github.com/joelsmith)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node and Storage]
- Kubernetes is now built using go1.15.8 ([kubernetes/kubernetes#99093](https://github.com/kubernetes/kubernetes/pull/99093), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Release and Testing]
- Fix conversions for custom metrics. ([kubernetes/kubernetes#94654](https://github.com/kubernetes/kubernetes/pull/94654), [@wojtek-t](https://github.com/wojtek-t)) [SIG Instrumentation]
- A new alpha-level field, `SupportsFsGroup`, has been introduced for CSIDrivers to allow them to specify whether they support volume ownership and permission modifications. The `CSIVolumeSupportFSGroup` feature gate must be enabled to allow this field to be used. ([kubernetes/kubernetes#92001](https://github.com/kubernetes/kubernetes/pull/92001), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, CLI and Storage]
- Added pod version skew strategy for seccomp profile to synchronize the deprecated annotations with the new API Server fields. Please see the corresponding section [in the KEP](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/135-seccomp/README.md#version-skew-strategy) for more detailed explanations. ([kubernetes/kubernetes#91408](https://github.com/kubernetes/kubernetes/pull/91408), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps, Auth, CLI and Node]
- Adds the ability to disable Accelerator/GPU metrics collected by Kubelet ([kubernetes/kubernetes#91930](https://github.com/kubernetes/kubernetes/pull/91930), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- Admission webhooks can now return warning messages that are surfaced to API clients, using the `.response.warnings` field in the admission review response. ([kubernetes/kubernetes#92667](https://github.com/kubernetes/kubernetes/pull/92667), [@liggitt](https://github.com/liggitt)) [SIG API Machinery and Testing]
- CertificateSigningRequest API conditions were updated:
  - a `status` field was added; this field defaults to `True`, and may only be set to `True` for `Approved`, `Denied`, and `Failed` conditions
  - a `lastTransitionTime` field was added
  - a `Failed` condition type was added to allow signers to indicate permanent failure; this condition can be added via the `certificatesigningrequests/status` subresource.
  - `Approved` and `Denied` conditions are mutually exclusive
  - `Approved`, `Denied`, and `Failed` conditions can no longer be removed from a CSR ([kubernetes/kubernetes#90191](https://github.com/kubernetes/kubernetes/pull/90191), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Auth, CLI and Node]
- Cluster admins can now turn off /logs endpoint in kubelet by setting enableSystemLogHandler to false in their kubelet configuration file. enableSystemLogHandler can be set to true only when enableDebuggingHandlers is also set to true. ([kubernetes/kubernetes#87273](https://github.com/kubernetes/kubernetes/pull/87273), [@SaranBalaji90](https://github.com/SaranBalaji90)) [SIG Node]
- Custom Endpoints are now mirrored to EndpointSlices by a new EndpointSliceMirroring controller. ([kubernetes/kubernetes#91637](https://github.com/kubernetes/kubernetes/pull/91637), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Cloud Provider, Instrumentation, Network and Testing]
- CustomResourceDefinitions added support for marking versions as deprecated by setting `spec.versions[*].deprecated` to `true`, and for optionally overriding the default deprecation warning with a `spec.versions[*].deprecationWarning` field. ([kubernetes/kubernetes#92329](https://github.com/kubernetes/kubernetes/pull/92329), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]
- EnvVarSource api doc bug fixes ([kubernetes/kubernetes#91194](https://github.com/kubernetes/kubernetes/pull/91194), [@wawa0210](https://github.com/wawa0210)) [SIG Apps]
- Fix bug in reflector that couldn't recover from "Too large resource version" errors ([kubernetes/kubernetes#92537](https://github.com/kubernetes/kubernetes/pull/92537), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([kubernetes/kubernetes#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- Generic ephemeral volumes, a new alpha feature under the `GenericEphemeralVolume` feature gate, provide a more flexible alternative to `EmptyDir` volumes: as with `EmptyDir`, volumes are created and deleted for each pod automatically by Kubernetes. But because the normal provisioning process is used (`PersistentVolumeClaim`), storage can be provided by third-party storage vendors and all of the usual volume features work. Volumes don't need to be empt; for example, restoring from snapshot is supported. ([kubernetes/kubernetes#92784](https://github.com/kubernetes/kubernetes/pull/92784), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Scheduling, Storage and Testing]
- Go1.14.4 is now the minimum version required for building Kubernetes ([kubernetes/kubernetes#92438](https://github.com/kubernetes/kubernetes/pull/92438), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Storage and Testing]
- Hide managedFields from kubectl edit command ([kubernetes/kubernetes#91946](https://github.com/kubernetes/kubernetes/pull/91946), [@soltysh](https://github.com/soltysh)) [SIG CLI]
- K8s.io/apimachinery - scheme.Convert() now uses only explicitly registered conversions - default reflection based conversion is no longer available. `+k8s:conversion-gen` tags can be used with the `k8s.io/code-generator` component to generate conversions. ([kubernetes/kubernetes#90018](https://github.com/kubernetes/kubernetes/pull/90018), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps and Testing]
- Kube-proxy: add `--bind-address-hard-fail` flag to treat failure to bind to a port as fatal ([kubernetes/kubernetes#89350](https://github.com/kubernetes/kubernetes/pull/89350), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle and Network]
- Kubebuilder validation tags are set on metav1.Condition for CRD generation ([kubernetes/kubernetes#92660](https://github.com/kubernetes/kubernetes/pull/92660), [@damemi](https://github.com/damemi)) [SIG API Machinery]
- Kubelet's --runonce option is now also available in Kubelet's config file as `runOnce`. ([kubernetes/kubernetes#89128](https://github.com/kubernetes/kubernetes/pull/89128), [@vincent178](https://github.com/vincent178)) [SIG Node]
- Kubelet: add '--logging-format' flag to support structured logging ([kubernetes/kubernetes#91532](https://github.com/kubernetes/kubernetes/pull/91532), [@afrouzMashaykhi](https://github.com/afrouzMashaykhi)) [SIG API Machinery, Cluster Lifecycle, Instrumentation and Node]
- Kubernetes is now built with golang 1.15.0-rc.1.
  - The deprecated, legacy behavior of treating the CommonName field on X.509 serving certificates as a host name when no Subject Alternative Names are present is now disabled by default. It can be temporarily re-enabled by adding the value x509ignoreCN=0 to the GODEBUG environment variable. ([kubernetes/kubernetes#93264](https://github.com/kubernetes/kubernetes/pull/93264), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Storage and Testing]
- Promote Immutable Secrets/ConfigMaps feature to Beta and enable the feature by default.
  This allows to set `Immutable` field in Secrets or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#89594](https://github.com/kubernetes/kubernetes/pull/89594), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps and Testing]
- Remove `BindTimeoutSeconds` from schedule configuration `KubeSchedulerConfiguration` ([kubernetes/kubernetes#91580](https://github.com/kubernetes/kubernetes/pull/91580), [@cofyc](https://github.com/cofyc)) [SIG Scheduling and Testing]
- Remove kubescheduler.config.k8s.io/v1alpha1 ([kubernetes/kubernetes#89298](https://github.com/kubernetes/kubernetes/pull/89298), [@gavinfish](https://github.com/gavinfish)) [SIG Scheduling]
- Reserve plugins that fail to reserve will trigger the unreserve extension point ([kubernetes/kubernetes#92391](https://github.com/kubernetes/kubernetes/pull/92391), [@adtac](https://github.com/adtac)) [SIG Scheduling and Testing]
- Resolve regression in `metadata.managedFields` handling in update/patch requests submitted by older API clients ([kubernetes/kubernetes#91748](https://github.com/kubernetes/kubernetes/pull/91748), [@apelisse](https://github.com/apelisse))
- Scheduler: optionally check for available storage capacity before scheduling pods which have unbound volumes (alpha feature with the new `CSIStorageCapacity` feature gate, only works for CSI drivers and depends on support for the feature in a CSI driver deployment) ([kubernetes/kubernetes#92387](https://github.com/kubernetes/kubernetes/pull/92387), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Scheduling, Storage and Testing]
- Seccomp support has graduated to GA. A new `seccompProfile` field is added to pod and container securityContext objects. Support for `seccomp.security.alpha.kubernetes.io/pod` and `container.seccomp.security.alpha.kubernetes.io/...` annotations is deprecated, and will be removed in v1.22. ([kubernetes/kubernetes#91381](https://github.com/kubernetes/kubernetes/pull/91381), [@pjbgf](https://github.com/pjbgf)) [SIG Apps, Auth, Node, Release, Scheduling and Testing]
- ServiceAppProtocol feature gate is now beta and enabled by default, adding new AppProtocol field to Services and Endpoints. ([kubernetes/kubernetes#90023](https://github.com/kubernetes/kubernetes/pull/90023), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- SetHostnameAsFQDN is a new field in PodSpec. When set to true, the fully 
  qualified domain name (FQDN) of a Pod is set as hostname of its containers. 
  In Linux containers, this means setting the FQDN in the hostname field of the 
  kernel (the nodename field of struct utsname).  In Windows containers, this
  means setting the this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters to FQDN. 
  If a pod does not have FQDN, this has no effect. ([kubernetes/kubernetes#91699](https://github.com/kubernetes/kubernetes/pull/91699), [@javidiaz](https://github.com/javidiaz)) [SIG Apps, Network, Node and Testing]
- The CertificateSigningRequest API is promoted to certificates.k8s.io/v1 with the following changes:
  - `spec.signerName` is now required, and requests for `kubernetes.io/legacy-unknown` are not allowed to be created via the `certificates.k8s.io/v1` API
  - `spec.usages` is now required, may not contain duplicate values, and must only contain known usages
  - `status.conditions` may not contain duplicate types
  - `status.conditions[*].status` is now required
  - `status.certificate` must be PEM-encoded, and contain only CERTIFICATE blocks ([kubernetes/kubernetes#91685](https://github.com/kubernetes/kubernetes/pull/91685), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Architecture, Auth, CLI and Testing]
- The HugePageStorageMediumSize feature gate is now on by default allowing usage of multiple sizes huge page resources on a container level. ([kubernetes/kubernetes#90592](https://github.com/kubernetes/kubernetes/pull/90592), [@bart0sh](https://github.com/bart0sh)) [SIG Node]
- The Kubelet's --node-status-max-images option is now available via the Kubelet config file field nodeStatusMaxImage ([kubernetes/kubernetes#91275](https://github.com/kubernetes/kubernetes/pull/91275), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's --seccomp-profile-root option is now marked as deprecated. ([kubernetes/kubernetes#91182](https://github.com/kubernetes/kubernetes/pull/91182), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--bootstrap-checkpoint-path` option is now removed. ([kubernetes/kubernetes#91577](https://github.com/kubernetes/kubernetes/pull/91577), [@knabben](https://github.com/knabben)) [SIG Apps and Node]
- The Kubelet's `--cloud-provider` and `--cloud-config` options are now marked as deprecated. ([kubernetes/kubernetes#90408](https://github.com/kubernetes/kubernetes/pull/90408), [@knabben](https://github.com/knabben)) [SIG Cloud Provider and Node]
- The Kubelet's `--enable-server` and `--provider-id` option is now available via the Kubelet config file field `enableServer` and `providerID` respectively. ([kubernetes/kubernetes#90494](https://github.com/kubernetes/kubernetes/pull/90494), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--kernel-memcg-notification` option is now available via the Kubelet config file field kernelMemcgNotification ([kubernetes/kubernetes#91863](https://github.com/kubernetes/kubernetes/pull/91863), [@knabben](https://github.com/knabben)) [SIG Cloud Provider, Node and Testing]
- The Kubelet's `--really-crash-for-testing` and  `--chaos-chance` options are now marked as deprecated. ([kubernetes/kubernetes#90499](https://github.com/kubernetes/kubernetes/pull/90499), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--volume-plugin-dir` option is now available via the Kubelet config file field `VolumePluginDir`. ([kubernetes/kubernetes#88480](https://github.com/kubernetes/kubernetes/pull/88480), [@savitharaghunathan](https://github.com/savitharaghunathan)) [SIG Node]
- The `DefaultIngressClass` feature is now GA. The `--feature-gate` parameter will be removed in 1.20. ([kubernetes/kubernetes#91957](https://github.com/kubernetes/kubernetes/pull/91957), [@cmluciano](https://github.com/cmluciano)) [SIG API Machinery, Apps, Network and Testing]
- The alpha `DynamicAuditing` feature gate and `auditregistration.k8s.io/v1alpha1` API have been removed and are no longer supported. ([kubernetes/kubernetes#91502](https://github.com/kubernetes/kubernetes/pull/91502), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Auth and Testing]
- The kube-controller-manager managed signers can now have distinct signing certificates and keys.  See the help about `--cluster-signing-[signer-name]-{cert,key}-file`.  `--cluster-signing-{cert,key}-file` is still the default. ([kubernetes/kubernetes#90822](https://github.com/kubernetes/kubernetes/pull/90822), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Apps and Auth]
- The unused `series.state` field, deprecated since v1.14, is removed from the `events.k8s.io/v1beta1` and `v1` Event types. ([kubernetes/kubernetes#90449](https://github.com/kubernetes/kubernetes/pull/90449), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps]
- Unreserve extension point for scheduler plugins is merged into Reserve extension point ([kubernetes/kubernetes#92200](https://github.com/kubernetes/kubernetes/pull/92200), [@adtac](https://github.com/adtac)) [SIG Scheduling and Testing]
- Update Golang to v1.14.4 ([kubernetes/kubernetes#88638](https://github.com/kubernetes/kubernetes/pull/88638), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Cloud Provider, Release and Testing]
- Updated the API documentation for Service.Spec.IPFamily to warn that its exact
  semantics will probably change before the dual-stack feature goes GA, and users
  should look at ClusterIP or Endpoints, not IPFamily, to figure out if an existing
  Service is IPv4, IPv6, or dual-stack. ([kubernetes/kubernetes#91527](https://github.com/kubernetes/kubernetes/pull/91527), [@danwinship](https://github.com/danwinship)) [SIG Apps and Network]
- Users can configure a resource prefix to ignore a group of resources. ([kubernetes/kubernetes#88842](https://github.com/kubernetes/kubernetes/pull/88842), [@angao](https://github.com/angao)) [SIG Node and Scheduling]
- `Ingress` and `IngressClass` resources have graduated to `networking.k8s.io/v1`. Ingress and IngressClass types in the `extensions/v1beta1` and `networking.k8s.io/v1beta1` API versions are deprecated and will no longer be served in 1.22+. Persisted objects can be accessed via the `networking.k8s.io/v1` API. Notable changes in v1 Ingress objects (v1beta1 field names are unchanged):
  - `spec.backend` -> `spec.defaultBackend`
  - `serviceName` -> `service.name`
  - `servicePort` -> `service.port.name` (for string values)
  - `servicePort` -> `service.port.number` (for numeric values)
  - `pathType` no longer has a default value in v1; "Exact", "Prefix", or "ImplementationSpecific" must be specified
  Other Ingress API updates:
  - backends can now be resource or service backends
  - `path` is no longer required to be a valid regular expression ([kubernetes/kubernetes#89778](https://github.com/kubernetes/kubernetes/pull/89778), [@cmluciano](https://github.com/cmluciano)) [SIG API Machinery, Apps, CLI, Network and Testing]
- `NodeResourcesLeastAllocated` and `NodeResourcesMostAllocated` plugins now support customized weight on the CPU and memory. ([kubernetes/kubernetes#90544](https://github.com/kubernetes/kubernetes/pull/90544), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- `PostFilter` type is added to scheduler component config API on version v1beta1. ([kubernetes/kubernetes#91547](https://github.com/kubernetes/kubernetes/pull/91547), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- `RequestedToCapacityRatioArgs` encoding is now strict ([kubernetes/kubernetes#91603](https://github.com/kubernetes/kubernetes/pull/91603), [@pancernik](https://github.com/pancernik)) [SIG Scheduling]
- `v1beta1` Scheduler `Extender` encoding is case-sensitive (`v1alpha1`/`v1alpha2` was case-insensitive), its `httpTimeout` field uses duration encoding (for example, one second is specified as `"1s"`), and the `enableHttps` field in `v1alpha1`/`v1alpha2` was renamed to `enableHTTPS`. ([kubernetes/kubernetes#91625](https://github.com/kubernetes/kubernetes/pull/91625), [@pancernik](https://github.com/pancernik)) [SIG Scheduling]
- Adds the ability to disable Accelerator/GPU metrics collected by Kubelet ([kubernetes/kubernetes#91930](https://github.com/kubernetes/kubernetes/pull/91930), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- Kubernetes is now built with golang 1.15.0-rc.1.
  - The deprecated, legacy behavior of treating the CommonName field on X.509 serving certificates as a host name when no Subject Alternative Names are present is now disabled by default. It can be temporarily re-enabled by adding the value x509ignoreCN=0 to the GODEBUG environment variable. ([kubernetes/kubernetes#93264](https://github.com/kubernetes/kubernetes/pull/93264), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Storage and Testing]
- A new alpha-level field, `SupportsFsGroup`, has been introduced for CSIDrivers to allow them to specify whether they support volume ownership and permission modifications. The `CSIVolumeSupportFSGroup` feature gate must be enabled to allow this field to be used. ([kubernetes/kubernetes#92001](https://github.com/kubernetes/kubernetes/pull/92001), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, CLI and Storage]
- The kube-controller-manager managed signers can now have distinct signing certificates and keys.  See the help about `--cluster-signing-[signer-name]-{cert,key}-file`.  `--cluster-signing-{cert,key}-file` is still the default. ([kubernetes/kubernetes#90822](https://github.com/kubernetes/kubernetes/pull/90822), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Apps and Auth]
- Added pod version skew strategy for seccomp profile to synchronize the deprecated annotations with the new API Server fields. Please see the corresponding section [in the KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/135-seccomp#version-skew-strategy) for more detailed explanations. ([kubernetes/kubernetes#91408](https://github.com/kubernetes/kubernetes/pull/91408), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps, Auth, CLI and Node]
- Custom Endpoints are now mirrored to EndpointSlices by a new EndpointSliceMirroring controller. ([kubernetes/kubernetes#91637](https://github.com/kubernetes/kubernetes/pull/91637), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Cloud Provider, Instrumentation, Network and Testing]
- Generic ephemeral volumes, a new alpha feature under the `GenericEphemeralVolume` feature gate, provide a more flexible alternative to `EmptyDir` volumes: as with `EmptyDir`, volumes are created and deleted for each pod automatically by Kubernetes. But because the normal provisioning process is used (`PersistentVolumeClaim`), storage can be provided by third-party storage vendors and all of the usual volume features work. Volumes don't need to be empt; for example, restoring from snapshot is supported. ([kubernetes/kubernetes#92784](https://github.com/kubernetes/kubernetes/pull/92784), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Scheduling, Storage and Testing]
- Remove `BindTimeoutSeconds` from schedule configuration `KubeSchedulerConfiguration` ([kubernetes/kubernetes#91580](https://github.com/kubernetes/kubernetes/pull/91580), [@cofyc](https://github.com/cofyc)) [SIG Scheduling and Testing]
- Resolve regression in metadata.managedFields handling in update/patch requests submitted by older API clients ([kubernetes/kubernetes#91748](https://github.com/kubernetes/kubernetes/pull/91748), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- The CertificateSigningRequest API is promoted to certificates.k8s.io/v1 with the following changes:
  - `spec.signerName` is now required, and requests for `kubernetes.io/legacy-unknown` are not allowed to be created via the `certificates.k8s.io/v1` API
  - `spec.usages` is now required, may not contain duplicate values, and must only contain known usages
  - `status.conditions` may not contain duplicate types
  - `status.conditions[*].status` is now required
  - `status.certificate` must be PEM-encoded, and contain only CERTIFICATE blocks ([kubernetes/kubernetes#91685](https://github.com/kubernetes/kubernetes/pull/91685), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Architecture, Auth, CLI and Testing]
- The Kubelet's `--cloud-provider` and `--cloud-config` options are now marked as deprecated. ([kubernetes/kubernetes#90408](https://github.com/kubernetes/kubernetes/pull/90408), [@knabben](https://github.com/knabben)) [SIG Cloud Provider and Node]
- CertificateSigningRequest API conditions were updated:
  - a `status` field was added; this field defaults to `True`, and may only be set to `True` for `Approved`, `Denied`, and `Failed` conditions
  - a `lastTransitionTime` field was added
  - a `Failed` condition type was added to allow signers to indicate permanent failure; this condition can be added via the `certificatesigningrequests/status` subresource.
  - `Approved` and `Denied` conditions are mutually exclusive
  - `Approved`, `Denied`, and `Failed` conditions can no longer be removed from a CSR ([kubernetes/kubernetes#90191](https://github.com/kubernetes/kubernetes/pull/90191), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Auth, CLI and Node]
- EnvVarSource api doc bug fixes ([kubernetes/kubernetes#91194](https://github.com/kubernetes/kubernetes/pull/91194), [@wawa0210](https://github.com/wawa0210)) [SIG Apps]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([kubernetes/kubernetes#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- The Kubelet's --node-status-max-images option is now available via the Kubelet config file field nodeStatusMaxImage ([kubernetes/kubernetes#91275](https://github.com/kubernetes/kubernetes/pull/91275), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's --seccomp-profile-root option is now available via the Kubelet config file field seccompProfileRoot. ([kubernetes/kubernetes#91182](https://github.com/kubernetes/kubernetes/pull/91182), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--enable-server` and `--provider-id` option is now available via the Kubelet config file field `enableServer` and `providerID` respectively. ([kubernetes/kubernetes#90494](https://github.com/kubernetes/kubernetes/pull/90494), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--really-crash-for-testing` and  `--chaos-chance` options are now marked as deprecated. ([kubernetes/kubernetes#90499](https://github.com/kubernetes/kubernetes/pull/90499), [@knabben](https://github.com/knabben)) [SIG Node]
- The alpha `DynamicAuditing` feature gate and `auditregistration.k8s.io/v1alpha1` API have been removed and are no longer supported. ([kubernetes/kubernetes#91502](https://github.com/kubernetes/kubernetes/pull/91502), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Auth and Testing]
- `NodeResourcesLeastAllocated` and `NodeResourcesMostAllocated` plugins now support customized weight on the CPU and memory. ([kubernetes/kubernetes#90544](https://github.com/kubernetes/kubernetes/pull/90544), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- `PostFilter` type is added to scheduler component config API on version v1beta1. ([kubernetes/kubernetes#91547](https://github.com/kubernetes/kubernetes/pull/91547), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- `kubescheduler.config.k8s.io` is now beta ([kubernetes/kubernetes#91420](https://github.com/kubernetes/kubernetes/pull/91420), [@pancernik](https://github.com/pancernik)) [SIG Scheduling]
 - EnvVarSource api doc bug fixes ([kubernetes/kubernetes#91194](https://github.com/kubernetes/kubernetes/pull/91194), [@wawa0210](https://github.com/wawa0210)) [SIG Apps]
 - The Kubelet's `--really-crash-for-testing` and  `--chaos-chance` options are now marked as deprecated. ([kubernetes/kubernetes#90499](https://github.com/kubernetes/kubernetes/pull/90499), [@knabben](https://github.com/knabben)) [SIG Node]
 - `NodeResourcesLeastAllocated` and `NodeResourcesMostAllocated` plugins now support customized weight on the CPU and memory. ([kubernetes/kubernetes#90544](https://github.com/kubernetes/kubernetes/pull/90544), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- K8s.io/apimachinery - scheme.Convert() now uses only explicitly registered conversions - default reflection based conversion is no longer available. `+k8s:conversion-gen` tags can be used with the `k8s.io/code-generator` component to generate conversions. ([kubernetes/kubernetes#90018](https://github.com/kubernetes/kubernetes/pull/90018), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps and Testing]
- Kubelet's --runonce option is now also available in Kubelet's config file as `runOnce`. ([kubernetes/kubernetes#89128](https://github.com/kubernetes/kubernetes/pull/89128), [@vincent178](https://github.com/vincent178)) [SIG Node]
- Promote Immutable Secrets/ConfigMaps feature to Beta and enable the feature by default.
  This allows to set `Immutable` field in Secrets or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#89594](https://github.com/kubernetes/kubernetes/pull/89594), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps and Testing]
- The unused `series.state` field, deprecated since v1.14, is removed from the `events.k8s.io/v1beta1` and `v1` Event types. ([kubernetes/kubernetes#90449](https://github.com/kubernetes/kubernetes/pull/90449), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps]
- Kube-proxy: add `--bind-address-hard-fail` flag to treat failure to bind to a port as fatal ([kubernetes/kubernetes#89350](https://github.com/kubernetes/kubernetes/pull/89350), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle and Network]
- Remove kubescheduler.config.k8s.io/v1alpha1 ([kubernetes/kubernetes#89298](https://github.com/kubernetes/kubernetes/pull/89298), [@gavinfish](https://github.com/gavinfish)) [SIG Scheduling]
- ServiceAppProtocol feature gate is now beta and enabled by default, adding new AppProtocol field to Services and Endpoints. ([kubernetes/kubernetes#90023](https://github.com/kubernetes/kubernetes/pull/90023), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The Kubelet's `--volume-plugin-dir` option is now available via the Kubelet config file field `VolumePluginDir`. ([kubernetes/kubernetes#88480](https://github.com/kubernetes/kubernetes/pull/88480), [@savitharaghunathan](https://github.com/savitharaghunathan)) [SIG Node]
- A new IngressClass resource has been added to enable better Ingress configuration. ([kubernetes/kubernetes#88509](https://github.com/kubernetes/kubernetes/pull/88509), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, CLI, Network, Node and Testing]
- API additions to apiserver types ([kubernetes/kubernetes#87179](https://github.com/kubernetes/kubernetes/pull/87179), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery, Cloud Provider and Cluster Lifecycle]
- Add Scheduling Profiles to kubescheduler.config.k8s.io/v1alpha2 ([kubernetes/kubernetes#88087](https://github.com/kubernetes/kubernetes/pull/88087), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling and Testing]
- Added GenericPVCDataSource feature gate to enable using arbitrary custom resources as the data source for a PVC. ([kubernetes/kubernetes#88636](https://github.com/kubernetes/kubernetes/pull/88636), [@bswartz](https://github.com/bswartz)) [SIG Apps and Storage]
- Added support for multiple sizes huge pages on a container level ([kubernetes/kubernetes#84051](https://github.com/kubernetes/kubernetes/pull/84051), [@bart0sh](https://github.com/bart0sh)) [SIG Apps, Node and Storage]
- Allow user to specify fsgroup permission change policy for pods ([kubernetes/kubernetes#88488](https://github.com/kubernetes/kubernetes/pull/88488), [@gnufied](https://github.com/gnufied)) [SIG Apps and Storage]
- AppProtocol is a new field on Service and Endpoints resources, enabled with the ServiceAppProtocol feature gate. ([kubernetes/kubernetes#88503](https://github.com/kubernetes/kubernetes/pull/88503), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- BlockVolume and CSIBlockVolume features are now GA. ([kubernetes/kubernetes#88673](https://github.com/kubernetes/kubernetes/pull/88673), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Node and Storage]
- Consumers of the 'certificatesigningrequests/approval' API must now grant permission to 'approve' CSRs for the 'signerName' specified on the CSR. More information on the new signerName field can be found at https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1513-certificate-signing-request/README.md/#signers ([kubernetes/kubernetes#88246](https://github.com/kubernetes/kubernetes/pull/88246), [@munnerz](https://github.com/munnerz)) [SIG API Machinery, Apps, Auth, CLI, Node and Testing]
- CustomResourceDefinition schemas that use `x-kubernetes-list-map-keys` to specify properties that uniquely identify list items must make those properties required or have a default value, to ensure those properties are present for all list items. See https://kubernetes.io/docs/reference/using-api/api-concepts/#merge-strategy for details. ([kubernetes/kubernetes#88076](https://github.com/kubernetes/kubernetes/pull/88076), [@eloyekunle](https://github.com/eloyekunle)) [SIG API Machinery and Testing]
- Fixed missing validation of uniqueness of list items in lists with `x-kubernetes-list-type: map` or `x-kubernetes-list-type: set` in CustomResources. ([kubernetes/kubernetes#84920](https://github.com/kubernetes/kubernetes/pull/84920), [@sttts](https://github.com/sttts)) [SIG API Machinery]
- Fixes a regression with clients prior to 1.15 not being able to update podIP in pod status, or podCIDR in node spec, against >= 1.16 API servers ([kubernetes/kubernetes#88505](https://github.com/kubernetes/kubernetes/pull/88505), [@liggitt](https://github.com/liggitt)) [SIG Apps and Network]
- Ingress: Add Exact and Prefix maching to Ingress PathTypes ([kubernetes/kubernetes#88587](https://github.com/kubernetes/kubernetes/pull/88587), [@cmluciano](https://github.com/cmluciano)) [SIG Apps, Cluster Lifecycle and Network]
- Ingress: Add alternate backends via TypedLocalObjectReference ([kubernetes/kubernetes#88775](https://github.com/kubernetes/kubernetes/pull/88775), [@cmluciano](https://github.com/cmluciano)) [SIG Apps and Network]
- Ingress: allow wildcard hosts in IngressRule ([kubernetes/kubernetes#88858](https://github.com/kubernetes/kubernetes/pull/88858), [@cmluciano](https://github.com/cmluciano)) [SIG Network]
- Introduces optional --detect-local flag to kube-proxy. 
  Currently the only supported value is "cluster-cidr", 
  which is the default if not specified. ([kubernetes/kubernetes#87748](https://github.com/kubernetes/kubernetes/pull/87748), [@satyasm](https://github.com/satyasm)) [SIG Cluster Lifecycle, Network and Scheduling]
- Kube-controller-manager and kube-scheduler expose profiling by default to match the kube-apiserver.  Use `--profiling=false` to disable. ([kubernetes/kubernetes#88663](https://github.com/kubernetes/kubernetes/pull/88663), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Cloud Provider and Scheduling]
- Kube-scheduler can run more than one scheduling profile. Given a pod, the profile is selected by using its `.spec.SchedulerName`. ([kubernetes/kubernetes#88285](https://github.com/kubernetes/kubernetes/pull/88285), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps, Scheduling and Testing]
- Move TaintBasedEvictions feature gates to GA ([kubernetes/kubernetes#87487](https://github.com/kubernetes/kubernetes/pull/87487), [@skilxn-go](https://github.com/skilxn-go)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Moving Windows RunAsUserName feature to GA ([kubernetes/kubernetes#87790](https://github.com/kubernetes/kubernetes/pull/87790), [@marosset](https://github.com/marosset)) [SIG Apps and Windows]
- New flag --endpointslice-updates-batch-period in kube-controller-manager can be used to reduce number of endpointslice updates generated by pod changes. ([kubernetes/kubernetes#88745](https://github.com/kubernetes/kubernetes/pull/88745), [@mborsz](https://github.com/mborsz)) [SIG API Machinery, Apps and Network]
- New flag `--show-hidden-metrics-for-version` in kubelet can be used to show all hidden metrics that deprecated in the previous minor release. ([kubernetes/kubernetes#85282](https://github.com/kubernetes/kubernetes/pull/85282), [@serathius](https://github.com/serathius)) [SIG Node]
- Removes ConfigMap as suggestion for IngressClass parameters ([kubernetes/kubernetes#89093](https://github.com/kubernetes/kubernetes/pull/89093), [@robscott](https://github.com/robscott)) [SIG Network]
- Scheduler Extenders can now be configured in the v1alpha2 component config ([kubernetes/kubernetes#88768](https://github.com/kubernetes/kubernetes/pull/88768), [@damemi](https://github.com/damemi)) [SIG Release, Scheduling and Testing]
- The apiserver/v1alph1 #EgressSelectorConfiguration API is now beta. ([kubernetes/kubernetes#88502](https://github.com/kubernetes/kubernetes/pull/88502), [@caesarxuchao](https://github.com/caesarxuchao)) [SIG API Machinery]
- The storage.k8s.io/CSIDriver has moved to GA, and is now available for use. ([kubernetes/kubernetes#84814](https://github.com/kubernetes/kubernetes/pull/84814), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, Apps, Auth, Node, Scheduling, Storage and Testing]
- VolumePVCDataSource moves to GA in 1.18 release ([kubernetes/kubernetes#88686](https://github.com/kubernetes/kubernetes/pull/88686), [@j-griffith](https://github.com/j-griffith)) [SIG Apps, CLI and Cluster Lifecycle]



# v18.20.1

* feat: load kubeconfig from dict ([#169](https://github.com/tomplus/kubernetes_asyncio/pull/169), [@tomplus](https://github.com/tomplus))

# v18.20.0

**Important Information:**

The library versioning scheme has been changed. Starting from this release, the library uses a version format `vY.Z.P` where `Y` and `Z` are respectively from the Kubernetes version `v1.Y.Z` and `P` would incremented due to changes on the library side itself. Ref: https://github.com/kubernetes-client/python/issues/1244

**API Deprecations:**
- The following deprecated APIs can no longer be served:
- All resources under `apps/v1beta1` and `apps/v1beta2` - use `apps/v1` instead
- `daemonsets`, `deployments`, `replicasets` resources under `extensions/v1beta1` - use `apps/v1` instead
- `networkpolicies` resources under `extensions/v1beta1` - use `networking.k8s.io/v1` instead
- `podsecuritypolicies` resources under `extensions/v1beta1` - use `policy/v1beta1` instead ([#85903](https://github.com/kubernetes/kubernetes/pull/85903), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Cluster Lifecycle, Instrumentation and Testing]

**API Change:**
- Fix bug in reflector that couldn't recover from "Too large resource version" errors ([#92537](https://github.com/kubernetes/kubernetes/pull/92537), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- Resolve regression in metadata.managedFields handling in update/patch requests submitted by older API clients ([#92007](https://github.com/kubernetes/kubernetes/pull/92007), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- A new IngressClass resource has been added to enable better Ingress configuration. ([#88509](https://github.com/kubernetes/kubernetes/pull/88509), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, CLI, Network, Node and Testing]
- The CSIDriver API has graduated to storage.k8s.io/v1, and is now available for use. ([#84814](https://github.com/kubernetes/kubernetes/pull/84814), [@huffmanca](https://github.com/huffmanca)) [SIG Storage]
- autoscaling/v2beta2 HorizontalPodAutoscaler added a `spec.behavior` field that allows scale behavior to be configured. Behaviors are specified separately for scaling up and down. In each direction a stabilization window can be specified as well as a list of policies and how to select amongst them. Policies can limit the absolute number of pods added or removed, or the percentage of pods added or removed. ([#74525](https://github.com/kubernetes/kubernetes/pull/74525), [@gliush](https://github.com/gliush)) [SIG API Machinery, Apps, Autoscaling and CLI]
- Ingress:
  - `spec.ingressClassName` replaces the deprecated `kubernetes.io/ingress.class` annotation, and allows associating an Ingress object with a particular controller.
  - path definitions added a `pathType` field to allow indicating how the specified path should be matched against incoming requests. Valid values are `Exact`, `Prefix`, and `ImplementationSpecific` ([#88587](https://github.com/kubernetes/kubernetes/pull/88587), [@cmluciano](https://github.com/cmluciano)) [SIG Apps, Cluster Lifecycle and Network]
- The alpha feature `AnyVolumeDataSource` enables PersistentVolumeClaim objects to use the spec.dataSource field to reference a custom type as a data source ([#88636](https://github.com/kubernetes/kubernetes/pull/88636), [@bswartz](https://github.com/bswartz)) [SIG Apps and Storage]
- The alpha feature `ConfigurableFSGroupPolicy` enables v1 Pods to specify a spec.securityContext.fsGroupChangePolicy policy to control how file permissions are applied to volumes mounted into the pod. ([#88488](https://github.com/kubernetes/kubernetes/pull/88488), [@gnufied](https://github.com/gnufied)) [SIG  Storage]
- The alpha feature `ServiceAppProtocol` enables setting an `appProtocol` field in ServicePort and EndpointPort definitions. ([#88503](https://github.com/kubernetes/kubernetes/pull/88503), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The alpha feature `ImmutableEphemeralVolumes` enables an `immutable` field in both Secret and ConfigMap objects to mark their contents as immutable. ([#86377](https://github.com/kubernetes/kubernetes/pull/86377), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps, CLI and Testing]
- The beta feature `ServerSideApply` enables tracking and managing changed fields for all new objects, which means there will be `managedFields` in `metadata` with the list of managers and their owned fields.
- The alpha feature `ServiceAccountIssuerDiscovery` enables publishing OIDC discovery information and service account token verification keys at `/.well-known/openid-configuration` and `/openid/v1/jwks` endpoints by API servers configured to issue service account tokens. ([#80724](https://github.com/kubernetes/kubernetes/pull/80724), [@cceckman](https://github.com/cceckman)) [SIG API Machinery, Auth, Cluster Lifecycle and Testing]
- CustomResourceDefinition schemas that use `x-kubernetes-list-map-keys` to specify properties that uniquely identify list items must make those properties required or have a default value, to ensure those properties are present for all list items. See https://kubernetes.io/docs/reference/using-api/api-concepts/&#35;merge-strategy for details. ([#88076](https://github.com/kubernetes/kubernetes/pull/88076), [@eloyekunle](https://github.com/eloyekunle)) [SIG API Machinery and Testing]
- CustomResourceDefinition schemas that use `x-kubernetes-list-type: map` or `x-kubernetes-list-type: set` now enable validation that the list items in the corresponding custom resources are unique. ([#84920](https://github.com/kubernetes/kubernetes/pull/84920), [@sttts](https://github.com/sttts)) [SIG API Machinery]

To read the full CHANGELOG visit [here](https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.18.md).

# v12.1.2

* fix: handle 401 returned by GKE ([#154](https://github.com/tomplus/kubernetes_asyncio/pull/154), [@tomplus](https://github.com/tomplus))

# v12.1.1

* fix: Watch() raises exceptions for received errors ([#151](https://github.com/tomplus/kubernetes_asyncio/pull/151), [@tomplus](https://github.com/tomplus))

# v12.1.0

* feat: add function to create objects from dict ([#143](https://github.com/tomplus/kubernetes_asyncio/pull/143), [@tomplus](https://github.com/tomplus))
* feat: Increase aiohttp read buffer to 2MiB ([#138](https://github.com/tomplus/kubernetes_asyncio/pull/138), [@acobHenner](https://github.com/JacobHenner))
* fix: Missing `create_from_yaml_single_item` import ([#133](https://github.com/tomplus/kubernetes_asyncio/pull/133), [@VideoSystemsTech](https://github.com/VideoSystemsTech))
* fix: show warning if config not loaded #127 ([#127](https://github.com/tomplus/kubernetes_asyncio/pull/127),   [@tomplus](https://github.com/tomplus))

# v12.0.1

* fix: remove checking headers if not preloaded content is returned from rest api ([#123](https://github.com/tomplus/kubernetes_asyncio/pull/123), [@tomplus](https://github.com/tomplus))

# v12.0.0

* feat: regenerate client for Kubernetes API Version: 1.16.14 using OpenAPI 4.3.1
* fix: Removed shlex args mangling ([#110](https://github.com/tomplus/kubernetes_asyncio/pull/110), [@WoLpH](https://github.com/WoLpH))
* fix: remove redundant close() in Watch class ([#119](https://github.com/tomplus/kubernetes_asyncio/pull/119), [@tomplus](https://github.com/tomplus))

**API Change:**

- Resolve regression in metadata.managedFields handling in update/patch requests submitted by older API clients ([#91748](https://github.com/kubernetes/kubernetes/pull/91748), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- Fix bug where sending a status update completely wipes managedFields for some types. ([#90033](https://github.com/kubernetes/kubernetes/pull/90033), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- The `MutatingWebhookConfiguration` and `ValidatingWebhookConfiguration` APIs have been promoted to `admissionregistration.k8s.io/v1`:
  - `failurePolicy` default changed from `Ignore` to `Fail` for v1
  - `matchPolicy` default changed from `Exact` to `Equivalent` for v1
  - `timeout` default changed from `30s` to `10s` for v1
  - `sideEffects` default value is removed, and the field made required, and only `None` and `NoneOnDryRun` are permitted for v1
  - `admissionReviewVersions` default value is removed and the field made required for v1 (supported versions for AdmissionReview are `v1` and `v1beta1`)
  - The `name` field for specified webhooks must be unique for `MutatingWebhookConfiguration` and `ValidatingWebhookConfiguration` objects created via `admissionregistration.k8s.io/v1`
- The `AdmissionReview` API sent to and received from admission webhooks has been promoted to `admission.k8s.io/v1`. Webhooks can specify a preference for receiving `v1` AdmissionReview objects with `admissionReviewVersions: ["v1","v1beta1"]`, and must respond with an API object in the same `apiVersion` they are sent. When webhooks use `admission.k8s.io/v1`, the following additional validation is performed on their responses:
  - `response.patch` and `response.patchType` are not permitted from validating admission webhooks
  - `apiVersion: "admission.k8s.io/v1"` is required
  - `kind: "AdmissionReview"` is required
  - `response.uid: "<value of request.uid>"` is required
  - `response.patchType: "JSONPatch"` is required (if `response.patch` is set) ([#80231](https://github.com/kubernetes/kubernetes/pull/80231), [@liggitt](https://github.com/liggitt))
- The `CustomResourceDefinition` API type is promoted to `apiextensions.k8s.io/v1` with the following changes:
  - Use of the new `default` feature in validation schemas is limited to v1
  - `spec.scope` is no longer defaulted to `Namespaced` and must be explicitly specified
  - `spec.version` is removed in v1; use `spec.versions` instead
  - `spec.validation` is removed in v1; use `spec.versions[*].schema` instead
  - `spec.subresources` is removed in v1; use `spec.versions[*].subresources` instead
  - `spec.additionalPrinterColumns` is removed in v1; use `spec.versions[*].additionalPrinterColumns` instead
  - `spec.conversion.webhookClientConfig` is moved to `spec.conversion.webhook.clientConfig` in v1
  - `spec.conversion.conversionReviewVersions` is moved to `spec.conversion.webhook.conversionReviewVersions` in v1
  - `spec.versions[*].schema.openAPIV3Schema` is now required when creating v1 CustomResourceDefinitions
  - `spec.preserveUnknownFields: true` is disallowed when creating v1 CustomResourceDefinitions; it must be specified within schema definitions as `x-kubernetes-preserve-unknown-fields: true`
  - In `additionalPrinterColumns` items, the `JSONPath` field was renamed to `jsonPath` in v1 (fixes https://github.com/kubernetes/kubernetes/issues/66531)
    The `apiextensions.k8s.io/v1beta1` version of `CustomResourceDefinition` is deprecated and will no longer be served in v1.19. ([#79604](https://github.com/kubernetes/kubernetes/pull/79604), [@liggitt](https://github.com/liggitt))
- The `ConversionReview` API sent to and received from custom resource CustomResourceDefinition conversion webhooks has been promoted to `apiextensions.k8s.io/v1`. CustomResourceDefinition conversion webhooks can now indicate they support receiving and responding with `ConversionReview` API objects in the `apiextensions.k8s.io/v1` version by including `v1` in the `conversionReviewVersions` list in their CustomResourceDefinition. Conversion webhooks must respond with a ConversionReview object in the same apiVersion they receive. `apiextensions.k8s.io/v1` `ConversionReview` responses must specify a `response.uid` that matches the `request.uid` of the object they were sent. ([#81476](https://github.com/kubernetes/kubernetes/pull/81476), [@liggitt](https://github.com/liggitt))
- Add scheduling support for RuntimeClasses. RuntimeClasses can now specify nodeSelector constraints & tolerations, which are merged into the PodSpec for pods using that RuntimeClass. ([#80825](https://github.com/kubernetes/kubernetes/pull/80825), [@tallclair](https://github.com/tallclair))
- Kubelet should now more reliably report the same primary node IP even if the set of node IPs reported by the CloudProvider changes. ([#79391](https://github.com/kubernetes/kubernetes/pull/79391), [@danwinship](https://github.com/danwinship))
- Omit nil or empty field when calculating container hash value to avoid hash changed. For a new field with a non-nil default value in the container spec, the hash would still get changed. ([#57741](https://github.com/kubernetes/kubernetes/pull/57741), [@dixudx](https://github.com/dixudx))
- Property `conditions` in `apiextensions.v1beta1.CustomResourceDefinitionStatus` and `apiextensions.v1.CustomResourceDefinitionStatus` is now optional instead of required. ([#64996](https://github.com/kubernetes/kubernetes/pull/64996), [@roycaihw](https://github.com/roycaihw))
- When the status of a CustomResourceDefinition condition changes, its corresponding `lastTransitionTime` is now updated. ([#69655](https://github.com/kubernetes/kubernetes/pull/69655), [@CaoShuFeng](https://github.com/CaoShuFeng))

# v11.3.0

* fix: watch closes http session ([#104](https://github.com/tomplus/kubernetes_asyncio/pull/104), [@tomplus](https://github.com/tomplus))

# v11.2.0

* feat: regenerate client against openapi-generator v4.3.0 (context-manager and close function for http client instead of using `__del__` method)
  ([#99](https://github.com/tomplus/kubernetes_asyncio/pull/99), [@jnschaeffer](https://github.com/jnschaeffer))

# v11.1.0

* feat: add compatability for follow methods ([#98](https://github.com/tomplus/kubernetes_asyncio/pull/98), [@playground-julia](https://github.com/playground-julia))

# v11.0.0

* feat: regenerate library using the latest version of openapi-generator (4.3.x) ([gen/#146](https://github.com/kubernetes-client/gen/pull/146), [@tomplus](https://github.com/tomplus))
* test: add tests for Python 3.8. ([#86](https://github.com/tomplus/kubernetes_asyncio/pull/86), [@tomplus](https://github.com/tomplus))
* fix: prevent installing aiohttp 4.0 and up for now ([#88](https://github.com/tomplus/kubernetes_asyncio/pull/88), [@sepulworld](https://github.com/sepulworld))
* fix: watch.stream stores resource_version for the next call ([#89](https://github.com/tomplus/kubernetes_asyncio/pull/89), [@tomplus](https://github.com/tomplus))
* chore: remove unused path import ([#92](https://github.com/tomplus/kubernetes_asyncio/pull/92), [@aK0nshin](https://github.com/aK0nshin))

**API Change:**
- Introduce `ExtensionsV1beta1RuntimeClassStrategyOptions` and `PolicyV1beta1RuntimeClassStrategyOptions`. Add RuntimeClass restrictions & defaulting to PodSecurityPolicy [kubernetes/kubernetes#73795](https://github.com/kubernetes/kubernetes/pull/73795)
- Introduce `V1WindowsSecurityContextOptions`. Add Windows specific options in Pod Security Context and Container Security Context [kubernetes/kubernetes#77147](https://github.com/kubernetes/kubernetes/pull/77147)
- Split `V1beta1Webhook` into `V1beta1MutatingWebhook` and `V1beta1ValidatingWebhook` [kubernetes/kubernetes#78491](https://github.com/kubernetes/kubernetes/pull/78491)
- Introduce parameter `allow_watch_bookmarks` in list options for requesting watch bookmarks from apiserver. The implementation in apiserver is hidden behind feature gate `WatchBookmark` (currently in Alpha stage) [kubernetes/kubernetes#74074](https://github.com/kubernetes/kubernetes/pull/74074)
- Add `V1DeleteOptions` parameters (`dry_run`, `grace_period_seconds`, `orphan_dependents`, `propagation_policy`) to delete collection APIs [kubernetes/kubernetes#77843](https://github.com/kubernetes/kubernetes/pull/77843)
- Add ListMeta.RemainingItemCount. When responding a LIST request, if the server has more data available, and if the request does not contain label selectors or field selectors, the server sets the ListOptions.RemainingItemCount to the number of remaining objects [kubernetes/kubernetes#75993](https://github.com/kubernetes/kubernetes/pull/75993)
- Add `controller_expand_secret_ref` in `V1SecretReference` to store CSI volume expansion secrets [kubernetes/kubernetes#77516](https://github.com/kubernetes/kubernetes/pull/77516)
- Introduce `preemption_policy` field to V1PriorityClass [kubernetes/kubernetes#74614](https://github.com/kubernetes/kubernetes/pull/74614)
- Add `port` configuration to service reference in Admission webhook configuration, AuditSink webhook configuration, CRD Conversion webhook configuration and kube-aggregator [kubernetes/kubernetes#74855](https://github.com/kubernetes/kubernetes/pull/74855)
- Introduce `inline_volume_spec` to `V1PersistentVolumeSpec` [kubernetes/kubernetes#77703](https://github.com/kubernetes/kubernetes/pull/77703)
- Add fields `x_kubernetes_embedded_resource`, `x_kubernetes_int_or_string`, `x_kubernetes_preserve_unknown_fields` to V1beta1JSONSchemaProps [kubernetes/kubernetes#77207](https://github.com/kubernetes/kubernetes/pull/77207)

# v10.0.1

* fix: when `_preload_content=False` Websocket Stream returns 401 error ([#84](https://github.com/tomplus/kubernetes_asyncio/pull/84), [@kexirong](https://github.com/kexirong))
* fix: e2e tests use `apps/v1` api instead of removed `extensions/v1beta1` ([#85](https://github.com/tomplus/kubernetes_asyncio/pull/85), [@tomplus](https://github.com/tomplus))

# v10.0.0

* feat: add `create_form_yaml()` functionality ([#76](https://github.com/tomplus/kubernetes_asyncio/pull/76), [@PidgeyBE](https://github.com/PidgeyBE))
* feat: custom objects can be merged by json-patch ([gen/#119](https://github.com/kubernetes-client/gen/pull/119), [@tomplus](https://github.com/tomplus)) 
* fix: parse microseconds in data-time fields ([#80](https://github.com/tomplus/kubernetes_asyncio/pull/80), [@tomplus](https://github.com/tomplus))
* feat: upgrade to API spec from Kubernetes 1.14 ([#83](https://github.com/tomplus/kubernetes_asyncio/pull/83), [@tomplus](https://github.com/tomplus))

**API Change:**

- Remove the AdmissionregistrationV1alpha1 API group, containing only the InitializationConfiguration type [kubernetes/kubernetes#72972](https://github.com/kubernetes/kubernetes/pull/72972)
- Promote Lease API to v1 [kubernetes/kubernetes#72239](https://github.com/kubernetes/kubernetes/pull/72239)
- The Ingress API is now available via `NetworkingV1beta1Api`. `ExtensionsV1beta1Api` Ingress objects are deprecated and will no longer be served in Kubernetes v1.18 [kubernetes/kubernetes#74057](https://github.com/kubernetes/kubernetes/pull/74057)
- Introduce RuntimeClass to NodeV1alpha1Api and NodeV1beta1Api [kubernetes/kubernetes#74433](https://github.com/kubernetes/kubernetes/pull/74433)
- Graduate PriorityClass API to GA SchedulingV1Api [kubernetes/kubernetes#73555](https://github.com/kubernetes/kubernetes/pull/73555)
- Introduce CSINodeInfo and CSIDriver to StorageV1beta1Api [kubernetes/kubernetes#74283](https://github.com/kubernetes/kubernetes/pull/74283)
- The alpha Initializers feature, `admissionregistration.k8s.io/v1alpha1` API version, `Initializers` admission plugin, and use of the `metadata.initializers` API field have been removed. Discontinue use of the alpha feature and delete any existing `InitializerConfiguration` API objects before upgrading. The `metadata.initializers` field will be removed in a future release. The parameter `include_uninitialized` has been removed. [kubernetes/kubernetes#72972](https://github.com/kubernetes/kubernetes/pull/72972)

# v9.1.0

* feat: check whether an object key is present on watch ([#71](https://github.com/tomplus/kubernetes_asyncio/pull/71), [@mickours](https://github.com/mickours))
* feat: merging kubeconfig files ([#69](https://github.com/tomplus/kubernetes_asyncio/pull/69), [@tomplus](https://github.com/tomplus))

# v9.0.0

* feat: switch to openapi-generator ([#58](https://github.com/tomplus/kubernetes_asyncio/pull/58), [@tomplus](https://github.com/tomplus))
* feat: add fieldSelector parameter to list/watch methods in custom objects spec ([gen/#106](https://github.com/kubernetes-client/gen/pull/106))
* feat: upgrade to API spec from Kubernetes 1.13 ([#58](https://github.com/tomplus/kubernetes_asyncio/pull/58), [@tomplus](https://github.com/tomplus))

Breaking Changes:
* Model v1beta1WebhookClientConfig is renamed to AdmissionregistrationV1beta1WebhookClientConfig, to avoid naming conflict
   with ApiextensionsV1beta1WebhookClientConfig introduced in: kubernetes/kubernetes#67006
* Delete request's body parameter is optional kubernetes/kubernetes#70032

# v8.1.0

* feat: watch improvement (context manager, close method) ([#61](https://github.com/tomplus/kubernetes_asyncio/pull/61), [@hubo1016](https://github.com/hubo1016))

# v8.0.3

* fix: use `yaml.safe_load`, `yaml.safe_dump` for security reasons ([#57](https://github.com/tomplus/kubernetes_asyncio/pull/57), [@tomplus](https://github.com/tomplus))

# v8.0.2

* feat: remove dependency to urllib3 from kube_config, pin urlllib>=1.23 due to CVE-2018-20060 ([#56](https://github.com/tomplus/kubernetes_asyncio/pull/56), [@tomplus](https://github.com/tomplus))

# v8.0.1

* fix: kubeconfig loading failure when server uri contains trailing slash ([#53](https://github.com/tomplus/kubernetes_asyncio/pull/53), [@tomplus](https://github.com/tomplus))
* feat: regenerate client with thread-pool optimization ([#54](https://github.com/tomplus/kubernetes_asyncio/pull/54), [@tomplus](https://github.com/tomplus))

# v8.0.0

* feat: upgrade to API spec from Kubernetes 1.12 ([#50](https://github.com/tomplus/kubernetes_asyncio/pull/50), [@tomplus](https://github.com/tomplus))

# v7.0.0

* first stable release 7.0.0

# v1.0.0-beta9

* fix: option verify-ssl impacts on server certs only ([#46](https://github.com/tomplus/kubernetes_asyncio/pull/46),
  [@tomplus](https://github.com/tomplus))

# v1.0.0-beta8

* feat: add debug logs to KubeConfigLoader ([#45](https://github.com/tomplus/kubernetes_asyncio/pull/45),
  [@tomplus](https://github.com/tomplus))
* feat: exec-plugins support in kubeconfig ([#44](https://github.com/tomplus/kubernetes_asyncio/pull/44),
  [@tomplus](https://github.com/tomplus))
* fix: read config data with bytes (python3) ([#41](https://github.com/tomplus/kubernetes_asyncio/pull/41),
  [@tomplus](https://github.com/tomplus))

# v1.0.0-beta7

* feat: add OIDC auth support ([#36](https://github.com/tomplus/kubernetes_asyncio/pull/36),
  [@bpicolo](https://github.com/bpicolo))

# v1.0.0-beta6

* feat: regenerate with latest client gen to get custom object status scale api
  ([#37](https://github.com/tomplus/kubernetes_asyncio/pull/37), [@juliantaylor](https://github.com/juliantaylor))
* fix: handling timeout by watch loop ([#39](https://github.com/tomplus/kubernetes_asyncio/pull/39),
  [@tomplus](https://github.com/tomplus))

# v1.0.0-beta5

* feat: upgrade to spec from Kuberentes 1.11 ([#34](https://github.com/tomplus/kubernetes_asyncio/pull/34), [@tomplus](https://github.com/tomplus))

# v1.0.0-beta4

* fix: aiohttp with `verify_ssl=False` ([#33](https://github.com/tomplus/kubernetes_asyncio/pull/33), [@bpicolo](https://github.com/bpicolo))

# v1.0.0-beta3

* feat: watch work forever if timeout is not specified ([#30](https://github.com/tomplus/kubernetes_asyncio/pull/30), [@tomplus](https://github.com/tomplus))

# v1.0.0-beta2

* feat: support Python 3.7 ([#28](https://github.com/tomplus/kubernetes_asyncio/pull/28), [@tomplus](https://github.com/tomplus))

# v1.0.0-beta1

* feat: make function `load_kube_config` asynchronous
* feat: function to auto-refresh gke token 
* feat: remove synchronous libraries from dependencies

# v1.0.0-alpha4

* feat: watch stops the iterator for empty responses and do not process ERROR responses ([#22](https://github.com/tomplus/kubernetes_asyncio/pull/22), [@olitheolix](https://github.com/olitheolix))
* feat: replace urllib3 by http.client in e2e initializer ([#20](https://github.com/tomplus/kubernetes_asyncio/pull/20), [@tomplus](https://github.com/tomplus))
* feat: new example - tail.py ([#19](https://github.com/tomplus/kubernetes_asyncio/pull/19), [@tomplus](https://github.com/tomplus))
* feat: new example - simultaneously watch multiple event streams without threads ([#13](https://github.com/tomplus/kubernetes_asyncio/pull/13), [@olitheolix](https://github.com/olitheolix))
* fix: fix few typos in setup.py ([#18](https://github.com/tomplus/kubernetes_asyncio/pull/18), [@evemorgen](https://github.com/evemorgen))
* fix: requirement for requests and urllib3 version ([#16](https://github.com/tomplus/kubernetes_asyncio/pull/16), [@tomplus](https://github.com/tomplus))

# v1.0.0-alpha3

* fix e2e and unit tests
* fix Watch, Stream

# v1.0.0-alpha2

* fix requirements.txt

# v1.0.0-alpha1

* first release
