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


class QataskExecutionStatusTaskRef(object):
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
        'moid': 'str',
        'object_type': 'str'
    }

    attribute_map = {
        'moid': 'Moid',
        'object_type': 'ObjectType'
    }

    def __init__(self, moid=None, object_type=None):
        """
        QataskExecutionStatusTaskRef - a model defined in Swagger
        """

        self._moid = None
        self._object_type = None

        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type

    @property
    def moid(self):
        """
        Gets the moid of this QataskExecutionStatusTaskRef.

        :return: The moid of this QataskExecutionStatusTaskRef.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this QataskExecutionStatusTaskRef.

        :param moid: The moid of this QataskExecutionStatusTaskRef.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this QataskExecutionStatusTaskRef.

        :return: The object_type of this QataskExecutionStatusTaskRef.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this QataskExecutionStatusTaskRef.

        :param object_type: The object_type of this QataskExecutionStatusTaskRef.
        :type: str
        """

        self._object_type = object_type

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
        if not isinstance(other, QataskExecutionStatusTaskRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
