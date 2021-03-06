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


class SnmpTrap(object):
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
        'destination': 'str',
        'enabled': 'bool',
        'port': 'int',
        'type': 'str',
        'user': 'str',
        'version': 'str'
    }

    attribute_map = {
        'destination': 'Destination',
        'enabled': 'Enabled',
        'port': 'Port',
        'type': 'Type',
        'user': 'User',
        'version': 'Version'
    }

    def __init__(self, destination=None, enabled=None, port=None, type='Trap', user=None, version='V3'):
        """
        SnmpTrap - a model defined in Swagger
        """

        self._destination = None
        self._enabled = None
        self._port = None
        self._type = None
        self._user = None
        self._version = None

        if destination is not None:
          self.destination = destination
        if enabled is not None:
          self.enabled = enabled
        if port is not None:
          self.port = port
        if type is not None:
          self.type = type
        if user is not None:
          self.user = user
        if version is not None:
          self.version = version

    @property
    def destination(self):
        """
        Gets the destination of this SnmpTrap.
        Address to which the SNMP trap information is sent  

        :return: The destination of this SnmpTrap.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this SnmpTrap.
        Address to which the SNMP trap information is sent  

        :param destination: The destination of this SnmpTrap.
        :type: str
        """

        self._destination = destination

    @property
    def enabled(self):
        """
        Gets the enabled of this SnmpTrap.
        Enables/disables the trap on the server If enabled, trap us active on the server.  

        :return: The enabled of this SnmpTrap.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SnmpTrap.
        Enables/disables the trap on the server If enabled, trap us active on the server.  

        :param enabled: The enabled of this SnmpTrap.
        :type: bool
        """

        self._enabled = enabled

    @property
    def port(self):
        """
        Gets the port of this SnmpTrap.
        Port used by the server to communicate with trap destination. Enter a value between 1-65535.  

        :return: The port of this SnmpTrap.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this SnmpTrap.
        Port used by the server to communicate with trap destination. Enter a value between 1-65535.  

        :param port: The port of this SnmpTrap.
        :type: int
        """

        self._port = port

    @property
    def type(self):
        """
        Gets the type of this SnmpTrap.
        Type of trap which decides whether to receive a notification when a trap is received at the destination  

        :return: The type of this SnmpTrap.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SnmpTrap.
        Type of trap which decides whether to receive a notification when a trap is received at the destination  

        :param type: The type of this SnmpTrap.
        :type: str
        """
        allowed_values = ["Trap", "Inform"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user(self):
        """
        Gets the user of this SnmpTrap.
        SNMP user for the trap. Applicable only to SNMPv3  

        :return: The user of this SnmpTrap.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this SnmpTrap.
        SNMP user for the trap. Applicable only to SNMPv3  

        :param user: The user of this SnmpTrap.
        :type: str
        """

        self._user = user

    @property
    def version(self):
        """
        Gets the version of this SnmpTrap.
        SNMP version used for the trap   

        :return: The version of this SnmpTrap.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SnmpTrap.
        SNMP version used for the trap   

        :param version: The version of this SnmpTrap.
        :type: str
        """
        allowed_values = ["V3", "V2"]
        if version not in allowed_values:
            raise ValueError(
                "Invalid value for `version` ({0}), must be one of {1}"
                .format(version, allowed_values)
            )

        self._version = version

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
        if not isinstance(other, SnmpTrap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
