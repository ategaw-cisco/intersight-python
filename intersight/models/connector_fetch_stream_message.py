# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-265
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectorFetchStreamMessage(object):
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
        'stream_name': 'str',
        'sequences': 'list[int]'
    }

    attribute_map = {
        'stream_name': 'StreamName',
        'sequences': 'Sequences'
    }

    def __init__(self, stream_name=None, sequences=None):
        """
        ConnectorFetchStreamMessage - a model defined in Swagger
        """

        self._stream_name = None
        self._sequences = None

        if stream_name is not None:
          self.stream_name = stream_name
        if sequences is not None:
          self.sequences = sequences

    @property
    def stream_name(self):
        """
        Gets the stream_name of this ConnectorFetchStreamMessage.
        The requested stream name. Stream names are unique per device endpoint.   

        :return: The stream_name of this ConnectorFetchStreamMessage.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ConnectorFetchStreamMessage.
        The requested stream name. Stream names are unique per device endpoint.   

        :param stream_name: The stream_name of this ConnectorFetchStreamMessage.
        :type: str
        """

        self._stream_name = stream_name

    @property
    def sequences(self):
        """
        Gets the sequences of this ConnectorFetchStreamMessage.
        List of sequences to retrieve from the stream cache   

        :return: The sequences of this ConnectorFetchStreamMessage.
        :rtype: list[int]
        """
        return self._sequences

    @sequences.setter
    def sequences(self, sequences):
        """
        Sets the sequences of this ConnectorFetchStreamMessage.
        List of sequences to retrieve from the stream cache   

        :param sequences: The sequences of this ConnectorFetchStreamMessage.
        :type: list[int]
        """

        self._sequences = sequences

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
        if not isinstance(other, ConnectorFetchStreamMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
