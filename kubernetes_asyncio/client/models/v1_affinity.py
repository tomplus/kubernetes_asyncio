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


class V1Affinity(object):
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
        'node_affinity': 'V1NodeAffinity',
        'pod_affinity': 'V1PodAffinity',
        'pod_anti_affinity': 'V1PodAntiAffinity'
    }

    attribute_map = {
        'node_affinity': 'nodeAffinity',
        'pod_affinity': 'podAffinity',
        'pod_anti_affinity': 'podAntiAffinity'
    }

    def __init__(self, node_affinity=None, pod_affinity=None, pod_anti_affinity=None, local_vars_configuration=None):  # noqa: E501
        """V1Affinity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._node_affinity = None
        self._pod_affinity = None
        self._pod_anti_affinity = None
        self.discriminator = None

        if node_affinity is not None:
            self.node_affinity = node_affinity
        if pod_affinity is not None:
            self.pod_affinity = pod_affinity
        if pod_anti_affinity is not None:
            self.pod_anti_affinity = pod_anti_affinity

    @property
    def node_affinity(self):
        """Gets the node_affinity of this V1Affinity.  # noqa: E501


        :return: The node_affinity of this V1Affinity.  # noqa: E501
        :rtype: V1NodeAffinity
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        """Sets the node_affinity of this V1Affinity.


        :param node_affinity: The node_affinity of this V1Affinity.  # noqa: E501
        :type node_affinity: V1NodeAffinity
        """

        self._node_affinity = node_affinity

    @property
    def pod_affinity(self):
        """Gets the pod_affinity of this V1Affinity.  # noqa: E501


        :return: The pod_affinity of this V1Affinity.  # noqa: E501
        :rtype: V1PodAffinity
        """
        return self._pod_affinity

    @pod_affinity.setter
    def pod_affinity(self, pod_affinity):
        """Sets the pod_affinity of this V1Affinity.


        :param pod_affinity: The pod_affinity of this V1Affinity.  # noqa: E501
        :type pod_affinity: V1PodAffinity
        """

        self._pod_affinity = pod_affinity

    @property
    def pod_anti_affinity(self):
        """Gets the pod_anti_affinity of this V1Affinity.  # noqa: E501


        :return: The pod_anti_affinity of this V1Affinity.  # noqa: E501
        :rtype: V1PodAntiAffinity
        """
        return self._pod_anti_affinity

    @pod_anti_affinity.setter
    def pod_anti_affinity(self, pod_anti_affinity):
        """Sets the pod_anti_affinity of this V1Affinity.


        :param pod_anti_affinity: The pod_anti_affinity of this V1Affinity.  # noqa: E501
        :type pod_anti_affinity: V1PodAntiAffinity
        """

        self._pod_anti_affinity = pod_anti_affinity

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
        if not isinstance(other, V1Affinity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Affinity):
            return True

        return self.to_dict() != other.to_dict()
