# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-300
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StorageLocalDisk(object):
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
        'slot_number': 'int'
    }

    attribute_map = {
        'slot_number': 'SlotNumber'
    }

    def __init__(self, slot_number=None):
        """
        StorageLocalDisk - a model defined in Swagger
        """

        self._slot_number = None

        if slot_number is not None:
          self.slot_number = slot_number

    @property
    def slot_number(self):
        """
        Gets the slot_number of this StorageLocalDisk.
        Specifies the slot number of the disk to be referenced. As this is a policy object, this slot number may or may not be valid depending on the number of disks in the associated server   

        :return: The slot_number of this StorageLocalDisk.
        :rtype: int
        """
        return self._slot_number

    @slot_number.setter
    def slot_number(self, slot_number):
        """
        Sets the slot_number of this StorageLocalDisk.
        Specifies the slot number of the disk to be referenced. As this is a policy object, this slot number may or may not be valid depending on the number of disks in the associated server   

        :param slot_number: The slot_number of this StorageLocalDisk.
        :type: int
        """

        self._slot_number = slot_number

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
        if not isinstance(other, StorageLocalDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
