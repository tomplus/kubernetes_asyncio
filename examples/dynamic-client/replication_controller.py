# Copyright 2021 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This example demonstrates the creation, listing & deletion of a namespaced replication controller using dynamic-client.
"""

import asyncio

from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.client.configuration import Configuration
from kubernetes_asyncio.config import kube_config
from kubernetes_asyncio.dynamic import DynamicClient


async def main():
    # Creating a dynamic client
    config = Configuration()
    await kube_config.load_kube_config(client_configuration=config)
    async with api_client.ApiClient(configuration=config) as apic:
        client = await DynamicClient(apic)

        # fetching the replication controller api
        api = await client.resources.get(api_version="v1", kind="ReplicationController")

        name = "frontend-replication-controller"

        replication_controller_manifest = {
            "apiVersion": "v1",
            "kind": "ReplicationController",
            "metadata": {"labels": {"name": name}, "name": name},
            "spec": {
                "replicas": 2,
                "selector": {"name": name},
                "template": {
                    "metadata": {"labels": {"name": name}},
                    "spec": {
                        "containers": [
                            {
                                "image": "nginx",
                                "name": "nginx",
                                "ports": [{"containerPort": 80, "protocol": "TCP"}],
                            }
                        ]
                    },
                },
            },
        }

        # Creating replication-controller `frontend-replication-controller` in the `default` namespace
        await api.create(body=replication_controller_manifest, namespace="default")

        print(
            "\n[INFO] replication-controller `frontend-replication-controller` created\n"
        )

        # Listing replication-controllers in the `default` namespace
        replication_controller_created = await api.get(name=name, namespace="default")

        print("%s\t%s\t\t\t\t\t%s" % ("NAMESPACE", "NAME", "REPLICAS"))
        print(
            "%s\t\t%s\t\t%s\n"
            % (
                replication_controller_created.metadata.namespace,
                replication_controller_created.metadata.name,
                replication_controller_created.spec.replicas,
            )
        )

        # Deleting replication-controller `frontend-service` from the `default` namespace
        await api.delete(name=name, body={}, namespace="default")

        print(
            "[INFO] replication-controller `frontend-replication-controller` deleted\n"
        )


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()
