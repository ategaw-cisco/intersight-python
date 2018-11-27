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


class ConnectorAuthMessage(object):
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
        'remote_user_locale': 'str',
        'remote_user_name': 'str',
        'remote_user_roles': 'str',
        'remote_user_session_id': 'str'
    }

    attribute_map = {
        'remote_user_locale': 'RemoteUserLocale',
        'remote_user_name': 'RemoteUserName',
        'remote_user_roles': 'RemoteUserRoles',
        'remote_user_session_id': 'RemoteUserSessionId'
    }

    def __init__(self, remote_user_locale=None, remote_user_name=None, remote_user_roles=None, remote_user_session_id=None):
        """
        ConnectorAuthMessage - a model defined in Swagger
        """

        self._remote_user_locale = None
        self._remote_user_name = None
        self._remote_user_roles = None
        self._remote_user_session_id = None

        if remote_user_locale is not None:
          self.remote_user_locale = remote_user_locale
        if remote_user_name is not None:
          self.remote_user_name = remote_user_name
        if remote_user_roles is not None:
          self.remote_user_roles = remote_user_roles
        if remote_user_session_id is not None:
          self.remote_user_session_id = remote_user_session_id

    @property
    def remote_user_locale(self):
        """
        Gets the remote_user_locale of this ConnectorAuthMessage.
        The platform locale to assign user. A locale defines one or more organizations (domains) the user is allowed access, and access is limited to the organizations specified in the locale.  

        :return: The remote_user_locale of this ConnectorAuthMessage.
        :rtype: str
        """
        return self._remote_user_locale

    @remote_user_locale.setter
    def remote_user_locale(self, remote_user_locale):
        """
        Sets the remote_user_locale of this ConnectorAuthMessage.
        The platform locale to assign user. A locale defines one or more organizations (domains) the user is allowed access, and access is limited to the organizations specified in the locale.  

        :param remote_user_locale: The remote_user_locale of this ConnectorAuthMessage.
        :type: str
        """

        self._remote_user_locale = remote_user_locale

    @property
    def remote_user_name(self):
        """
        Gets the remote_user_name of this ConnectorAuthMessage.
        User name passed to the platform for use in platform audit logs.  

        :return: The remote_user_name of this ConnectorAuthMessage.
        :rtype: str
        """
        return self._remote_user_name

    @remote_user_name.setter
    def remote_user_name(self, remote_user_name):
        """
        Sets the remote_user_name of this ConnectorAuthMessage.
        User name passed to the platform for use in platform audit logs.  

        :param remote_user_name: The remote_user_name of this ConnectorAuthMessage.
        :type: str
        """

        self._remote_user_name = remote_user_name

    @property
    def remote_user_roles(self):
        """
        Gets the remote_user_roles of this ConnectorAuthMessage.
        List of roles to pass to the platform to validate the action against  

        :return: The remote_user_roles of this ConnectorAuthMessage.
        :rtype: str
        """
        return self._remote_user_roles

    @remote_user_roles.setter
    def remote_user_roles(self, remote_user_roles):
        """
        Sets the remote_user_roles of this ConnectorAuthMessage.
        List of roles to pass to the platform to validate the action against  

        :param remote_user_roles: The remote_user_roles of this ConnectorAuthMessage.
        :type: str
        """

        self._remote_user_roles = remote_user_roles

    @property
    def remote_user_session_id(self):
        """
        Gets the remote_user_session_id of this ConnectorAuthMessage.
        Session Id passed to the platform for use in platforms auditing.   

        :return: The remote_user_session_id of this ConnectorAuthMessage.
        :rtype: str
        """
        return self._remote_user_session_id

    @remote_user_session_id.setter
    def remote_user_session_id(self, remote_user_session_id):
        """
        Sets the remote_user_session_id of this ConnectorAuthMessage.
        Session Id passed to the platform for use in platforms auditing.   

        :param remote_user_session_id: The remote_user_session_id of this ConnectorAuthMessage.
        :type: str
        """

        self._remote_user_session_id = remote_user_session_id

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
        if not isinstance(other, ConnectorAuthMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
