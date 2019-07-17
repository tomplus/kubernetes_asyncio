# coding: utf-8

from __future__ import absolute_import

import unittest

from kubernetes_asyncio.utils import create_from_yaml

import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException


class TestCreateFromYAML(unittest.TestCase):
    """ExtensionsV1beta1IDRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateFromYAML(self):
        """Test testCreateFromYAML"""
        # The only function there is will deploy a yaml straight to a kubernetes cluster
        # So there is not much to unit test... There is a e2e test doing this.
        pass


if __name__ == '__main__':
    unittest.main()
