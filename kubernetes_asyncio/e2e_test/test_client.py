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
import uuid
from unittest import IsolatedAsyncioTestCase

from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.client.api import (
    apiextensions_v1_api, core_v1_api, custom_objects_api,
)
from kubernetes_asyncio.e2e_test import base
from kubernetes_asyncio.stream import WsApiClient


def short_uuid():
    id = str(uuid.uuid4())
    return id[-12:]


class TestClient(IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    async def test_pod_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        client_ws = WsApiClient(configuration=self.config)

        api = core_v1_api.CoreV1Api(client)
        api_ws = core_v1_api.CoreV1Api(client_ws)

        name = 'busybox-test-' + short_uuid()
        pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {
                'name': name
            },
            'spec': {
                'containers': [{
                    'image': 'busybox',
                    'name': 'sleep',
                    "args": [
                        "/bin/sh",
                        "-c",
                        "while true;do date;sleep 5; done"
                    ]
                }]
            }
        }

        resp = await api.create_namespaced_pod(body=pod_manifest, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        while True:
            resp = await api.read_namespaced_pod(name=name, namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)

        exec_command = ['/bin/sh',
                        '-c',
                        'for i in $(seq 1 3); do date; done']
        resp = await api_ws.connect_get_namespaced_pod_exec(
            name, 'default', command=exec_command,
            stderr=False, stdin=False, stdout=True, tty=False
        )
        print('EXEC response : %s' % resp)
        self.assertEqual(3, len(resp.splitlines()))

        exec_command = 'uptime'
        resp = await api_ws.connect_post_namespaced_pod_exec(
            name, 'default', command=exec_command,
            stderr=False, stdin=False, stdout=True, tty=False
        )
        print('EXEC response : %s' % resp)
        self.assertEqual(1, len(resp.splitlines()))

        resp = await api.list_pod_for_all_namespaces()
        number_of_pods = len(resp.items)
        self.assertTrue(number_of_pods > 0)

        resp = await api.delete_namespaced_pod(name=name, body={}, namespace='default')

    async def test_service_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'frontend-' + short_uuid()
        service_manifest = {'apiVersion': 'v1',
                            'kind': 'Service',
                            'metadata': {'labels': {'name': name},
                                         'name': name,
                                         'resourceversion': 'v1'},
                            'spec': {'ports': [{'name': 'port',
                                                'port': 80,
                                                'protocol': 'TCP',
                                                'targetPort': 80}],
                                     'selector': {'name': name}}}

        resp = await api.create_namespaced_service(body=service_manifest, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        resp = await api.read_namespaced_service(name=name, namespace='default')
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

    async def test_custom_objects_api(self):
        client = api_client.ApiClient(configuration=self.config)

        apiextensions_api_client = apiextensions_v1_api.ApiextensionsV1Api(client)
        custom_objects_api_client = custom_objects_api.CustomObjectsApi(client)

        name = 'clusterchangemes.apps.example.com'
        crd_manifest = {
            "apiVersion": "apiextensions.k8s.io/v1",
            "kind": "CustomResourceDefinition",
            "metadata": {
                "name": name,
            },
            "spec": {
                "group": "apps.example.com",
                "names": {
                    "kind": "ClusterChangeMe",
                    "listKind": "ClusterChangeMeList",
                    "plural": "clusterchangemes",
                    "singular": "clusterchangeme",
                },
                "scope": "Cluster",
                "versions": [
                    {
                        "name": "v1",
                        "served": True,
                        "storage": True,
                        "schema": {
                            "openAPIV3Schema": {
                                "type": "object",
                                "properties": {
                                    "spec": {
                                        "type": "object",
                                        "properties": {
                                            "size": {"type": "integer"}
                                        },
                                    }
                                },
                            }
                        },
                    }
                ],
            },
        }
        custom_object_manifest = {
            'apiVersion': 'apps.example.com/v1',
            'kind': 'ClusterChangeMe',
            'metadata': {
                'name': "changeme-name",
            },
            'spec': {}
        }

        await apiextensions_api_client.create_custom_resource_definition(
            crd_manifest
        )

        await apiextensions_api_client.read_custom_resource_definition(
            crd_manifest["metadata"]["name"]
        )

        await custom_objects_api_client.create_cluster_custom_object(
            crd_manifest["spec"]["group"],
            crd_manifest["spec"]["versions"][0]["name"],
            crd_manifest["spec"]["names"]["plural"],
            custom_object_manifest
        )

        # json merge patch (implied)
        resp = await custom_objects_api_client.patch_cluster_custom_object(
            group=crd_manifest["spec"]["group"],
            version=crd_manifest["spec"]["versions"][0]["name"],
            plural=crd_manifest["spec"]["names"]["plural"],
            name=custom_object_manifest["metadata"]["name"],
            body={
                "spec": {
                    "size": 0
                }
            },
        )
        self.assertEqual(resp["spec"]["size"], 0)

        await apiextensions_api_client.delete_custom_resource_definition(
            crd_manifest["metadata"]["name"]
        )

    async def test_replication_controller_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'frontend-' + short_uuid()
        rc_manifest = {
            'apiVersion': 'v1',
            'kind': 'ReplicationController',
            'metadata': {
                'labels': {'name': name},
                'name': name
            },
            'spec': {
                'replicas': 2,
                'selector': {
                    'name': name
                },
                'template': {
                    'metadata': {'labels': {'name': name}},
                    'spec': {
                        'containers': [
                            {
                                'image': 'nginx',
                                'name': 'nginx',
                                'ports': [{'containerPort': 80, 'protocol': 'TCP'}]
                            }
                        ]
                    }
                }
            }
        }

        resp = await api.create_namespaced_replication_controller(
            body=rc_manifest, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = await api.read_namespaced_replication_controller(
            name=name, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = await api.delete_namespaced_replication_controller(
            name=name, body={}, namespace='default')

    async def test_configmap_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'test-configmap-' + short_uuid()
        test_configmap = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
            },
            "data": {
                "config.json": "{\"command\":\"/usr/bin/mysqld_safe\"}",
                "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\nport = 3306\n"
            }
        }

        resp = await api.create_namespaced_config_map(
            body=test_configmap, namespace='default'
        )
        self.assertEqual(name, resp.metadata.name)

        resp = await api.read_namespaced_config_map(
            name=name, namespace='default')
        self.assertEqual(name, resp.metadata.name)

        # strategic merge patch
        resp = await api.patch_namespaced_config_map(
            name=name, namespace='default', body={'data': {'key': 'value', 'frontend.cnf': 'patched'}})

        resp = await api.read_namespaced_config_map(
            name=name, namespace='default')
        self.assertEqual(resp.data['config.json'], test_configmap['data']['config.json'])
        self.assertEqual(resp.data['frontend.cnf'], 'patched')
        self.assertEqual(resp.data['key'], 'value')

        resp = await api.delete_namespaced_config_map(
            name=name, body={}, namespace='default')

        resp = await api.list_namespaced_config_map('default', pretty=True)
        for item in resp.items:
            self.assertNotEqual(item.metadata.name, name)

    async def test_node_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        resp = await api.list_node()

        for item in resp.items:
            node = await api.read_node(name=item.metadata.name)
            self.assertTrue(len(node.metadata.labels) > 0)
            self.assertTrue(isinstance(node.metadata.labels, dict))
