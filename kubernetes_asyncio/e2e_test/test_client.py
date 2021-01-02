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

import asynctest

from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.client.api import core_v1_api
from kubernetes_asyncio.e2e_test import base
from kubernetes_asyncio.stream import WsApiClient


def short_uuid():
    id = str(uuid.uuid4())
    return id[-12:]


class TestClient(asynctest.TestCase):

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

        service_manifest['spec']['ports'] = [
            {'name': 'new',
             'port': 8080,
             'protocol': 'TCP',
             'targetPort': 8080}
        ]
        resp = await api.patch_namespaced_service(
            body=service_manifest,
            name=name,
            namespace='default'
        )
        self.assertEqual(2, len(resp.spec.ports))
        self.assertTrue(resp.status)

        resp = await api.delete_namespaced_service(name=name, body={}, namespace='default')

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

        test_configmap['data']['config.json'] = "{}"
        resp = await api.patch_namespaced_config_map(
            name=name, namespace='default', body=test_configmap)

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


if __name__ == '__main__':
    asynctest.main()
