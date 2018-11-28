# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-261
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectorpackConnectorPackSummary(object):
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
        'downloaded_version': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'downloaded_version': 'DownloadedVersion',
        'name': 'Name',
        'version': 'Version'
    }

    def __init__(self, downloaded_version=None, name=None, version=None):
        """
        ConnectorpackConnectorPackSummary - a model defined in Swagger
        """

        self._downloaded_version = None
        self._name = None
        self._version = None

        if downloaded_version is not None:
          self.downloaded_version = downloaded_version
        if name is not None:
          self.name = name
        if version is not None:
          self.version = version

    @property
    def downloaded_version(self):
        """
        Gets the downloaded_version of this ConnectorpackConnectorPackSummary.
        Downloaded version of connector pack image in UCS Director  

        :return: The downloaded_version of this ConnectorpackConnectorPackSummary.
        :rtype: str
        """
        return self._downloaded_version

    @downloaded_version.setter
    def downloaded_version(self, downloaded_version):
        """
        Sets the downloaded_version of this ConnectorpackConnectorPackSummary.
        Downloaded version of connector pack image in UCS Director  

        :param downloaded_version: The downloaded_version of this ConnectorpackConnectorPackSummary.
        :type: str
        """

        self._downloaded_version = downloaded_version

    @property
    def name(self):
        """
        Gets the name of this ConnectorpackConnectorPackSummary.
        Name of connector pack running in UCS Director  

        :return: The name of this ConnectorpackConnectorPackSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectorpackConnectorPackSummary.
        Name of connector pack running in UCS Director  

        :param name: The name of this ConnectorpackConnectorPackSummary.
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """
        Gets the version of this ConnectorpackConnectorPackSummary.
        Running connector pack version in UCS Director   

        :return: The version of this ConnectorpackConnectorPackSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ConnectorpackConnectorPackSummary.
        Running connector pack version in UCS Director   

        :param version: The version of this ConnectorpackConnectorPackSummary.
        :type: str
        """

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
        if not isinstance(other, ConnectorpackConnectorPackSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
