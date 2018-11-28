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


class SdcardPartition(object):
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
        'type': 'str',
        'virtual_drives': 'list[SdcardVirtualDrive]'
    }

    attribute_map = {
        'type': 'Type',
        'virtual_drives': 'VirtualDrives'
    }

    def __init__(self, type='OS', virtual_drives=None):
        """
        SdcardPartition - a model defined in Swagger
        """

        self._type = None
        self._virtual_drives = None

        if type is not None:
          self.type = type
        if virtual_drives is not None:
          self.virtual_drives = virtual_drives

    @property
    def type(self):
        """
        Gets the type of this SdcardPartition.
        Type of the partition  

        :return: The type of this SdcardPartition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SdcardPartition.
        Type of the partition  

        :param type: The type of this SdcardPartition.
        :type: str
        """
        allowed_values = ["OS", "Utility"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def virtual_drives(self):
        """
        Gets the virtual_drives of this SdcardPartition.
        Collection of available virtual drives   

        :return: The virtual_drives of this SdcardPartition.
        :rtype: list[SdcardVirtualDrive]
        """
        return self._virtual_drives

    @virtual_drives.setter
    def virtual_drives(self, virtual_drives):
        """
        Sets the virtual_drives of this SdcardPartition.
        Collection of available virtual drives   

        :param virtual_drives: The virtual_drives of this SdcardPartition.
        :type: list[SdcardVirtualDrive]
        """

        self._virtual_drives = virtual_drives

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
        if not isinstance(other, SdcardPartition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
