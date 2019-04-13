# Contributing guidelines

### Contributing A Patch

1. Submit an issue describing your proposed change to the repo in question.
1. The [repo owners](OWNERS) will respond to your issue promptly.
1. If your proposed change is accepted, and you haven't already done so, sign a Contributor License Agreement (see details above).
1. Fork the desired repo, develop and test your code changes.
1. Submit a pull request.

### Adding dependencies

If your patch depends on new packages, add those packages to [requirements.txt](requirements.txt) and [setup.py](setup.py).

### Rebuild client

This client is built (as other Kubernetes clients) by scripts from [kubernetes-client/gen](https://github.com/kubernetes-client/gen).
These scripts prepare a docker image with preinstalled tools (eg. openapi-generator).
It's time consuming but finally this image is cached on your local machine and next regenerations will work smoothly.

To simplify set up the environment here is a script named `scripts/update-client.sh` which clones
[kubernetes-client/gen](https://github.com/kubernetes-client/gen) and launches regenerating process.
