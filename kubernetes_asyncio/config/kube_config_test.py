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

import base64
import datetime
import os
import shutil
import tempfile
from types import SimpleNamespace

import yaml
from asynctest import Mock, TestCase, main, patch
from six import PY3

from .config_exception import ConfigException
from .kube_config import (
    ENV_KUBECONFIG_PATH_SEPARATOR, ConfigNode, FileOrData, KubeConfigLoader,
    KubeConfigMerger, list_kube_config_contexts, load_kube_config,
    load_kube_config_from_dict, new_client_from_config,
    new_client_from_config_dict, refresh_token,
)

BEARER_TOKEN_FORMAT = "Bearer %s"

NON_EXISTING_FILE = "zz_non_existing_file_472398324"


def _base64(string):
    return base64.standard_b64encode(string.encode()).decode()


def _unpadded_base64(string):
    return base64.b64encode(string.encode()).decode().rstrip('')


def _raise_exception(st):
    raise Exception(st)


TEST_FILE_KEY = "file"
TEST_DATA_KEY = "data"
TEST_FILENAME = "test-filename"

TEST_DATA = "test-data"
TEST_DATA_BASE64 = _base64(TEST_DATA)

TEST_ANOTHER_DATA = "another-test-data"
TEST_ANOTHER_DATA_BASE64 = _base64(TEST_ANOTHER_DATA)

TEST_HOST = "test-host"
TEST_USERNAME = "me"
TEST_PASSWORD = "pass"
# token for me:pass
TEST_BASIC_TOKEN = "Basic bWU6cGFzcw=="

TEST_SSL_HOST = "https://test-host"
TEST_CERTIFICATE_AUTH = "cert-auth"
TEST_CERTIFICATE_AUTH_BASE64 = _base64(TEST_CERTIFICATE_AUTH)
TEST_CLIENT_KEY = "client-key"
TEST_CLIENT_KEY_BASE64 = _base64(TEST_CLIENT_KEY)
TEST_CLIENT_CERT = "client-cert"
TEST_CLIENT_CERT_BASE64 = _base64(TEST_CLIENT_CERT)

TEST_OIDC_TOKEN = "test-oidc-token"
TEST_OIDC_INFO = "{\"name\": \"test\"}"
TEST_OIDC_BASE = _unpadded_base64(TEST_OIDC_TOKEN) + "." + _unpadded_base64(TEST_OIDC_INFO)
TEST_OIDC_LOGIN = TEST_OIDC_BASE + "." + TEST_CLIENT_CERT_BASE64
TEST_OIDC_TOKEN = "Bearer %s" % TEST_OIDC_LOGIN
TEST_OIDC_EXP = "{\"name\": \"test\",\"exp\": 536457600}"
TEST_OIDC_EXP_BASE = _unpadded_base64(TEST_OIDC_TOKEN) + "." + _unpadded_base64(TEST_OIDC_EXP)
TEST_OIDC_EXPIRED_LOGIN = TEST_OIDC_EXP_BASE + "." + TEST_CLIENT_CERT_BASE64
TEST_OIDC_CA = _base64(TEST_CERTIFICATE_AUTH)


async def _return_async_value(val):
    return val


class BaseTestCase(TestCase):

    def setUp(self):
        self._temp_files = []

    def tearDown(self):
        for f in self._temp_files:
            os.remove(f)
        patch.stopall()

    def _create_temp_file(self, content=""):
        handler, name = tempfile.mkstemp()
        self._temp_files.append(name)
        os.write(handler, str.encode(content))
        os.close(handler)
        return name

    def expect_exception(self, func, message_part, *args, **kwargs):
        with self.assertRaises(ConfigException) as context:
            func(*args, **kwargs)
        self.assertIn(message_part, str(context.exception))

    async def async_expect_exception(self, func, message_part, *args, **kwargs):
        with self.assertRaises(ConfigException) as context:
            await func(*args, **kwargs)
        self.assertIn(message_part, str(context.exception))


