# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-300
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FirmwareHttpServer(object):
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
        'location_link': 'str',
        'mount_options': 'str'
    }

    attribute_map = {
        'location_link': 'LocationLink',
        'mount_options': 'MountOptions'
    }

    def __init__(self, location_link=None, mount_options=None):
        """
        FirmwareHttpServer - a model defined in Swagger
        """

        self._location_link = None
        self._mount_options = None

        if location_link is not None:
          self.location_link = location_link
        if mount_options is not None:
          self.mount_options = mount_options

    @property
    def location_link(self):
        """
        Gets the location_link of this FirmwareHttpServer.
        HTTP/HTTPS link to the image. Accepted formats http[s]://server-hostname/share/image or http[s]://serverip/share/image.  

        :return: The location_link of this FirmwareHttpServer.
        :rtype: str
        """
        return self._location_link

    @location_link.setter
    def location_link(self, location_link):
        """
        Sets the location_link of this FirmwareHttpServer.
        HTTP/HTTPS link to the image. Accepted formats http[s]://server-hostname/share/image or http[s]://serverip/share/image.  

        :param location_link: The location_link of this FirmwareHttpServer.
        :type: str
        """

        self._location_link = location_link

    @property
    def mount_options(self):
        """
        Gets the mount_options of this FirmwareHttpServer.
        Mount option as configured on the HTTP server. Empty if nothing is configured.   

        :return: The mount_options of this FirmwareHttpServer.
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """
        Sets the mount_options of this FirmwareHttpServer.
        Mount option as configured on the HTTP server. Empty if nothing is configured.   

        :param mount_options: The mount_options of this FirmwareHttpServer.
        :type: str
        """

        self._mount_options = mount_options

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
        if not isinstance(other, FirmwareHttpServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
