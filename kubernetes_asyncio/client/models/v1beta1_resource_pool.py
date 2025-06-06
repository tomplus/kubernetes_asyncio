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


class V1beta1ResourcePool(object):
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
        'generation': 'int',
        'name': 'str',
        'resource_slice_count': 'int'
    }

    attribute_map = {
        'generation': 'generation',
        'name': 'name',
        'resource_slice_count': 'resourceSliceCount'
    }

    def __init__(self, generation=None, name=None, resource_slice_count=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1ResourcePool - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._generation = None
        self._name = None
        self._resource_slice_count = None
        self.discriminator = None

        self.generation = generation
        self.name = name
        self.resource_slice_count = resource_slice_count

    @property
    def generation(self):
        """Gets the generation of this V1beta1ResourcePool.  # noqa: E501

        Generation tracks the change in a pool over time. Whenever a driver changes something about one or more of the resources in a pool, it must change the generation in all ResourceSlices which are part of that pool. Consumers of ResourceSlices should only consider resources from the pool with the highest generation number. The generation may be reset by drivers, which should be fine for consumers, assuming that all ResourceSlices in a pool are updated to match or deleted.  Combined with ResourceSliceCount, this mechanism enables consumers to detect pools which are comprised of multiple ResourceSlices and are in an incomplete state.  # noqa: E501

        :return: The generation of this V1beta1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this V1beta1ResourcePool.

        Generation tracks the change in a pool over time. Whenever a driver changes something about one or more of the resources in a pool, it must change the generation in all ResourceSlices which are part of that pool. Consumers of ResourceSlices should only consider resources from the pool with the highest generation number. The generation may be reset by drivers, which should be fine for consumers, assuming that all ResourceSlices in a pool are updated to match or deleted.  Combined with ResourceSliceCount, this mechanism enables consumers to detect pools which are comprised of multiple ResourceSlices and are in an incomplete state.  # noqa: E501

        :param generation: The generation of this V1beta1ResourcePool.  # noqa: E501
        :type generation: int
        """
        if self.local_vars_configuration.client_side_validation and generation is None:  # noqa: E501
            raise ValueError("Invalid value for `generation`, must not be `None`")  # noqa: E501

        self._generation = generation

    @property
    def name(self):
        """Gets the name of this V1beta1ResourcePool.  # noqa: E501

        Name is used to identify the pool. For node-local devices, this is often the node name, but this is not required.  It must not be longer than 253 characters and must consist of one or more DNS sub-domains separated by slashes. This field is immutable.  # noqa: E501

        :return: The name of this V1beta1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1ResourcePool.

        Name is used to identify the pool. For node-local devices, this is often the node name, but this is not required.  It must not be longer than 253 characters and must consist of one or more DNS sub-domains separated by slashes. This field is immutable.  # noqa: E501

        :param name: The name of this V1beta1ResourcePool.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resource_slice_count(self):
        """Gets the resource_slice_count of this V1beta1ResourcePool.  # noqa: E501

        ResourceSliceCount is the total number of ResourceSlices in the pool at this generation number. Must be greater than zero.  Consumers can use this to check whether they have seen all ResourceSlices belonging to the same pool.  # noqa: E501

        :return: The resource_slice_count of this V1beta1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._resource_slice_count

    @resource_slice_count.setter
    def resource_slice_count(self, resource_slice_count):
        """Sets the resource_slice_count of this V1beta1ResourcePool.

        ResourceSliceCount is the total number of ResourceSlices in the pool at this generation number. Must be greater than zero.  Consumers can use this to check whether they have seen all ResourceSlices belonging to the same pool.  # noqa: E501

        :param resource_slice_count: The resource_slice_count of this V1beta1ResourcePool.  # noqa: E501
        :type resource_slice_count: int
        """
        if self.local_vars_configuration.client_side_validation and resource_slice_count is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_slice_count`, must not be `None`")  # noqa: E501

        self._resource_slice_count = resource_slice_count

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
        if not isinstance(other, V1beta1ResourcePool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1ResourcePool):
            return True

        return self.to_dict() != other.to_dict()
