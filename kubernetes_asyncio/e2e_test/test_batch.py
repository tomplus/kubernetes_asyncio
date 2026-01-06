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

import uuid
from unittest import IsolatedAsyncioTestCase

from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.client.api import batch_v1_api
from kubernetes_asyncio.client.models.v1_container import V1Container
from kubernetes_asyncio.client.models.v1_job import V1Job
from kubernetes_asyncio.client.models.v1_job_spec import V1JobSpec
from kubernetes_asyncio.client.models.v1_object_meta import V1ObjectMeta
from kubernetes_asyncio.client.models.v1_pod_spec import V1PodSpec
from kubernetes_asyncio.client.models.v1_pod_template_spec import V1PodTemplateSpec
from kubernetes_asyncio.e2e_test import base


class TestClientBatch(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    async def test_job_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = batch_v1_api.BatchV1Api(client)

        name = "test-job-" + str(uuid.uuid4())
        job_manifest = V1Job(
            kind="Job",
            spec=V1JobSpec(
                template=V1PodTemplateSpec(
                    spec=V1PodSpec(
                        containers=[
                            V1Container(
                                image="busybox",
                                name=name,
                                command=["sh", "-c", "sleep 5"],
                            )
                        ],
                        restart_policy="Never",
                    ),
                    metadata=V1ObjectMeta(name=name),
                )
            ),
            api_version="batch/v1",
            metadata=V1ObjectMeta(name=name),
        )

        resp = await api.create_namespaced_job(body=job_manifest, namespace="default")
        self.assertEqual(name, resp.metadata.name)

        resp = await api.read_namespaced_job(name=name, namespace="default")
        self.assertEqual(name, resp.metadata.name)

        await api.delete_namespaced_job(name=name, body={}, namespace="default")
