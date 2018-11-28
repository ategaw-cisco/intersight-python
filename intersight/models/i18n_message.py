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


class I18nMessage(object):
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
        'message': 'str',
        'message_id': 'str',
        'message_params': 'list[I18nMessageParam]'
    }

    attribute_map = {
        'message': 'Message',
        'message_id': 'MessageId',
        'message_params': 'MessageParams'
    }

    def __init__(self, message=None, message_id=None, message_params=None):
        """
        I18nMessage - a model defined in Swagger
        """

        self._message = None
        self._message_id = None
        self._message_params = None

        if message is not None:
          self.message = message
        if message_id is not None:
          self.message_id = message_id
        if message_params is not None:
          self.message_params = message_params

    @property
    def message(self):
        """
        Gets the message of this I18nMessage.
        The default (en-US) localized message. Default localized message will be stored and directly retrieved when the user's locale setting is en-US.  

        :return: The message of this I18nMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this I18nMessage.
        The default (en-US) localized message. Default localized message will be stored and directly retrieved when the user's locale setting is en-US.  

        :param message: The message of this I18nMessage.
        :type: str
        """

        self._message = message

    @property
    def message_id(self):
        """
        Gets the message_id of this I18nMessage.
        The message identitifer that is mapped to localized messages  

        :return: The message_id of this I18nMessage.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this I18nMessage.
        The message identitifer that is mapped to localized messages  

        :param message_id: The message_id of this I18nMessage.
        :type: str
        """

        self._message_id = message_id

    @property
    def message_params(self):
        """
        Gets the message_params of this I18nMessage.
        List of message parameters   

        :return: The message_params of this I18nMessage.
        :rtype: list[I18nMessageParam]
        """
        return self._message_params

    @message_params.setter
    def message_params(self, message_params):
        """
        Sets the message_params of this I18nMessage.
        List of message parameters   

        :param message_params: The message_params of this I18nMessage.
        :type: list[I18nMessageParam]
        """

        self._message_params = message_params

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
        if not isinstance(other, I18nMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
