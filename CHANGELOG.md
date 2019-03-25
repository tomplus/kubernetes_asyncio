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

* fix: feat: remove dependency to urllib3 from kube_config, pin urlllib>=1.23 due to CVE-2018-20060 ([#56](https://github.com/tomplus/kubernetes_asyncio/pull/56), [@tomplus](https://github.com/tomplus))

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
