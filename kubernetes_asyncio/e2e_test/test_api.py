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

import os
import uuid
from unittest import IsolatedAsyncioTestCase

import yaml

from kubernetes_asyncio import utils
from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.client.api import apps_v1_api
from kubernetes_asyncio.client.configuration import Configuration
from kubernetes_asyncio.client.models import v1_delete_options
from kubernetes_asyncio.client.models.v1_container import V1Container
from kubernetes_asyncio.client.models.v1_daemon_set import V1DaemonSet
from kubernetes_asyncio.client.models.v1_daemon_set_spec import V1DaemonSetSpec
from kubernetes_asyncio.client.models.v1_daemon_set_update_strategy import (
    V1DaemonSetUpdateStrategy,
)
from kubernetes_asyncio.client.models.v1_label_selector import V1LabelSelector
from kubernetes_asyncio.client.models.v1_object_meta import V1ObjectMeta
from kubernetes_asyncio.client.models.v1_pod_spec import V1PodSpec
from kubernetes_asyncio.client.models.v1_pod_template_spec import V1PodTemplateSpec
from kubernetes_asyncio.e2e_test import base


class TestClientApi(IsolatedAsyncioTestCase):
    config: Configuration

    @classmethod
    def setUpClass(cls) -> None:
        cls.config = base.get_e2e_configuration()

    async def test_create_deployment(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = apps_v1_api.AppsV1Api(client)
        name = "nginx-deployment-" + str(uuid.uuid4())
        deployment = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: %s
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
"""
        resp = await api.create_namespaced_deployment(
            body=yaml.safe_load(deployment % name), namespace="default"
        )
        resp = await api.read_namespaced_deployment(name, "default")
        self.assertIsNotNone(resp)

        options = v1_delete_options.V1DeleteOptions()
        resp_delete = await api.delete_namespaced_deployment(
            name, "default", body=options
        )
        self.assertIsNotNone(resp_delete)

    async def test_create_deployment_from_yaml_file(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = apps_v1_api.AppsV1Api(client)
        name = "nginx-deployment-" + str(uuid.uuid4())
        tempfile = "temp.yaml"
        deployment = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: %s
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
"""
        with open(tempfile, "w") as f:
            f.write(deployment % name)
        resp = await utils.create_from_yaml(client, tempfile)
        os.remove(tempfile)
        resp = await api.read_namespaced_deployment(name, "default")
        self.assertIsNotNone(resp)

        options = v1_delete_options.V1DeleteOptions()
        resp = await api.delete_namespaced_deployment(name, "default", body=options)

    async def test_create_daemonset(self) -> None:
        client = api_client.ApiClient(configuration=self.config)
        api = apps_v1_api.AppsV1Api(client)
        name = "nginx-app-" + str(uuid.uuid4())
        daemonset = V1DaemonSet(
            api_version="apps/v1",
            kind="DaemonSet",
            metadata=V1ObjectMeta(
                labels={"app": "nginx"},
                name=name,
            ),
            spec=V1DaemonSetSpec(
                selector=V1LabelSelector(match_labels={"app": "nginx"}),
                template=V1PodTemplateSpec(
                    metadata=V1ObjectMeta(
                        labels={"app": "nginx"},
                        name=name,
                    ),
                    spec=V1PodSpec(
                        containers=[
                            V1Container(name="nginx-app", image="nginx:1.10"),
                        ],
                    ),
                ),
                update_strategy=V1DaemonSetUpdateStrategy(type="RollingUpdate"),
            ),
        )
        resp = await api.create_namespaced_daemon_set("default", body=daemonset)
        resp = await api.read_namespaced_daemon_set(name, "default")
        self.assertIsNotNone(resp)

        options = v1_delete_options.V1DeleteOptions()
        resp_delete = await api.delete_namespaced_daemon_set(
            name, "default", body=options
        )
        self.assertIsNotNone(resp_delete)
