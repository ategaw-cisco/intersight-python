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


class HyperflexServerFirmwareVersionEntry(object):
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
        'value': 'str',
        'constraint': 'HyperflexAppSettingConstraint',
        'label': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'value': 'Value',
        'constraint': 'Constraint',
        'label': 'Label'
    }

    def __init__(self, name=None, value=None, constraint=None, label=None):
        """
        HyperflexServerFirmwareVersionEntry - a model defined in Swagger
        """

        self._name = None
        self._value = None
        self._constraint = None
        self._label = None

        if name is not None:
          self.name = name
        if value is not None:
          self.value = value
        if constraint is not None:
          self.constraint = constraint
        if label is not None:
          self.label = label

    @property
    def name(self):
        """
        Gets the name of this HyperflexServerFirmwareVersionEntry.
        Application setting identifier  

        :return: The name of this HyperflexServerFirmwareVersionEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexServerFirmwareVersionEntry.
        Application setting identifier  

        :param name: The name of this HyperflexServerFirmwareVersionEntry.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this HyperflexServerFirmwareVersionEntry.
        Application setting value   

        :return: The value of this HyperflexServerFirmwareVersionEntry.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this HyperflexServerFirmwareVersionEntry.
        Application setting value   

        :param value: The value of this HyperflexServerFirmwareVersionEntry.
        :type: str
        """

        self._value = value

    @property
    def constraint(self):
        """
        Gets the constraint of this HyperflexServerFirmwareVersionEntry.
        Conditions to be met to apply the AppSetting  

        :return: The constraint of this HyperflexServerFirmwareVersionEntry.
        :rtype: HyperflexAppSettingConstraint
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        """
        Sets the constraint of this HyperflexServerFirmwareVersionEntry.
        Conditions to be met to apply the AppSetting  

        :param constraint: The constraint of this HyperflexServerFirmwareVersionEntry.
        :type: HyperflexAppSettingConstraint
        """

        self._constraint = constraint

    @property
    def label(self):
        """
        Gets the label of this HyperflexServerFirmwareVersionEntry.
        Display name for server firmware bundle version in UI   

        :return: The label of this HyperflexServerFirmwareVersionEntry.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this HyperflexServerFirmwareVersionEntry.
        Display name for server firmware bundle version in UI   

        :param label: The label of this HyperflexServerFirmwareVersionEntry.
        :type: str
        """

        self._label = label

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
        if not isinstance(other, HyperflexServerFirmwareVersionEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
