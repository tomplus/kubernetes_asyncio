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


class V1alpha3AllocatedDeviceStatus(object):
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
        'conditions': 'list[V1Condition]',
        'data': 'object',
        'device': 'str',
        'driver': 'str',
        'network_data': 'V1alpha3NetworkDeviceData',
        'pool': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'data': 'data',
        'device': 'device',
        'driver': 'driver',
        'network_data': 'networkData',
        'pool': 'pool'
    }

    def __init__(self, conditions=None, data=None, device=None, driver=None, network_data=None, pool=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha3AllocatedDeviceStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._data = None
        self._device = None
        self._driver = None
        self._network_data = None
        self._pool = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if data is not None:
            self.data = data
        self.device = device
        self.driver = driver
        if network_data is not None:
            self.network_data = network_data
        self.pool = pool

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha3AllocatedDeviceStatus.  # noqa: E501

        Conditions contains the latest observation of the device's state. If the device has been configured according to the class and claim config references, the `Ready` condition should be True.  # noqa: E501

        :return: The conditions of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :rtype: list[V1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha3AllocatedDeviceStatus.

        Conditions contains the latest observation of the device's state. If the device has been configured according to the class and claim config references, the `Ready` condition should be True.  # noqa: E501

        :param conditions: The conditions of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :type conditions: list[V1Condition]
        """

        self._conditions = conditions

    @property
    def data(self):
        """Gets the data of this V1alpha3AllocatedDeviceStatus.  # noqa: E501

        Data contains arbitrary driver-specific data.  The length of the raw data must be smaller or equal to 10 Ki.  # noqa: E501

        :return: The data of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this V1alpha3AllocatedDeviceStatus.

        Data contains arbitrary driver-specific data.  The length of the raw data must be smaller or equal to 10 Ki.  # noqa: E501

        :param data: The data of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :type data: object
        """

        self._data = data

    @property
    def device(self):
        """Gets the device of this V1alpha3AllocatedDeviceStatus.  # noqa: E501

        Device references one device instance via its name in the driver's resource pool. It must be a DNS label.  # noqa: E501

        :return: The device of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this V1alpha3AllocatedDeviceStatus.

        Device references one device instance via its name in the driver's resource pool. It must be a DNS label.  # noqa: E501

        :param device: The device of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :type device: str
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def driver(self):
        """Gets the driver of this V1alpha3AllocatedDeviceStatus.  # noqa: E501

        Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.  # noqa: E501

        :return: The driver of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this V1alpha3AllocatedDeviceStatus.

        Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.  # noqa: E501

        :param driver: The driver of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :type driver: str
        """
        if self.local_vars_configuration.client_side_validation and driver is None:  # noqa: E501
            raise ValueError("Invalid value for `driver`, must not be `None`")  # noqa: E501

        self._driver = driver

    @property
    def network_data(self):
        """Gets the network_data of this V1alpha3AllocatedDeviceStatus.  # noqa: E501


        :return: The network_data of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :rtype: V1alpha3NetworkDeviceData
        """
        return self._network_data

    @network_data.setter
    def network_data(self, network_data):
        """Sets the network_data of this V1alpha3AllocatedDeviceStatus.


        :param network_data: The network_data of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :type network_data: V1alpha3NetworkDeviceData
        """

        self._network_data = network_data

    @property
    def pool(self):
        """Gets the pool of this V1alpha3AllocatedDeviceStatus.  # noqa: E501

        This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.  # noqa: E501

        :return: The pool of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this V1alpha3AllocatedDeviceStatus.

        This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.  # noqa: E501

        :param pool: The pool of this V1alpha3AllocatedDeviceStatus.  # noqa: E501
        :type pool: str
        """
        if self.local_vars_configuration.client_side_validation and pool is None:  # noqa: E501
            raise ValueError("Invalid value for `pool`, must not be `None`")  # noqa: E501

        self._pool = pool

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
        if not isinstance(other, V1alpha3AllocatedDeviceStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha3AllocatedDeviceStatus):
            return True

        return self.to_dict() != other.to_dict()
