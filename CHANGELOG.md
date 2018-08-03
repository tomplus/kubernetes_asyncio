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
