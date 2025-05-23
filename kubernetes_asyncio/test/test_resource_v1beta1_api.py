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
from kubernetes_asyncio.client.api.resource_v1beta1_api import ResourceV1beta1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestResourceV1beta1Api(unittest.IsolatedAsyncioTestCase):
    """ResourceV1beta1Api unit test stubs"""

    async def asyncSetUp(self):
        self.api = kubernetes_asyncio.client.api.resource_v1beta1_api.ResourceV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_device_class(self):
        """Test case for create_device_class

        """
        pass

    def test_create_namespaced_resource_claim(self):
        """Test case for create_namespaced_resource_claim

        """
        pass

    def test_create_namespaced_resource_claim_template(self):
        """Test case for create_namespaced_resource_claim_template

        """
        pass

    def test_create_resource_slice(self):
        """Test case for create_resource_slice

        """
        pass

    def test_delete_collection_device_class(self):
        """Test case for delete_collection_device_class

        """
        pass

    def test_delete_collection_namespaced_resource_claim(self):
        """Test case for delete_collection_namespaced_resource_claim

        """
        pass

    def test_delete_collection_namespaced_resource_claim_template(self):
        """Test case for delete_collection_namespaced_resource_claim_template

        """
        pass

    def test_delete_collection_resource_slice(self):
        """Test case for delete_collection_resource_slice

        """
        pass

    def test_delete_device_class(self):
        """Test case for delete_device_class

        """
        pass

    def test_delete_namespaced_resource_claim(self):
        """Test case for delete_namespaced_resource_claim

        """
        pass

    def test_delete_namespaced_resource_claim_template(self):
        """Test case for delete_namespaced_resource_claim_template

        """
        pass

    def test_delete_resource_slice(self):
        """Test case for delete_resource_slice

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_device_class(self):
        """Test case for list_device_class

        """
        pass

    def test_list_namespaced_resource_claim(self):
        """Test case for list_namespaced_resource_claim

        """
        pass

    def test_list_namespaced_resource_claim_template(self):
        """Test case for list_namespaced_resource_claim_template

        """
        pass

    def test_list_resource_claim_for_all_namespaces(self):
        """Test case for list_resource_claim_for_all_namespaces

        """
        pass

    def test_list_resource_claim_template_for_all_namespaces(self):
        """Test case for list_resource_claim_template_for_all_namespaces

        """
        pass

    def test_list_resource_slice(self):
        """Test case for list_resource_slice

        """
        pass

    def test_patch_device_class(self):
        """Test case for patch_device_class

        """
        pass

    def test_patch_namespaced_resource_claim(self):
        """Test case for patch_namespaced_resource_claim

        """
        pass

    def test_patch_namespaced_resource_claim_status(self):
        """Test case for patch_namespaced_resource_claim_status

        """
        pass

    def test_patch_namespaced_resource_claim_template(self):
        """Test case for patch_namespaced_resource_claim_template

        """
        pass

    def test_patch_resource_slice(self):
        """Test case for patch_resource_slice

        """
        pass

    def test_read_device_class(self):
        """Test case for read_device_class

        """
        pass

    def test_read_namespaced_resource_claim(self):
        """Test case for read_namespaced_resource_claim

        """
        pass

    def test_read_namespaced_resource_claim_status(self):
        """Test case for read_namespaced_resource_claim_status

        """
        pass

    def test_read_namespaced_resource_claim_template(self):
        """Test case for read_namespaced_resource_claim_template

        """
        pass

    def test_read_resource_slice(self):
        """Test case for read_resource_slice

        """
        pass

    def test_replace_device_class(self):
        """Test case for replace_device_class

        """
        pass

    def test_replace_namespaced_resource_claim(self):
        """Test case for replace_namespaced_resource_claim

        """
        pass

    def test_replace_namespaced_resource_claim_status(self):
        """Test case for replace_namespaced_resource_claim_status

        """
        pass

    def test_replace_namespaced_resource_claim_template(self):
        """Test case for replace_namespaced_resource_claim_template

        """
        pass

    def test_replace_resource_slice(self):
        """Test case for replace_resource_slice

        """
        pass


if __name__ == '__main__':
    unittest.main()
