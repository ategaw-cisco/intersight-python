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


class HclProduct(object):
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
        'driver_names': 'list[str]',
        'error_code': 'str',
        'firmwares': 'list[HclFirmware]',
        'id': 'str',
        'model': 'str',
        'revision': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'driver_names': 'DriverNames',
        'error_code': 'ErrorCode',
        'firmwares': 'Firmwares',
        'id': 'Id',
        'model': 'Model',
        'revision': 'Revision',
        'vendor': 'Vendor'
    }

    def __init__(self, driver_names=None, error_code='Success', firmwares=None, id=None, model=None, revision=None, vendor=None):
        """
        HclProduct - a model defined in Swagger
        """

        self._driver_names = None
        self._error_code = None
        self._firmwares = None
        self._id = None
        self._model = None
        self._revision = None
        self._vendor = None

        if driver_names is not None:
          self.driver_names = driver_names
        if error_code is not None:
          self.error_code = error_code
        if firmwares is not None:
          self.firmwares = firmwares
        if id is not None:
          self.id = id
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if vendor is not None:
          self.vendor = vendor

    @property
    def driver_names(self):
        """
        Gets the driver_names of this HclProduct.
        supported driver names  

        :return: The driver_names of this HclProduct.
        :rtype: list[str]
        """
        return self._driver_names

    @driver_names.setter
    def driver_names(self, driver_names):
        """
        Sets the driver_names of this HclProduct.
        supported driver names  

        :param driver_names: The driver_names of this HclProduct.
        :type: list[str]
        """

        self._driver_names = driver_names

    @property
    def error_code(self):
        """
        Gets the error_code of this HclProduct.
        Error code indicating the support status  

        :return: The error_code of this HclProduct.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this HclProduct.
        Error code indicating the support status  

        :param error_code: The error_code of this HclProduct.
        :type: str
        """
        allowed_values = ["Success", "Unknown", "UnknownServer", "InvalidUcsVersion", "ProcessorNotSupported", "OSNotSupported", "UCSVersionNotSupported", "UcsVersionServerOSCombinationNotSupported", "ProductUnknown", "ProductNotSupported", "DriverNameNotSupported", "FirmwareVersionNotSupported", "DriverVersionNotSupported", "FirmwareVersionDriverVersionCombinationNotSupported", "FirmwareVersionAndDriverVersionNotSupported", "FirmwareVersionAndDriverNameNotSupported", "InternalError", "MarshallingError"]
        if error_code not in allowed_values:
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def firmwares(self):
        """
        Gets the firmwares of this HclProduct.
        supported firmware list  

        :return: The firmwares of this HclProduct.
        :rtype: list[HclFirmware]
        """
        return self._firmwares

    @firmwares.setter
    def firmwares(self, firmwares):
        """
        Sets the firmwares of this HclProduct.
        supported firmware list  

        :param firmwares: The firmwares of this HclProduct.
        :type: list[HclFirmware]
        """

        self._firmwares = firmwares

    @property
    def id(self):
        """
        Gets the id of this HclProduct.

        :return: The id of this HclProduct.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HclProduct.

        :param id: The id of this HclProduct.
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """
        Gets the model of this HclProduct.
        Model/PID of the product/adapter  

        :return: The model of this HclProduct.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this HclProduct.
        Model/PID of the product/adapter  

        :param model: The model of this HclProduct.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this HclProduct.
        revision of the adapter model  

        :return: The revision of this HclProduct.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this HclProduct.
        revision of the adapter model  

        :param revision: The revision of this HclProduct.
        :type: str
        """

        self._revision = revision

    @property
    def vendor(self):
        """
        Gets the vendor of this HclProduct.
        Vendor of the adapter   

        :return: The vendor of this HclProduct.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this HclProduct.
        Vendor of the adapter   

        :param vendor: The vendor of this HclProduct.
        :type: str
        """

        self._vendor = vendor

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
        if not isinstance(other, HclProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
