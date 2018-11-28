# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-264
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StorageSpanGroup(object):
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
        'disks': 'list[StorageLocalDisk]'
    }

    attribute_map = {
        'disks': 'Disks'
    }

    def __init__(self, disks=None):
        """
        StorageSpanGroup - a model defined in Swagger
        """

        self._disks = None

        if disks is not None:
          self.disks = disks

    @property
    def disks(self):
        """
        Gets the disks of this StorageSpanGroup.
        Collection of local disks that are part of this span group. The minimum number of disks needed in a span group varies based on RAID level. Raid0 requires at least one disk, Raid1 and Raid10 requires at least 2 and in multiples of 2, Raid5 Raid50 Raid6 and Raid60 require at least 3 disks in a span group   

        :return: The disks of this StorageSpanGroup.
        :rtype: list[StorageLocalDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """
        Sets the disks of this StorageSpanGroup.
        Collection of local disks that are part of this span group. The minimum number of disks needed in a span group varies based on RAID level. Raid0 requires at least one disk, Raid1 and Raid10 requires at least 2 and in multiples of 2, Raid5 Raid50 Raid6 and Raid60 require at least 3 disks in a span group   

        :param disks: The disks of this StorageSpanGroup.
        :type: list[StorageLocalDisk]
        """

        self._disks = disks

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
        if not isinstance(other, StorageSpanGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
