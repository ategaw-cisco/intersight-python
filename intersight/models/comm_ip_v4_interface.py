# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-261
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CommIpV4Interface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gateway': 'str',
        'ip_address': 'str',
        'netmask': 'str'
    }

    attribute_map = {
        'gateway': 'Gateway',
        'ip_address': 'IpAddress',
        'netmask': 'Netmask'
    }

    def __init__(self, gateway=None, ip_address=None, netmask=None):
        """
        CommIpV4Interface - a model defined in Swagger
        """

        self._gateway = None
        self._ip_address = None
        self._netmask = None

        if gateway is not None:
          self.gateway = gateway
        if ip_address is not None:
          self.ip_address = ip_address
        if netmask is not None:
          self.netmask = netmask

    @property
    def gateway(self):
        """
        Gets the gateway of this CommIpV4Interface.
        IP Gateway  

        :return: The gateway of this CommIpV4Interface.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this CommIpV4Interface.
        IP Gateway  

        :param gateway: The gateway of this CommIpV4Interface.
        :type: str
        """

        self._gateway = gateway

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CommIpV4Interface.
        IP Address  

        :return: The ip_address of this CommIpV4Interface.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CommIpV4Interface.
        IP Address  

        :param ip_address: The ip_address of this CommIpV4Interface.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def netmask(self):
        """
        Gets the netmask of this CommIpV4Interface.
        IP Netmask   

        :return: The netmask of this CommIpV4Interface.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """
        Sets the netmask of this CommIpV4Interface.
        IP Netmask   

        :param netmask: The netmask of this CommIpV4Interface.
        :type: str
        """

        self._netmask = netmask

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CommIpV4Interface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
