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


class FirmwareDirectDownload(object):
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
        'http_server': 'FirmwareHttpServer',
        'image_source': 'str',
        'is_password_set': 'bool',
        'password': 'str',
        'upgradeoption': 'str',
        'username': 'str'
    }

    attribute_map = {
        'http_server': 'HttpServer',
        'image_source': 'ImageSource',
        'is_password_set': 'IsPasswordSet',
        'password': 'Password',
        'upgradeoption': 'Upgradeoption',
        'username': 'Username'
    }

    def __init__(self, http_server=None, image_source='cco', is_password_set=None, password=None, upgradeoption='sd_upgrade_mount_only', username=None):
        """
        FirmwareDirectDownload - a model defined in Swagger
        """

        self._http_server = None
        self._image_source = None
        self._is_password_set = None
        self._password = None
        self._upgradeoption = None
        self._username = None

        if http_server is not None:
          self.http_server = http_server
        if image_source is not None:
          self.image_source = image_source
        if is_password_set is not None:
          self.is_password_set = is_password_set
        if password is not None:
          self.password = password
        if upgradeoption is not None:
          self.upgradeoption = upgradeoption
        if username is not None:
          self.username = username

    @property
    def http_server(self):
        """
        Gets the http_server of this FirmwareDirectDownload.
        HTTP Server option when the image source is a local https server  

        :return: The http_server of this FirmwareDirectDownload.
        :rtype: FirmwareHttpServer
        """
        return self._http_server

    @http_server.setter
    def http_server(self, http_server):
        """
        Sets the http_server of this FirmwareDirectDownload.
        HTTP Server option when the image source is a local https server  

        :param http_server: The http_server of this FirmwareDirectDownload.
        :type: FirmwareHttpServer
        """

        self._http_server = http_server

    @property
    def image_source(self):
        """
        Gets the image_source of this FirmwareDirectDownload.
        Source type referring the image to be downloaded from CCO or from a local https server  

        :return: The image_source of this FirmwareDirectDownload.
        :rtype: str
        """
        return self._image_source

    @image_source.setter
    def image_source(self, image_source):
        """
        Sets the image_source of this FirmwareDirectDownload.
        Source type referring the image to be downloaded from CCO or from a local https server  

        :param image_source: The image_source of this FirmwareDirectDownload.
        :type: str
        """
        allowed_values = ["cco", "localHttp"]
        if image_source not in allowed_values:
            raise ValueError(
                "Invalid value for `image_source` ({0}), must be one of {1}"
                .format(image_source, allowed_values)
            )

        self._image_source = image_source

    @property
    def is_password_set(self):
        """
        Gets the is_password_set of this FirmwareDirectDownload.

        :return: The is_password_set of this FirmwareDirectDownload.
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """
        Sets the is_password_set of this FirmwareDirectDownload.

        :param is_password_set: The is_password_set of this FirmwareDirectDownload.
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def password(self):
        """
        Gets the password of this FirmwareDirectDownload.
        Password as configured on the local https server  

        :return: The password of this FirmwareDirectDownload.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this FirmwareDirectDownload.
        Password as configured on the local https server  

        :param password: The password of this FirmwareDirectDownload.
        :type: str
        """

        self._password = password

    @property
    def upgradeoption(self):
        """
        Gets the upgradeoption of this FirmwareDirectDownload.
        Option to control the upgrade, e.g., sd_upgrade_mount_only - download the image into sd and upgrade wait for the server on-next boot  

        :return: The upgradeoption of this FirmwareDirectDownload.
        :rtype: str
        """
        return self._upgradeoption

    @upgradeoption.setter
    def upgradeoption(self, upgradeoption):
        """
        Sets the upgradeoption of this FirmwareDirectDownload.
        Option to control the upgrade, e.g., sd_upgrade_mount_only - download the image into sd and upgrade wait for the server on-next boot  

        :param upgradeoption: The upgradeoption of this FirmwareDirectDownload.
        :type: str
        """
        allowed_values = ["sd_upgrade_mount_only", "sd_download_only", "sd_upgrade_only", "sd_upgrade_full"]
        if upgradeoption not in allowed_values:
            raise ValueError(
                "Invalid value for `upgradeoption` ({0}), must be one of {1}"
                .format(upgradeoption, allowed_values)
            )

        self._upgradeoption = upgradeoption

    @property
    def username(self):
        """
        Gets the username of this FirmwareDirectDownload.
        Username as configured on the local https server   

        :return: The username of this FirmwareDirectDownload.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this FirmwareDirectDownload.
        Username as configured on the local https server   

        :param username: The username of this FirmwareDirectDownload.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, FirmwareDirectDownload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
