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

from asynctest import CoroutineMock, TestCase

from kubernetes_asyncio.utils import delete_from_dict, delete_from_yaml


class DeleteFromYamlTest(TestCase):

    async def test_delete_from_yaml(self):
        api_client = CoroutineMock()
        api_client.call_api = CoroutineMock()

        await delete_from_yaml(api_client, 'examples/nginx-deployment.yaml')

        # simple check for api call
        self.assertEqual(api_client.call_api.call_args[0][0],
                         '/apis/apps/v1/namespaces/{namespace}/deployments/{name}')

        self.assertEqual(api_client.call_api.call_args[0][1],
                         'DELETE')

        self.assertEqual(api_client.call_api.call_args[0][2],
                         {'name': 'nginx-deployment', 'namespace': 'default'})

    async def test_delete_from_dict(self):
        api_client = CoroutineMock()
        api_client.call_api = CoroutineMock()

        await delete_from_dict(api_client, {
            'apiVersion': 'apps/v1',
            'kind': 'Deployment',
            'metadata': {
                'name': 'nginx-deployment'},
        })

        # simple check for api call
        self.assertEqual(api_client.call_api.call_args[0][0],
                         '/apis/apps/v1/namespaces/{namespace}/deployments/{name}')
        self.assertEqual(api_client.call_api.call_args[0][1],
                         'DELETE')

        self.assertEqual(api_client.call_api.call_args[0][2],
                         {'name': 'nginx-deployment', 'namespace': 'default'})


if __name__ == '__main__':
    import asynctest
    asynctest.main()
