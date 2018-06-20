# Copyright 2016 The Kubernetes Authors.
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

from asynctest import CoroutineMock, Mock, TestCase, patch

import kubernetes_asyncio
from kubernetes_asyncio.watch import Watch


class WatchTest(TestCase):

    async def test_watch_with_decode(self):
        fake_resp = CoroutineMock()
        fake_resp.content.readline = CoroutineMock()
        fake_resp.content.readline.side_effect = [
            '{"type": "ADDED", "object": {"metadata": {"name": "test1"},"spec": {}, "status": {}}}',
            '{"type": "ADDED", "object": {"metadata": {"name": "test2"},"spec": {}, "status": {}}}',
            '{"type": "ADDED", "object": {"metadata": {"name": "test3"},"spec": {}, "status": {}}}',
            'should_not_happened']

        fake_api = Mock()
        fake_api.get_namespaces = CoroutineMock(return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':return: V1NamespaceList'

        watch = kubernetes_asyncio.watch.Watch()
        count = 1
        async for e in watch.stream(fake_api.get_namespaces):
            self.assertEqual("ADDED", e['type'])
            # make sure decoder worked and we got a model with the right name
            self.assertEqual("test%d" % count, e['object'].metadata.name)
            count += 1
            # make sure we can stop the watch and the last event with won't be
            # returned
            if count == 4:
                watch.stop()

        fake_api.get_namespaces.assert_called_once_with(
            _preload_content=False, watch=True)

    def test_unmarshal_with_float_object(self):
        w = Watch()
        event = w.unmarshal_event('{"type": "ADDED", "object": 1}', 'float')
        self.assertEqual("ADDED", event['type'])
        self.assertEqual(1.0, event['object'])
        self.assertTrue(isinstance(event['object'], float))
        self.assertEqual(1, event['raw_object'])

    def test_unmarshal_with_no_return_type(self):
        w = Watch()
        event = w.unmarshal_event(
            '{"type": "ADDED", "object": ["test1"]}', None)
        self.assertEqual("ADDED", event['type'])
        self.assertEqual(["test1"], event['object'])
        self.assertEqual(["test1"], event['raw_object'])

    async def test_unmarshall_k8s_error_response(self):
        """Never parse messages of type ERROR.

        This test uses an actually recorded error, in this case for an outdated
        resource version.

        """
        # An actual error response sent by K8s during testing.
        k8s_err = {
            'type': 'ERROR',
            'object': {
                'kind': 'Status', 'apiVersion': 'v1', 'metadata': {},
                'status': 'Failure',
                'message': 'too old resource version: 1 (8146471)',
                'reason': 'Gone', 'code': 410
            }
        }

        ret = Watch().unmarshal_event(json.dumps(k8s_err), None)
        assert ret['type'] == k8s_err['type']
        assert ret['object'] == ret['raw_object'] == k8s_err['object']

    async def test_watch_with_exception(self):
        fake_resp = CoroutineMock()
        fake_resp.content.readline = CoroutineMock()
        fake_resp.content.readline.side_effect = KeyError("expected")
        fake_api = Mock()
        fake_api.get_namespaces = CoroutineMock(return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':return: V1NamespaceList'

        with self.assertRaises(KeyError):
            watch = kubernetes_asyncio.watch.Watch()
            async for e in watch.stream(fake_api.get_namespaces, timeout_seconds=10):
                pass


if __name__ == '__main__':
    import asynctest
    asynctest.main()