class TestFileOrData(BaseTestCase):

    @staticmethod
    def get_file_content(filename):
        with open(filename) as f:
            return f.read()

    def test_file_given_file(self):
        obj = {
            TEST_FILE_KEY: self._create_temp_file(content=TEST_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_file_given_non_existing_file(self):
        temp_filename = NON_EXISTING_FILE
        obj = {TEST_FILE_KEY: temp_filename}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY)
        self.expect_exception(t.as_file, "does not exists")

    def test_file_given_data(self):
        obj = {TEST_DATA_KEY: TEST_DATA_BASE64}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_file_given_data_no_base64(self):
        obj = {TEST_DATA_KEY: TEST_DATA}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY, base64_file_content=False)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_data_given_data(self):
        obj = {TEST_DATA_KEY: TEST_DATA_BASE64}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA_BASE64, t.as_data())

    def test_data_given_file(self):
        obj = {
            TEST_FILE_KEY: self._create_temp_file(content=TEST_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY)
        self.assertEqual(TEST_DATA_BASE64, t.as_data())

    def test_data_given_file_no_base64(self):
        obj = {
            TEST_FILE_KEY: self._create_temp_file(content=TEST_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       base64_file_content=False)
        self.assertEqual(TEST_DATA, t.as_data())

    def test_data_given_file_and_data(self):
        obj = {
            TEST_DATA_KEY: TEST_DATA_BASE64,
            TEST_FILE_KEY: self._create_temp_file(
                content=TEST_ANOTHER_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA_BASE64, t.as_data())

    def test_file_given_file_and_data(self):
        obj = {
            TEST_DATA_KEY: TEST_DATA_BASE64,
            TEST_FILE_KEY: self._create_temp_file(
                content=TEST_ANOTHER_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_file_with_custom_dirname(self):
        tempfile = self._create_temp_file(content=TEST_DATA)
        tempfile_dir = os.path.dirname(tempfile)
        tempfile_basename = os.path.basename(tempfile)
        obj = {TEST_FILE_KEY: tempfile_basename}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       file_base_path=tempfile_dir)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_file_given_data_bytes(self):
        obj = {TEST_DATA_KEY: TEST_DATA_BASE64.encode()}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_file_given_data_bytes_no_base64(self):
        obj = {TEST_DATA_KEY: TEST_DATA.encode()}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY, base64_file_content=False)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))


class TestConfigNode(BaseTestCase):

    test_obj = {"key1": "test", "key2": ["a", "b", "c"],
                "key3": {"inner_key": "inner_value"},
                "with_names": [{"name": "test_name", "value": "test_value"},
                               {"name": "test_name2",
                                "value": {"key1", "test"}},
                               {"name": "test_name3", "value": [1, 2, 3]}],
                "with_names_dup": [{"name": "test_name", "value": "test_value"},
                                   {"name": "test_name",
                                    "value": {"key1", "test"}},
                                   {"name": "test_name3", "value": [1, 2, 3]}]}

    def setUp(self):
        super(TestConfigNode, self).setUp()
        self.node = ConfigNode("test_obj", self.test_obj)

    def test_normal_map_array_operations(self):
        self.assertEqual("test", self.node['key1'])
        self.assertEqual(5, len(self.node))

        self.assertEqual("test_obj/key2", self.node['key2'].name)
        self.assertEqual(["a", "b", "c"], self.node['key2'].value)
        self.assertEqual("b", self.node['key2'][1])
        self.assertEqual(3, len(self.node['key2']))

        self.assertEqual("test_obj/key3", self.node['key3'].name)
        self.assertEqual({"inner_key": "inner_value"}, self.node['key3'].value)
        self.assertEqual("inner_value", self.node['key3']["inner_key"])
        self.assertEqual(1, len(self.node['key3']))

    def test_get_with_name(self):
        node = self.node["with_names"]
        self.assertEqual(
            "test_value",
            node.get_with_name("test_name")["value"])
        self.assertTrue(
            isinstance(node.get_with_name("test_name2"), ConfigNode))
        self.assertTrue(
            isinstance(node.get_with_name("test_name3"), ConfigNode))
        self.assertEqual("test_obj/with_names[name=test_name2]",
                         node.get_with_name("test_name2").name)
        self.assertEqual("test_obj/with_names[name=test_name3]",
                         node.get_with_name("test_name3").name)

    def test_key_does_not_exists(self):
        self.expect_exception(lambda: self.node['not-exists-key'],
                              "Expected key not-exists-key in test_obj")
        self.expect_exception(lambda: self.node['key3']['not-exists-key'],
                              "Expected key not-exists-key in test_obj/key3")

    def test_get_with_name_on_invalid_object(self):
        self.expect_exception(
            lambda: self.node['key2'].get_with_name('no-name'),
            "Expected all values in test_obj/key2 list to have \'name\' key")

    def test_get_with_name_on_non_list_object(self):
        self.expect_exception(
            lambda: self.node['key3'].get_with_name('no-name'),
            "Expected test_obj/key3 to be a list")

    def test_get_with_name_on_name_does_not_exists(self):
        self.expect_exception(
            lambda: self.node['with_names'].get_with_name('no-name'),
            "Expected object with name no-name in test_obj/with_names list")

    def test_get_with_name_on_duplicate_name(self):
        self.expect_exception(
            lambda: self.node['with_names_dup'].get_with_name('test_name'),
            "Expected only one object with name test_name in test_obj/with_names_dup list")


class FakeConfig:

    FILE_KEYS = ["ssl_ca_cert", "key_file", "cert_file"]

    def __init__(self, token=None, **kwargs):
        self.api_key = {}
        if token:
            self.api_key['BearerToken'] = token

        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if len(self.__dict__) != len(other.__dict__):
            return
        for k, v in self.__dict__.items():
            if k not in other.__dict__:
                return
            if k in self.FILE_KEYS:
                if v and other.__dict__[k]:
                    try:
                        with open(v) as f1, open(other.__dict__[k]) as f2:
                            if f1.read() != f2.read():
                                return
                    except IOError:
                        # fall back to only compare filenames in case we are
                        # testing the passing of filenames to the config
                        if other.__dict__[k] != v:
                            return
                else:
                    if other.__dict__[k] != v:
                        return
            else:
                if other.__dict__[k] != v:
                    return
        return True

    def __repr__(self):
        rep = "\n"
        for k, v in self.__dict__.items():
            val = v
            if k in self.FILE_KEYS:
                try:
                    with open(v) as f:
                        val = "FILE: %s" % str.decode(f.read())
                except IOError as e:
                    val = "ERROR: %s" % str(e)
            rep += "\t%s: %s\n" % (k, val)
        return "Config(%s\n)" % rep


class TestKubeConfigLoader(BaseTestCase):
    TEST_KUBE_CONFIG = {
        "current-context": "no_user",
        "contexts": [
            {
                "name": "no_user",
                "context": {
                    "cluster": "default"
                }
            },
            {
                "name": "simple_token",
                "context": {
                    "cluster": "default",
                    "user": "simple_token"
                }
            },
            {
                "name": "gcp",
                "context": {
                    "cluster": "default",
                    "user": "gcp"
                }
            },
            {
                "name": "expired_gcp",
                "context": {
                    "cluster": "default",
                    "user": "expired_gcp"
                }
            },
            {
                "name": "oidc",
                "context": {
                    "cluster": "default",
                    "user": "oidc"
                }
            },
            {
                "name": "expired_oidc",
                "context": {
                    "cluster": "default",
                    "user": "expired_oidc"
                }
            },
            {
                "name": "expired_oidc_no_idp_cert_data",
                "context": {
                    "cluster": "default",
                    "user": "expired_oidc_no_idp_cert_data"
                }
            },
            {
                "name": "user_pass",
                "context": {
                    "cluster": "default",
                    "user": "user_pass"
                }
            },
            {
                "name": "ssl",
                "context": {
                    "cluster": "ssl",
                    "user": "ssl"
                }
            },
            {
                "name": "no_ssl_verification",
                "context": {
                    "cluster": "no_ssl_verification",
                    "user": "ssl"
                }
            },
            {
                "name": "ssl-no_file",
                "context": {
                    "cluster": "ssl-no_file",
                    "user": "ssl-no_file"
                }
            },
            {
                "name": "ssl-local-file",
                "context": {
                    "cluster": "ssl-local-file",
                    "user": "ssl-local-file"
                }
            },
            {
                "name": "non_existing_user",
                "context": {
                    "cluster": "default",
                    "user": "non_existing_user"
                }
            },
            {
                "name": "exec_cred_user",
                "context": {
                    "cluster": "default",
                    "user": "exec_cred_user"
                }
            },
        ],
        "clusters": [
            {
                "name": "default",
                "cluster": {
                    "server": TEST_HOST
                }
            },
            {
                "name": "ssl-no_file",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "certificate-authority": TEST_CERTIFICATE_AUTH,
                }
            },
            {
                "name": "ssl-local-file",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "certificate-authority": "cert_test",
                }
            },
            {
                "name": "ssl",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "certificate-authority-data": TEST_CERTIFICATE_AUTH_BASE64,
                }
            },
            {
                "name": "no_ssl_verification",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "insecure-skip-tls-verify": "true",
                }
            },
        ],
        "users": [
            {
                "name": "simple_token",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
            {
                "name": "gcp",
                "user": {
                    "auth-provider": {
                        "name": "gcp",
                        "config": {
                            "access-token": TEST_DATA_BASE64,
                        }
                    },
                    "token": TEST_DATA_BASE64,  # should be ignored
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
            {
                "name": "expired_gcp",
                "user": {
                    "auth-provider": {
                        "name": "gcp",
                        "config": {
                            "access-token": TEST_DATA_BASE64,
                            "expiry": "2000-01-01T12:00:00Z",  # always in past
                        }
                    },
                    "token": TEST_DATA_BASE64,  # should be ignored
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
            {
                "name": "oidc",
                "user": {
                    "auth-provider": {
                        "name": "oidc",
                        "config": {
                            "id-token": TEST_OIDC_LOGIN
                        }
                    }
                }
            },
            {
                "name": "expired_oidc",
                "user": {
                    "auth-provider": {
                        "name": "oidc",
                        "config": {
                            "client-id": "tectonic-kubectl",
                            "client-secret": "FAKE_SECRET",
                            "id-token": TEST_OIDC_EXPIRED_LOGIN,
                            "idp-certificate-authority-data": TEST_OIDC_CA,
                            "idp-issuer-url": "https://example.localhost/identity",
                            "refresh-token": "lucWJjEhlxZW01cXI3YmVlcYnpxNGhzk"
                        }
                    }
                }
            },
            {
                "name": "expired_oidc_no_idp_cert_data",
                "user": {
                    "auth-provider": {
                        "name": "oidc",
                        "config": {
                            "client-id": "tectonic-kubectl",
                            "client-secret": "FAKE_SECRET",
                            "id-token": TEST_OIDC_EXPIRED_LOGIN,
                            "idp-issuer-url": "https://example.localhost/identity",
                            "refresh-token": "lucWJjEhlxZW01cXI3YmVlcYnpxNGhzk"
                        }
                    }
                }
            },
            {
                "name": "user_pass",
                "user": {
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
            {
                "name": "ssl-no_file",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "client-certificate": TEST_CLIENT_CERT,
                    "client-key": TEST_CLIENT_KEY,
                }
            },
            {
                "name": "ssl-local-file",
                "user": {
                    "tokenFile": "token_file",
                    "client-certificate": "client_cert",
                    "client-key": "client_key",
                }
            },
            {
                "name": "ssl",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "client-certificate-data": TEST_CLIENT_CERT_BASE64,
                    "client-key-data": TEST_CLIENT_KEY_BASE64,
                }
            },
            {
                "name": "exec_cred_user",
                "user": {
                    "exec": {
                        "apiVersion": "client.authentication.k8s.io/v1beta1",
                        "command": "aws-iam-authenticator",
                        "args": ["token", "-i", "dummy-cluster"]
                    }
                }
            },
        ]
    }

    async def test_no_user_context(self):
        expected = FakeConfig(host=TEST_HOST)
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="no_user").load_and_set(actual)
        self.assertEqual(expected, actual)

    async def test_simple_token(self):
        expected = FakeConfig(host=TEST_HOST,
                              token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64)
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="simple_token").load_and_set(actual)
        self.assertEqual(expected, actual)

    def test_load_user_token(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="simple_token")
        self.assertTrue(loader._load_user_token())
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64, loader.token)

    async def test_gcp_no_refresh(self):
        expected = FakeConfig(
            host=TEST_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64)
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="gcp",
            get_google_credentials=lambda: _raise_exception(
                "SHOULD NOT BE CALLED")).load_and_set(actual)
        self.assertEqual(expected, actual)

    async def test_load_gcp_token_no_refresh(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="gcp",
            get_google_credentials=lambda: _raise_exception(
                "SHOULD NOT BE CALLED"))
        res = await loader.load_gcp_token()
        self.assertTrue(res)
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
                         loader.token)

    async def test_load_gcp_token_with_refresh(self):

        cred = SimpleNamespace(
            token=TEST_ANOTHER_DATA_BASE64,
            expiry=datetime.datetime.now()
        )

        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="expired_gcp",
            get_google_credentials=lambda: cred)
        res = await loader.load_gcp_token()
        self.assertTrue(res)
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_ANOTHER_DATA_BASE64,
                         loader.token)

    async def test_async_load_gcp_token_with_refresh(self):

        async def cred():
            return SimpleNamespace(
                token=TEST_ANOTHER_DATA_BASE64,
                expiry=datetime.datetime.now()
            )

        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="expired_gcp",
            get_google_credentials=cred)
        res = await loader.load_gcp_token()
        self.assertTrue(res)
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_ANOTHER_DATA_BASE64,
                         loader.token)

    async def test_oidc_no_refresh(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context='oidc',
        )
        await loader._load_authentication()
        self.assertEqual(TEST_OIDC_TOKEN, loader.token)

    @patch('kubernetes_asyncio.config.kube_config.OpenIDRequestor.refresh_token')
    async def test_oidc_with_refresh(self, mock_refresh_token):
        mock_refresh_token.return_value = {
            'id_token': 'abc123',
            'refresh_token': 'newtoken123'
        }

        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context='expired_oidc',
        )
        await loader._load_authentication()
        self.assertEqual('Bearer abc123', loader.token)

    @patch('kubernetes_asyncio.config.kube_config.OpenIDRequestor.refresh_token')
    async def test_oidc_with_refresh_no_idp_cert_data(self, mock_refresh_token):
        mock_refresh_token.return_value = {
            'id_token': 'abc123',
            'refresh_token': 'newtoken123'
        }

        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context='expired_oidc_no_idp_cert_data',
        )
        await loader._load_authentication()
        self.assertEqual('Bearer abc123', loader.token)

    async def test_invalid_oidc_configs(self):
        loader = KubeConfigLoader(config_dict=self.TEST_KUBE_CONFIG)

        with self.assertRaises(ValueError):
            loader._user = {'auth-provider': {}}
            await loader._load_oid_token()

        with self.assertRaises(ValueError):
            loader._user = {
                'auth-provider': {
                    'config': {
                        'id-token': 'notvalid'
                    },
                }
            }
            await loader._load_oid_token()

    async def test_invalid_refresh(self):
        loader = KubeConfigLoader(config_dict=self.TEST_KUBE_CONFIG)

        with self.assertRaises(ConfigException):
            await loader._refresh_oidc({'config': {}})

    @patch('kubernetes_asyncio.config.kube_config.ExecProvider.run')
    async def test_user_exec_auth(self, mock):
        token = "dummy"
        mock.return_value = {
            "token": token
        }
        expected = FakeConfig(host=TEST_HOST, api_key={
                              "BearerToken": BEARER_TOKEN_FORMAT % token})
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="exec_cred_user").load_and_set(actual)
        self.assertEqual(expected, actual)

    async def test_user_pass(self):
        expected = FakeConfig(host=TEST_HOST, token=TEST_BASIC_TOKEN)
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="user_pass").load_and_set(actual)
        self.assertEqual(expected, actual)

    def test_load_user_pass_token(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="user_pass")
        self.assertTrue(loader._load_user_pass_token())
        self.assertEqual(TEST_BASIC_TOKEN, loader.token)

    async def test_ssl_no_cert_files(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="ssl-no_file")
        await self.async_expect_exception(
            loader.load_and_set,
            "does not exists",
            FakeConfig())

    async def test_ssl(self):
        expected = FakeConfig(
            host=TEST_SSL_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
            cert_file=self._create_temp_file(TEST_CLIENT_CERT),
            key_file=self._create_temp_file(TEST_CLIENT_KEY),
            ssl_ca_cert=self._create_temp_file(TEST_CERTIFICATE_AUTH)
        )
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="ssl").load_and_set(actual)
        self.assertEqual(expected, actual)

    async def test_ssl_no_verification(self):
        expected = FakeConfig(
            host=TEST_SSL_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
            cert_file=self._create_temp_file(TEST_CLIENT_CERT),
            key_file=self._create_temp_file(TEST_CLIENT_KEY),
            verify_ssl=False,
            ssl_ca_cert=None,
        )
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="no_ssl_verification").load_and_set(actual)
        self.assertEqual(expected, actual)

    def test_list_contexts(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="no_user")
        actual_contexts = loader.list_contexts()
        expected_contexts = ConfigNode("", self.TEST_KUBE_CONFIG)['contexts']
        for actual in actual_contexts:
            expected = expected_contexts.get_with_name(actual['name'])
            self.assertEqual(expected.value, actual)

    def test_current_context(self):
        loader = KubeConfigLoader(config_dict=self.TEST_KUBE_CONFIG)
        expected_contexts = ConfigNode("", self.TEST_KUBE_CONFIG)['contexts']
        self.assertEqual(expected_contexts.get_with_name("no_user").value,
                         loader.current_context)

    def test_set_active_context(self):
        loader = KubeConfigLoader(config_dict=self.TEST_KUBE_CONFIG)
        loader.set_active_context("ssl")
        expected_contexts = ConfigNode("", self.TEST_KUBE_CONFIG)['contexts']
        self.assertEqual(expected_contexts.get_with_name("ssl").value,
                         loader.current_context)

    async def test_ssl_with_relative_ssl_files(self):
        expected = FakeConfig(
            host=TEST_SSL_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
            cert_file=self._create_temp_file(TEST_CLIENT_CERT),
            key_file=self._create_temp_file(TEST_CLIENT_KEY),
            ssl_ca_cert=self._create_temp_file(TEST_CERTIFICATE_AUTH)
        )
        try:
            temp_dir = tempfile.mkdtemp()
            actual = FakeConfig()
            with open(os.path.join(temp_dir, "cert_test"), "wb") as fd:
                fd.write(TEST_CERTIFICATE_AUTH.encode())
            with open(os.path.join(temp_dir, "client_cert"), "wb") as fd:
                fd.write(TEST_CLIENT_CERT.encode())
            with open(os.path.join(temp_dir, "client_key"), "wb") as fd:
                fd.write(TEST_CLIENT_KEY.encode())
            with open(os.path.join(temp_dir, "token_file"), "wb") as fd:
                fd.write(TEST_DATA_BASE64.encode())
            await KubeConfigLoader(
                config_dict=self.TEST_KUBE_CONFIG,
                active_context="ssl-local-file",
                config_base_path=temp_dir).load_and_set(actual)
            self.assertEqual(expected, actual)
        finally:
            shutil.rmtree(temp_dir)

    async def test_load_kube_config(self):
        expected = FakeConfig(host=TEST_HOST,
                              token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64)
        config_file = self._create_temp_file(yaml.safe_dump(self.TEST_KUBE_CONFIG))
        actual = FakeConfig()
        await load_kube_config(config_file=config_file,
                               context="simple_token",
                               client_configuration=actual)
        self.assertEqual(expected, actual)

    async def test_load_kube_config_from_dict(self):
        expected = FakeConfig(host=TEST_HOST,
                              token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64)
        actual = FakeConfig()
        await load_kube_config_from_dict(config_dict=self.TEST_KUBE_CONFIG,
                                         context="simple_token",
                                         client_configuration=actual)
        self.assertEqual(expected, actual)

    async def test_load_kube_config_from_dict_with_temp_file_path(self):
        expected = FakeConfig(
            host=TEST_SSL_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
            cert_file=self._create_temp_file(TEST_CLIENT_CERT),
            key_file=self._create_temp_file(TEST_CLIENT_KEY),
            ssl_ca_cert=self._create_temp_file(TEST_CERTIFICATE_AUTH)
        )
        actual = FakeConfig()

        tmp_path = tempfile.mkdtemp('test_temp_file_path')

        await load_kube_config_from_dict(config_dict=self.TEST_KUBE_CONFIG,
                                         context="ssl",
                                         client_configuration=actual,
                                         temp_file_path=tmp_path)
        self.assertEqual(expected, actual)

        # 3 files has to be created within temp_file_path
        self.assertEqual(len(os.listdir(tmp_path)), 3)

    def test_list_kube_config_contexts(self):
        config_file = self._create_temp_file(yaml.safe_dump(self.TEST_KUBE_CONFIG))
        contexts, active_context = list_kube_config_contexts(
            config_file=config_file)
        self.assertDictEqual(self.TEST_KUBE_CONFIG['contexts'][0],
                             active_context)
        if PY3:
            self.assertCountEqual(self.TEST_KUBE_CONFIG['contexts'],
                                  contexts)
        else:
            self.assertItemsEqual(self.TEST_KUBE_CONFIG['contexts'],
                                  contexts)

    async def test_new_client_from_config(self):
        config_file = self._create_temp_file(yaml.safe_dump(self.TEST_KUBE_CONFIG))
        client = await new_client_from_config(
            config_file=config_file, context="simple_token")
        self.assertEqual(TEST_HOST, client.configuration.host)
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
                         client.configuration.api_key['BearerToken'])

    async def test_new_client_from_config_dict(self):
        client = await new_client_from_config_dict(
            config_dict=self.TEST_KUBE_CONFIG, context="simple_token")
        self.assertEqual(TEST_HOST, client.configuration.host)
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
                         client.configuration.api_key['BearerToken'])

    async def test_no_users_section(self):
        expected = FakeConfig(host=TEST_HOST)
        actual = FakeConfig()
        test_kube_config = self.TEST_KUBE_CONFIG.copy()
        del test_kube_config['users']
        await KubeConfigLoader(
            config_dict=test_kube_config,
            active_context="gcp").load_and_set(actual)
        self.assertEqual(expected, actual)

    async def test_non_existing_user(self):
        expected = FakeConfig(host=TEST_HOST)
        actual = FakeConfig()
        await KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="non_existing_user").load_and_set(actual)
        self.assertEqual(expected, actual)

    async def test_refresh_token(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="gcp",
            get_google_credentials=lambda: _raise_exception(
                "SHOULD NOT BE CALLED"))
        mock_sleep = patch('asyncio.sleep').start()
        mock_sleep.side_effect = [0, AssertionError]

        mock_config = Mock()
        mock_config.api_key = {}

        with self.assertRaises(AssertionError):
            await refresh_token(loader, mock_config)

        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
                         loader.token)


