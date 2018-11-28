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


class HyperflexNamedVsan(object):
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
        'name': 'str',
        'vsan_id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'vsan_id': 'VsanId'
    }

    def __init__(self, name=None, vsan_id=None):
        """
        HyperflexNamedVsan - a model defined in Swagger
        """

        self._name = None
        self._vsan_id = None

        if name is not None:
          self.name = name
        if vsan_id is not None:
          self.vsan_id = vsan_id

    @property
    def name(self):
        """
        Gets the name of this HyperflexNamedVsan.
        VSAN name  

        :return: The name of this HyperflexNamedVsan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexNamedVsan.
        VSAN name  

        :param name: The name of this HyperflexNamedVsan.
        :type: str
        """

        self._name = name

    @property
    def vsan_id(self):
        """
        Gets the vsan_id of this HyperflexNamedVsan.
        VSAN ID   

        :return: The vsan_id of this HyperflexNamedVsan.
        :rtype: int
        """
        return self._vsan_id

    @vsan_id.setter
    def vsan_id(self, vsan_id):
        """
        Sets the vsan_id of this HyperflexNamedVsan.
        VSAN ID   

        :param vsan_id: The vsan_id of this HyperflexNamedVsan.
        :type: int
        """

        self._vsan_id = vsan_id

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
        if not isinstance(other, HyperflexNamedVsan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
