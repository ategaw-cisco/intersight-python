# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-262
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HyperflexHxNetworkAddressDt(object):
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
        'address': 'str',
        'fqdn': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'address': 'Address',
        'fqdn': 'Fqdn',
        'ip': 'Ip'
    }

    def __init__(self, address=None, fqdn=None, ip=None):
        """
        HyperflexHxNetworkAddressDt - a model defined in Swagger
        """

        self._address = None
        self._fqdn = None
        self._ip = None

        if address is not None:
          self.address = address
        if fqdn is not None:
          self.fqdn = fqdn
        if ip is not None:
          self.ip = ip

    @property
    def address(self):
        """
        Gets the address of this HyperflexHxNetworkAddressDt.

        :return: The address of this HyperflexHxNetworkAddressDt.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this HyperflexHxNetworkAddressDt.

        :param address: The address of this HyperflexHxNetworkAddressDt.
        :type: str
        """

        self._address = address

    @property
    def fqdn(self):
        """
        Gets the fqdn of this HyperflexHxNetworkAddressDt.

        :return: The fqdn of this HyperflexHxNetworkAddressDt.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this HyperflexHxNetworkAddressDt.

        :param fqdn: The fqdn of this HyperflexHxNetworkAddressDt.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def ip(self):
        """
        Gets the ip of this HyperflexHxNetworkAddressDt.

        :return: The ip of this HyperflexHxNetworkAddressDt.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this HyperflexHxNetworkAddressDt.

        :param ip: The ip of this HyperflexHxNetworkAddressDt.
        :type: str
        """

        self._ip = ip

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
        if not isinstance(other, HyperflexHxNetworkAddressDt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
