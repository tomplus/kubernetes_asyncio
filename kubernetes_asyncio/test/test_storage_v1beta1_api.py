# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.32.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.storage_v1beta1_api import StorageV1beta1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestStorageV1beta1Api(unittest.IsolatedAsyncioTestCase):
    """StorageV1beta1Api unit test stubs"""

    async def asyncSetUp(self):
        self.api = kubernetes_asyncio.client.api.storage_v1beta1_api.StorageV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_volume_attributes_class(self):
        """Test case for create_volume_attributes_class

        """
        pass

    def test_delete_collection_volume_attributes_class(self):
        """Test case for delete_collection_volume_attributes_class

        """
        pass

    def test_delete_volume_attributes_class(self):
        """Test case for delete_volume_attributes_class

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_volume_attributes_class(self):
        """Test case for list_volume_attributes_class

        """
        pass

    def test_patch_volume_attributes_class(self):
        """Test case for patch_volume_attributes_class

        """
        pass

    def test_read_volume_attributes_class(self):
        """Test case for read_volume_attributes_class

        """
        pass

    def test_replace_volume_attributes_class(self):
        """Test case for replace_volume_attributes_class

        """
        pass


if __name__ == '__main__':
    unittest.main()