class TestKubeConfigMerger(BaseTestCase):
    TEST_KUBE_CONFIG_PART1 = {
        "current-context": "no_user",
        "contexts": [
            {
                "name": "no_user",
                "context": {
                    "cluster": "default"
                }
            },
        ],
        "clusters": [
            {
                "name": "default",
                "cluster": {
                    "server": TEST_HOST
                }
            },
        ],
        "users": []
    }

    TEST_KUBE_CONFIG_PART2 = {
        "current-context": "",
        "contexts": [
            {
                "name": "ssl",
                "context": {
                    "cluster": "ssl",
                    "user": "ssl"
                }
            },
            {
                "name": "simple_token",
                "context": {
                    "cluster": "default",
                    "user": "simple_token"
                }
            },
        ],
        "clusters": [
            {
                "name": "ssl",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "certificate-authority-data":
                        TEST_CERTIFICATE_AUTH_BASE64,
                }
            },
        ],
        "users": [
            {
                "name": "ssl",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "client-certificate-data": TEST_CLIENT_CERT_BASE64,
                    "client-key-data": TEST_CLIENT_KEY_BASE64,
                }
            },
        ]
    }

    TEST_KUBE_CONFIG_PART3 = {
        "current-context": "no_user",
        "contexts": [
            {
                "name": "expired_oidc",
                "context": {
                    "cluster": "default",
                    "user": "expired_oidc"
                }
            },
            {
                "name": "ssl",
                "context": {
                    "cluster": "skipped-part2-defined-this-context",
                    "user": "skipped"
                }
            },
        ],
        "clusters": [
        ],
        "users": [
            {
                "name": "expired_oidc",
                "user": {
                    "auth-provider": {
                        "name": "oidc",
                        "config": {
                            "client-id": "tectonic-kubectl",
                            "client-secret": "FAKE_SECRET",
                            "id-token": TEST_OIDC_EXPIRED_LOGIN,
                            "idp-certificate-authority-data": TEST_OIDC_CA,
                            "idp-issuer-url": "https://example.org/identity",
                            "refresh-token":
                                "lucWJjEhlxZW01cXI3YmVlcYnpxNGhzk"
                        }
                    }
                }
            },
            {
                "name": "simple_token",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
        ]
    }

    def _create_multi_config(self):
        files = []
        for part in (
                self.TEST_KUBE_CONFIG_PART1,
                self.TEST_KUBE_CONFIG_PART2,
                self.TEST_KUBE_CONFIG_PART3):
            files.append(self._create_temp_file(yaml.safe_dump(part)))
        return ENV_KUBECONFIG_PATH_SEPARATOR.join(files)

    def test_list_kube_config_contexts(self):
        kubeconfigs = self._create_multi_config()
        expected_contexts = [
            {'context': {'cluster': 'default'}, 'name': 'no_user'},
            {'context': {'cluster': 'ssl', 'user': 'ssl'}, 'name': 'ssl'},
            {'context': {'cluster': 'default', 'user': 'simple_token'},
             'name': 'simple_token'},
            {'context': {'cluster': 'default', 'user': 'expired_oidc'}, 'name': 'expired_oidc'}]

        contexts, active_context = list_kube_config_contexts(
            config_file=kubeconfigs)

        self.assertEqual(contexts, expected_contexts)
        self.assertEqual(active_context, expected_contexts[0])

    async def test_new_client_from_config(self):
        kubeconfigs = self._create_multi_config()
        client = await new_client_from_config(
            config_file=kubeconfigs, context="simple_token")
        self.assertEqual(TEST_HOST, client.configuration.host)
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
                         client.configuration.api_key['BearerToken'])

    def test_save_changes(self):
        kubeconfigs = self._create_multi_config()

        # load configuration, update token, save config
        kconf = KubeConfigMerger(kubeconfigs)
        user = kconf.config['users'].get_with_name('expired_oidc')['user']
        provider = user['auth-provider']['config']
        provider.value['id-token'] = "token-changed"
        kconf.save_changes()

        # re-read configuration
        kconf = KubeConfigMerger(kubeconfigs)
        user = kconf.config['users'].get_with_name('expired_oidc')['user']
        provider = user['auth-provider']['config']

        # new token
        self.assertEqual(provider.value['id-token'], "token-changed")


if __name__ == '__main__':
    main()
