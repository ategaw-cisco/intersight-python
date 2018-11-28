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


class Error(object):
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
        'cause': 'Error',
        'code': 'int',
        'message': 'str',
        'message_id': 'str'
    }

    attribute_map = {
        'cause': 'cause',
        'code': 'code',
        'message': 'message',
        'message_id': 'messageId'
    }

    def __init__(self, cause=None, code=None, message=None, message_id=None):
        """
        Error - a model defined in Swagger
        """

        self._cause = None
        self._code = None
        self._message = None
        self._message_id = None

        if cause is not None:
          self.cause = cause
        self.code = code
        self.message = message
        if message_id is not None:
          self.message_id = message_id

    @property
    def cause(self):
        """
        Gets the cause of this Error.
        The cause of this error

        :return: The cause of this Error.
        :rtype: Error
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """
        Sets the cause of this Error.
        The cause of this error

        :param cause: The cause of this Error.
        :type: Error
        """

        self._cause = cause

    @property
    def code(self):
        """
        Gets the code of this Error.

        :return: The code of this Error.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Error.

        :param code: The code of this Error.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this Error.

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Error.

        :param message: The message of this Error.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def message_id(self):
        """
        Gets the message_id of this Error.
        A language-independent identifier of the specific error.

        :return: The message_id of this Error.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this Error.
        A language-independent identifier of the specific error.

        :param message_id: The message_id of this Error.
        :type: str
        """

        self._message_id = message_id

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
