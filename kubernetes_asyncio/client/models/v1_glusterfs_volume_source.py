# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.32.3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1GlusterfsVolumeSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'endpoints': 'str',
        'path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'path': 'path',
        'read_only': 'readOnly'
    }

    def __init__(self, endpoints=None, path=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        """V1GlusterfsVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._endpoints = None
        self._path = None
        self._read_only = None
        self.discriminator = None

        self.endpoints = endpoints
        self.path = path
        if read_only is not None:
            self.read_only = read_only

    @property
    def endpoints(self):
        """Gets the endpoints of this V1GlusterfsVolumeSource.  # noqa: E501

        endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :return: The endpoints of this V1GlusterfsVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this V1GlusterfsVolumeSource.

        endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :param endpoints: The endpoints of this V1GlusterfsVolumeSource.  # noqa: E501
        :type endpoints: str
        """
        if self.local_vars_configuration.client_side_validation and endpoints is None:  # noqa: E501
            raise ValueError("Invalid value for `endpoints`, must not be `None`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def path(self):
        """Gets the path of this V1GlusterfsVolumeSource.  # noqa: E501

        path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :return: The path of this V1GlusterfsVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1GlusterfsVolumeSource.

        path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :param path: The path of this V1GlusterfsVolumeSource.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def read_only(self):
        """Gets the read_only of this V1GlusterfsVolumeSource.  # noqa: E501

        readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :return: The read_only of this V1GlusterfsVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1GlusterfsVolumeSource.

        readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod  # noqa: E501

        :param read_only: The read_only of this V1GlusterfsVolumeSource.  # noqa: E501
        :type read_only: bool
        """

        self._read_only = read_only

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1GlusterfsVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1GlusterfsVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
