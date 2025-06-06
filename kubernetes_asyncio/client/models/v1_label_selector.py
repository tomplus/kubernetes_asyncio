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


class V1LabelSelector(object):
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
        'match_expressions': 'list[V1LabelSelectorRequirement]',
        'match_labels': 'dict(str, str)'
    }

    attribute_map = {
        'match_expressions': 'matchExpressions',
        'match_labels': 'matchLabels'
    }

    def __init__(self, match_expressions=None, match_labels=None, local_vars_configuration=None):  # noqa: E501
        """V1LabelSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._match_expressions = None
        self._match_labels = None
        self.discriminator = None

        if match_expressions is not None:
            self.match_expressions = match_expressions
        if match_labels is not None:
            self.match_labels = match_labels

    @property
    def match_expressions(self):
        """Gets the match_expressions of this V1LabelSelector.  # noqa: E501

        matchExpressions is a list of label selector requirements. The requirements are ANDed.  # noqa: E501

        :return: The match_expressions of this V1LabelSelector.  # noqa: E501
        :rtype: list[V1LabelSelectorRequirement]
        """
        return self._match_expressions

    @match_expressions.setter
    def match_expressions(self, match_expressions):
        """Sets the match_expressions of this V1LabelSelector.

        matchExpressions is a list of label selector requirements. The requirements are ANDed.  # noqa: E501

        :param match_expressions: The match_expressions of this V1LabelSelector.  # noqa: E501
        :type match_expressions: list[V1LabelSelectorRequirement]
        """

        self._match_expressions = match_expressions

    @property
    def match_labels(self):
        """Gets the match_labels of this V1LabelSelector.  # noqa: E501

        matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.  # noqa: E501

        :return: The match_labels of this V1LabelSelector.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._match_labels

    @match_labels.setter
    def match_labels(self, match_labels):
        """Sets the match_labels of this V1LabelSelector.

        matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.  # noqa: E501

        :param match_labels: The match_labels of this V1LabelSelector.  # noqa: E501
        :type match_labels: dict(str, str)
        """

        self._match_labels = match_labels

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
        if not isinstance(other, V1LabelSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1LabelSelector):
            return True

        return self.to_dict() != other.to_dict()
