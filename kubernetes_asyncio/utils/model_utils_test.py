# Copyright 2026 The Kubernetes Authors.
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

from unittest import IsolatedAsyncioTestCase

from kubernetes_asyncio import client
from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.utils.model_utils import model_from_dict, model_to_dict


class ModelUtilsTest(IsolatedAsyncioTestCase):

    def test_model_from_dict_secret(self) -> None:
        manifest = {
            "apiVersion": "v1",
            "kind": "Secret",
            "metadata": {"name": "example", "namespace": "default"},
            "type": "Opaque",
            "stringData": {"username": "admin", "password": "s3cr3t"},
        }

        secret = model_from_dict(manifest, client.V1Secret)
        self.assertIsInstance(secret, client.V1Secret)
        self.assertEqual(secret.metadata.name, "example")
        self.assertEqual(secret.type, "Opaque")
        self.assertEqual(secret.string_data["username"], "admin")

    def test_model_to_dict_uses_json_keys(self) -> None:
        secret = client.V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=client.V1ObjectMeta(name="example"),
            string_data={"username": "admin"},
            type="Opaque",
        )

        payload = model_to_dict(secret)
        self.assertEqual(payload["metadata"]["name"], "example")
        self.assertIn("stringData", payload)
        self.assertNotIn("string_data", payload)
        self.assertEqual(payload["stringData"]["username"], "admin")

    async def test_roundtrip_with_shared_api_client(self) -> None:
        async with ApiClient() as api_client:
            manifest = {
                "apiVersion": "v1",
                "kind": "ConfigMap",
                "metadata": {"name": "cm"},
                "data": {"key": "value"},
            }
            cm = model_from_dict(manifest, client.V1ConfigMap, api_client=api_client)
            payload = model_to_dict(cm, api_client=api_client)
            self.assertEqual(payload["data"]["key"], "value")
            self.assertEqual(payload["metadata"]["name"], "cm")
            self.assertIsInstance(cm, client.V1ConfigMap)
