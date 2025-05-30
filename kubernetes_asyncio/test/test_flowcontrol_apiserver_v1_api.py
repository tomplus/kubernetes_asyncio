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
from kubernetes_asyncio.client.api.flowcontrol_apiserver_v1_api import FlowcontrolApiserverV1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestFlowcontrolApiserverV1Api(unittest.IsolatedAsyncioTestCase):
    """FlowcontrolApiserverV1Api unit test stubs"""

    async def asyncSetUp(self):
        self.api = kubernetes_asyncio.client.api.flowcontrol_apiserver_v1_api.FlowcontrolApiserverV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_flow_schema(self):
        """Test case for create_flow_schema

        """
        pass

    def test_create_priority_level_configuration(self):
        """Test case for create_priority_level_configuration

        """
        pass

    def test_delete_collection_flow_schema(self):
        """Test case for delete_collection_flow_schema

        """
        pass

    def test_delete_collection_priority_level_configuration(self):
        """Test case for delete_collection_priority_level_configuration

        """
        pass

    def test_delete_flow_schema(self):
        """Test case for delete_flow_schema

        """
        pass

    def test_delete_priority_level_configuration(self):
        """Test case for delete_priority_level_configuration

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_flow_schema(self):
        """Test case for list_flow_schema

        """
        pass

    def test_list_priority_level_configuration(self):
        """Test case for list_priority_level_configuration

        """
        pass

    def test_patch_flow_schema(self):
        """Test case for patch_flow_schema

        """
        pass

    def test_patch_flow_schema_status(self):
        """Test case for patch_flow_schema_status

        """
        pass

    def test_patch_priority_level_configuration(self):
        """Test case for patch_priority_level_configuration

        """
        pass

    def test_patch_priority_level_configuration_status(self):
        """Test case for patch_priority_level_configuration_status

        """
        pass

    def test_read_flow_schema(self):
        """Test case for read_flow_schema

        """
        pass

    def test_read_flow_schema_status(self):
        """Test case for read_flow_schema_status

        """
        pass

    def test_read_priority_level_configuration(self):
        """Test case for read_priority_level_configuration

        """
        pass

    def test_read_priority_level_configuration_status(self):
        """Test case for read_priority_level_configuration_status

        """
        pass

    def test_replace_flow_schema(self):
        """Test case for replace_flow_schema

        """
        pass

    def test_replace_flow_schema_status(self):
        """Test case for replace_flow_schema_status

        """
        pass

    def test_replace_priority_level_configuration(self):
        """Test case for replace_priority_level_configuration

        """
        pass

    def test_replace_priority_level_configuration_status(self):
        """Test case for replace_priority_level_configuration_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
