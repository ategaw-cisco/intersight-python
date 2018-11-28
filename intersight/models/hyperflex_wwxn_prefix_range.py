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


class HyperflexWwxnPrefixRange(object):
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
        'end_addr': 'str',
        'start_addr': 'str'
    }

    attribute_map = {
        'end_addr': 'EndAddr',
        'start_addr': 'StartAddr'
    }

    def __init__(self, end_addr=None, start_addr=None):
        """
        HyperflexWwxnPrefixRange - a model defined in Swagger
        """

        self._end_addr = None
        self._start_addr = None

        if end_addr is not None:
          self.end_addr = end_addr
        if start_addr is not None:
          self.start_addr = start_addr

    @property
    def end_addr(self):
        """
        Gets the end_addr of this HyperflexWwxnPrefixRange.
        End WWxN prefix of a WWPN/WWNN range in the form of 20:00:00:25:B5:XX  

        :return: The end_addr of this HyperflexWwxnPrefixRange.
        :rtype: str
        """
        return self._end_addr

    @end_addr.setter
    def end_addr(self, end_addr):
        """
        Sets the end_addr of this HyperflexWwxnPrefixRange.
        End WWxN prefix of a WWPN/WWNN range in the form of 20:00:00:25:B5:XX  

        :param end_addr: The end_addr of this HyperflexWwxnPrefixRange.
        :type: str
        """

        self._end_addr = end_addr

    @property
    def start_addr(self):
        """
        Gets the start_addr of this HyperflexWwxnPrefixRange.
        Start WWxN prefix of a WWPN/WWNN range in the form of 20:00:00:25:B5:XX   

        :return: The start_addr of this HyperflexWwxnPrefixRange.
        :rtype: str
        """
        return self._start_addr

    @start_addr.setter
    def start_addr(self, start_addr):
        """
        Sets the start_addr of this HyperflexWwxnPrefixRange.
        Start WWxN prefix of a WWPN/WWNN range in the form of 20:00:00:25:B5:XX   

        :param start_addr: The start_addr of this HyperflexWwxnPrefixRange.
        :type: str
        """

        self._start_addr = start_addr

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
        if not isinstance(other, HyperflexWwxnPrefixRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
