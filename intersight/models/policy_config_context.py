# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-260
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyConfigContext(object):
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
        'config_state': 'str',
        'control_action': 'str',
        'error_state': 'str',
        'oper_state': 'str'
    }

    attribute_map = {
        'config_state': 'ConfigState',
        'control_action': 'ControlAction',
        'error_state': 'ErrorState',
        'oper_state': 'OperState'
    }

    def __init__(self, config_state=None, control_action=None, error_state=None, oper_state=None):
        """
        PolicyConfigContext - a model defined in Swagger
        """

        self._config_state = None
        self._control_action = None
        self._error_state = None
        self._oper_state = None

        if config_state is not None:
          self.config_state = config_state
        if control_action is not None:
          self.control_action = control_action
        if error_state is not None:
          self.error_state = error_state
        if oper_state is not None:
          self.oper_state = oper_state

    @property
    def config_state(self):
        """
        Gets the config_state of this PolicyConfigContext.
        Indicates a profile's configuration deploying state Values -- Assigned, Not-assigned, Associated, Pending-changes, Validating, Configuring, Failed  

        :return: The config_state of this PolicyConfigContext.
        :rtype: str
        """
        return self._config_state

    @config_state.setter
    def config_state(self, config_state):
        """
        Sets the config_state of this PolicyConfigContext.
        Indicates a profile's configuration deploying state Values -- Assigned, Not-assigned, Associated, Pending-changes, Validating, Configuring, Failed  

        :param config_state: The config_state of this PolicyConfigContext.
        :type: str
        """

        self._config_state = config_state

    @property
    def control_action(self):
        """
        Gets the control_action of this PolicyConfigContext.
        System action to trigger the appropriate workflow. Values -- No_op, ConfigChange, Deploy, Unbind  

        :return: The control_action of this PolicyConfigContext.
        :rtype: str
        """
        return self._control_action

    @control_action.setter
    def control_action(self, control_action):
        """
        Sets the control_action of this PolicyConfigContext.
        System action to trigger the appropriate workflow. Values -- No_op, ConfigChange, Deploy, Unbind  

        :param control_action: The control_action of this PolicyConfigContext.
        :type: str
        """

        self._control_action = control_action

    @property
    def error_state(self):
        """
        Gets the error_state of this PolicyConfigContext.
        Indicates a profile's error state. Values -- Validation-error (Static validation error), Pre-config-error (Runtime validation error), Config-error (Runtime configuration error)  

        :return: The error_state of this PolicyConfigContext.
        :rtype: str
        """
        return self._error_state

    @error_state.setter
    def error_state(self, error_state):
        """
        Sets the error_state of this PolicyConfigContext.
        Indicates a profile's error state. Values -- Validation-error (Static validation error), Pre-config-error (Runtime validation error), Config-error (Runtime configuration error)  

        :param error_state: The error_state of this PolicyConfigContext.
        :type: str
        """

        self._error_state = error_state

    @property
    def oper_state(self):
        """
        Gets the oper_state of this PolicyConfigContext.
        Combined state (configState, and operational state of the associated physical resource) to indicate the current state of the profile. Values -- n/a, Power-off, Pending-changes, Configuring, Ok, Failed   

        :return: The oper_state of this PolicyConfigContext.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this PolicyConfigContext.
        Combined state (configState, and operational state of the associated physical resource) to indicate the current state of the profile. Values -- n/a, Power-off, Pending-changes, Configuring, Ok, Failed   

        :param oper_state: The oper_state of this PolicyConfigContext.
        :type: str
        """

        self._oper_state = oper_state

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
        if not isinstance(other, PolicyConfigContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
