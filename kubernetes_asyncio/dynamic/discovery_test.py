# Copyright 2019 The Kubernetes Authors.
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

import os
import unittest

from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.dynamic import DynamicClient
from kubernetes_asyncio.e2e_test import base


class TestDiscoverer(unittest.IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    async def test_init_cache_from_file(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            await client.resources.get(api_version='v1', kind='Node')
            mtime1 = os.path.getmtime(client.resources._Discoverer__cache_file)

        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            await client.resources.get(api_version='v1', kind='Node')
            mtime2 = os.path.getmtime(client.resources._Discoverer__cache_file)

        # test no Discoverer._write_cache called
        self.assertTrue(mtime1 == mtime2)

    async def test_cache_decoder_resource_and_subresource(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            # first invalidate cache
            await client.resources.invalidate_cache()

        # do Discoverer.__init__
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            # the resources of client will use _cache['resources'] in memory
            deploy1 = await client.resources.get(kind='Deployment', api_version="apps/v1")

        # do Discoverer.__init__
        # async with api_client.ApiClient(configuration=self.config) as apic:
            client2 = await DynamicClient(apic)
            # the resources of client will use _cache['resources'] decode from cache file
            deploy2 = await client2.resources.get(kind='Deployment', api_version="apps/v1")

        deploy2.client = deploy1.client
        # test Resource is the same
        self.assertDictEqual(deploy1.to_dict(), deploy2.to_dict())

        # test Subresource is the same
        self.assertDictEqual(deploy1.status.to_dict(), deploy2.status.to_dict())
