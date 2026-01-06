# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import time
from typing import Any, cast
import uuid
from unittest import IsolatedAsyncioTestCase

from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.client.api import core_v1_api
from kubernetes_asyncio.client.configuration import Configuration
from kubernetes_asyncio.client.models.v1_config_map import V1ConfigMap
from kubernetes_asyncio.client.models.v1_container import V1Container
from kubernetes_asyncio.client.models.v1_container_port import V1ContainerPort
from kubernetes_asyncio.client.models.v1_object_meta import V1ObjectMeta
from kubernetes_asyncio.client.models.v1_pod import V1Pod
from kubernetes_asyncio.client.models.v1_pod_spec import V1PodSpec
from kubernetes_asyncio.client.models.v1_pod_template_spec import V1PodTemplateSpec
from kubernetes_asyncio.client.models.v1_replication_controller import (
    V1ReplicationController,
)
from kubernetes_asyncio.client.models.v1_replication_controller_spec import (
    V1ReplicationControllerSpec,
)
from kubernetes_asyncio.client.models.v1_service import V1Service
from kubernetes_asyncio.client.models.v1_service_port import V1ServicePort
from kubernetes_asyncio.client.models.v1_service_spec import V1ServiceSpec
from kubernetes_asyncio.e2e_test import base
from kubernetes_asyncio.stream import WsApiClient


def short_uuid() -> str:
    id = str(uuid.uuid4())
    return id[-12:]


class TestClient(IsolatedAsyncioTestCase):
    config: Configuration

    @classmethod
    def setUpClass(cls) -> None:
        cls.config = base.get_e2e_configuration()

    async def test_pod_apis(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        client_ws = WsApiClient(configuration=self.config)

        api = core_v1_api.CoreV1Api(client)
        api_ws = core_v1_api.CoreV1Api(client_ws)

        name = "busybox-test-" + short_uuid()
        pod_manifest = V1Pod(
            api_version="v1",
            kind="Pod",
            metadata=V1ObjectMeta(name=name),
            spec=V1PodSpec(
                containers=[
                    V1Container(
                        image="busybox",
                        name="sleep",
                        args=[
                            "/bin/sh",
                            "-c",
                            "while true;do date;sleep 5; done",
                        ],
                    )
                ]
            ),
        )

        resp = await api.create_namespaced_pod(body=pod_manifest, namespace="default")
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        while True:
            resp = await api.read_namespaced_pod(name=name, namespace="default")
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)
            if resp.status.phase != "Pending":
                break
            time.sleep(1)

        exec_command = ["/bin/sh", "-c", "for i in $(seq 1 3); do date; done"]
        resp_out = await api_ws.connect_get_namespaced_pod_exec(
            name,
            "default",
            command=exec_command,
            stderr=False,
            stdin=False,
            stdout=True,
            tty=False,
        )
        print("EXEC response : %s" % resp_out)
        self.assertEqual(3, len(resp_out.splitlines()))

        resp_out = await api_ws.connect_post_namespaced_pod_exec(
            name,
            "default",
            command="uptime",
            stderr=False,
            stdin=False,
            stdout=True,
            tty=False,
        )
        print("EXEC response : %s" % resp_out)
        self.assertEqual(1, len(resp_out.splitlines()))

        resp_list = await api.list_pod_for_all_namespaces()
        number_of_pods = len(resp_list.items)
        self.assertTrue(number_of_pods > 0)

        resp = await api.delete_namespaced_pod(name=name, body={}, namespace="default")

    async def test_service_apis(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = "frontend-" + short_uuid()
        service_manifest = V1Service(
            api_version="v1",
            kind="Service",
            metadata=V1ObjectMeta(
                labels={"name": name},
                name=name,
                resource_version="v1",
            ),
            spec=V1ServiceSpec(
                ports=[
                    V1ServicePort(name="port", port=80, protocol="TCP", target_port=80)
                ],
                selector={"name": name},
            ),
        )

        resp = await api.create_namespaced_service(
            body=service_manifest, namespace="default"
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        resp = await api.read_namespaced_service(name=name, namespace="default")
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        # strategic merge patch
        resp = await api.patch_namespaced_service(
            name=name,
            namespace="default",
            body={
                "spec": {
                    "ports": [
                        {
                            "name": "new",
                            "port": 8080,
                            "protocol": "TCP",
                            "targetPort": 8080,
                        }
                    ]
                }
            },
        )
        self.assertEqual(len(resp.spec.ports), 2)
        self.assertTrue(resp.status)

        # json merge patch
        resp = await api.patch_namespaced_service(
            name=name,
            namespace="default",
            body={
                "spec": {
                    "ports": [
                        {
                            "name": "new2",
                            "port": 8080,
                            "protocol": "TCP",
                            "targetPort": 8080,
                        }
                    ]
                }
            },
            _content_type="application/merge-patch+json",
        )
        self.assertEqual(len(resp.spec.ports), 1)
        self.assertEqual(resp.spec.ports[0].name, "new2")
        self.assertTrue(resp.status)

        # json patch
        resp = await api.patch_namespaced_service(
            name=name,
            namespace="default",
            body=[
                {
                    "op": "add",
                    "path": "/spec/ports/0",
                    "value": {
                        "name": "new3",
                        "protocol": "TCP",
                        "port": 1000,
                        "targetPort": 1000,
                    },
                }
            ],
        )
        self.assertEqual(len(resp.spec.ports), 2)
        self.assertEqual(resp.spec.ports[0].name, "new3")
        self.assertEqual(resp.spec.ports[1].name, "new2")
        self.assertTrue(resp.status)
        resp = await api.delete_namespaced_service(
            name=name, body={}, namespace="default"
        )

    async def test_replication_controller_apis(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = "frontend-" + short_uuid()
        rc_manifest = V1ReplicationController(
            api_version="v1",
            kind="ReplicationController",
            metadata=V1ObjectMeta(labels={"name": name}, name=name),
            spec=V1ReplicationControllerSpec(
                replicas=2,
                selector={"name": name},
                template=V1PodTemplateSpec(
                    metadata=V1ObjectMeta(labels={"name": name}),
                    spec=V1PodSpec(
                        containers=[
                            V1Container(
                                image="nginx",
                                name="nginx",
                                ports=[
                                    V1ContainerPort(container_port=80, protocol="TCP")
                                ],
                            )
                        ]
                    ),
                ),
            ),
        )

        resp = await api.create_namespaced_replication_controller(
            body=rc_manifest, namespace="default"
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = await api.read_namespaced_replication_controller(
            name=name, namespace="default"
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        await api.delete_namespaced_replication_controller(
            name=name, namespace="default"
        )

    async def test_configmap_apis(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = "test-configmap-" + short_uuid()
        test_configmap = V1ConfigMap(
            kind="ConfigMap",
            api_version="v1",
            metadata=V1ObjectMeta(name=name),
            data={
                "config.json": '{"command":"/usr/bin/mysqld_safe"}',
                "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\nport = 3306\n",
            },
        )

        resp = await api.create_namespaced_config_map(
            body=test_configmap, namespace="default"
        )
        self.assertEqual(name, resp.metadata.name)

        resp = await api.read_namespaced_config_map(name=name, namespace="default")
        self.assertEqual(name, resp.metadata.name)

        # strategic merge patch
        resp = await api.patch_namespaced_config_map(
            name=name,
            namespace="default",
            body={"data": {"key": "value", "frontend.cnf": "patched"}},
        )

        resp = await api.read_namespaced_config_map(name=name, namespace="default")
        self.assertEqual(resp.data["config.json"], test_configmap.data["config.json"])
        self.assertEqual(resp.data["frontend.cnf"], "patched")
        self.assertEqual(resp.data["key"], "value")

        await api.delete_namespaced_config_map(name=name, namespace="default")

        resp_list = await api.list_namespaced_config_map("default", pretty=True)
        for item in resp_list.items:
            self.assertNotEqual(item.metadata.name, name)

    async def test_node_apis(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        resp = await api.list_node()

        for item in resp.items:
            node = await api.read_node(name=item.metadata.name)
            self.assertTrue(len(node.metadata.labels) > 0)
            self.assertTrue(isinstance(node.metadata.labels, dict))

    async def test_body_as_dict(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = "test-configmap-" + short_uuid()
        test_configmap: dict[str, Any] = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
            },
            "data": {
                "config.json": '{"command":"/usr/bin/mysqld_safe"}',
                "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\nport = 3306\n",
            },
        }

        # cast dict as V1ConfigMap
        resp = await api.create_namespaced_config_map(
            body=cast(V1ConfigMap, test_configmap), namespace="default"
        )
        self.assertEqual(name, resp.metadata.name)

        # strategic merge patch
        resp = await api.patch_namespaced_config_map(
            name=name,
            namespace="default",
            body={"data": {"key": "value", "frontend.cnf": "patched"}},
        )

        resp = await api.read_namespaced_config_map(name=name, namespace="default")
        self.assertEqual(
            resp.data["config.json"], test_configmap["data"]["config.json"]
        )
        self.assertEqual(resp.data["frontend.cnf"], "patched")
        self.assertEqual(resp.data["key"], "value")

        resp_status = await api.delete_namespaced_config_map(
            name=name, body={}, namespace="default"
        )
        self.assertIsNotNone(resp_status)

        resp_list = await api.list_namespaced_config_map("default", pretty=True)
        for item in resp_list.items:
            self.assertNotEqual(item.metadata.name, name)
