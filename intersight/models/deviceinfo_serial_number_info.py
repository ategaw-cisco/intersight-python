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


class DeviceinfoSerialNumberInfo(object):
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
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'covered_product_line_end_date': 'str',
        'customer_address': 'str',
        'customer_city': 'str',
        'customer_country': 'str',
        'customer_name': 'str',
        'customer_province': 'str',
        'is_valid': 'bool',
        'item_description': 'str',
        'orderable_pid': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'serial_number': 'str',
        'service_contract_number': 'str',
        'service_line_descr': 'str',
        'warranty_end_date': 'str',
        'warranty_type': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'covered_product_line_end_date': 'CoveredProductLineEndDate',
        'customer_address': 'CustomerAddress',
        'customer_city': 'CustomerCity',
        'customer_country': 'CustomerCountry',
        'customer_name': 'CustomerName',
        'customer_province': 'CustomerProvince',
        'is_valid': 'IsValid',
        'item_description': 'ItemDescription',
        'orderable_pid': 'OrderablePid',
        'registered_device': 'RegisteredDevice',
        'serial_number': 'SerialNumber',
        'service_contract_number': 'ServiceContractNumber',
        'service_line_descr': 'ServiceLineDescr',
        'warranty_end_date': 'WarrantyEndDate',
        'warranty_type': 'WarrantyType'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, covered_product_line_end_date=None, customer_address=None, customer_city=None, customer_country=None, customer_name=None, customer_province=None, is_valid=None, item_description=None, orderable_pid=None, registered_device=None, serial_number=None, service_contract_number=None, service_line_descr=None, warranty_end_date=None, warranty_type=None):
        """
        DeviceinfoSerialNumberInfo - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._version_context = None
        self._covered_product_line_end_date = None
        self._customer_address = None
        self._customer_city = None
        self._customer_country = None
        self._customer_name = None
        self._customer_province = None
        self._is_valid = None
        self._item_description = None
        self._orderable_pid = None
        self._registered_device = None
        self._serial_number = None
        self._service_contract_number = None
        self._service_line_descr = None
        self._warranty_end_date = None
        self._warranty_type = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if covered_product_line_end_date is not None:
          self.covered_product_line_end_date = covered_product_line_end_date
        if customer_address is not None:
          self.customer_address = customer_address
        if customer_city is not None:
          self.customer_city = customer_city
        if customer_country is not None:
          self.customer_country = customer_country
        if customer_name is not None:
          self.customer_name = customer_name
        if customer_province is not None:
          self.customer_province = customer_province
        if is_valid is not None:
          self.is_valid = is_valid
        if item_description is not None:
          self.item_description = item_description
        if orderable_pid is not None:
          self.orderable_pid = orderable_pid
        if registered_device is not None:
          self.registered_device = registered_device
        if serial_number is not None:
          self.serial_number = serial_number
        if service_contract_number is not None:
          self.service_contract_number = service_contract_number
        if service_line_descr is not None:
          self.service_line_descr = service_line_descr
        if warranty_end_date is not None:
          self.warranty_end_date = warranty_end_date
        if warranty_type is not None:
          self.warranty_type = warranty_type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this DeviceinfoSerialNumberInfo.
        The Account ID for this managed object.  

        :return: The account_moid of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this DeviceinfoSerialNumberInfo.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this DeviceinfoSerialNumberInfo.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this DeviceinfoSerialNumberInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this DeviceinfoSerialNumberInfo.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this DeviceinfoSerialNumberInfo.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this DeviceinfoSerialNumberInfo.
        The time when this managed object was created.  

        :return: The create_time of this DeviceinfoSerialNumberInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this DeviceinfoSerialNumberInfo.
        The time when this managed object was created.  

        :param create_time: The create_time of this DeviceinfoSerialNumberInfo.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this DeviceinfoSerialNumberInfo.
        The time when this managed object was last modified.  

        :return: The mod_time of this DeviceinfoSerialNumberInfo.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this DeviceinfoSerialNumberInfo.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this DeviceinfoSerialNumberInfo.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this DeviceinfoSerialNumberInfo.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this DeviceinfoSerialNumberInfo.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this DeviceinfoSerialNumberInfo.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this DeviceinfoSerialNumberInfo.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this DeviceinfoSerialNumberInfo.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this DeviceinfoSerialNumberInfo.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this DeviceinfoSerialNumberInfo.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this DeviceinfoSerialNumberInfo.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this DeviceinfoSerialNumberInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this DeviceinfoSerialNumberInfo.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this DeviceinfoSerialNumberInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this DeviceinfoSerialNumberInfo.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this DeviceinfoSerialNumberInfo.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this DeviceinfoSerialNumberInfo.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this DeviceinfoSerialNumberInfo.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this DeviceinfoSerialNumberInfo.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this DeviceinfoSerialNumberInfo.
        The versioning info for this managed object   

        :return: The version_context of this DeviceinfoSerialNumberInfo.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this DeviceinfoSerialNumberInfo.
        The versioning info for this managed object   

        :param version_context: The version_context of this DeviceinfoSerialNumberInfo.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def covered_product_line_end_date(self):
        """
        Gets the covered_product_line_end_date of this DeviceinfoSerialNumberInfo.

        :return: The covered_product_line_end_date of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._covered_product_line_end_date

    @covered_product_line_end_date.setter
    def covered_product_line_end_date(self, covered_product_line_end_date):
        """
        Sets the covered_product_line_end_date of this DeviceinfoSerialNumberInfo.

        :param covered_product_line_end_date: The covered_product_line_end_date of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._covered_product_line_end_date = covered_product_line_end_date

    @property
    def customer_address(self):
        """
        Gets the customer_address of this DeviceinfoSerialNumberInfo.

        :return: The customer_address of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._customer_address

    @customer_address.setter
    def customer_address(self, customer_address):
        """
        Sets the customer_address of this DeviceinfoSerialNumberInfo.

        :param customer_address: The customer_address of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._customer_address = customer_address

    @property
    def customer_city(self):
        """
        Gets the customer_city of this DeviceinfoSerialNumberInfo.

        :return: The customer_city of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._customer_city

    @customer_city.setter
    def customer_city(self, customer_city):
        """
        Sets the customer_city of this DeviceinfoSerialNumberInfo.

        :param customer_city: The customer_city of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._customer_city = customer_city

    @property
    def customer_country(self):
        """
        Gets the customer_country of this DeviceinfoSerialNumberInfo.

        :return: The customer_country of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._customer_country

    @customer_country.setter
    def customer_country(self, customer_country):
        """
        Sets the customer_country of this DeviceinfoSerialNumberInfo.

        :param customer_country: The customer_country of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._customer_country = customer_country

    @property
    def customer_name(self):
        """
        Gets the customer_name of this DeviceinfoSerialNumberInfo.

        :return: The customer_name of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """
        Sets the customer_name of this DeviceinfoSerialNumberInfo.

        :param customer_name: The customer_name of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._customer_name = customer_name

    @property
    def customer_province(self):
        """
        Gets the customer_province of this DeviceinfoSerialNumberInfo.

        :return: The customer_province of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._customer_province

    @customer_province.setter
    def customer_province(self, customer_province):
        """
        Sets the customer_province of this DeviceinfoSerialNumberInfo.

        :param customer_province: The customer_province of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._customer_province = customer_province

    @property
    def is_valid(self):
        """
        Gets the is_valid of this DeviceinfoSerialNumberInfo.

        :return: The is_valid of this DeviceinfoSerialNumberInfo.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """
        Sets the is_valid of this DeviceinfoSerialNumberInfo.

        :param is_valid: The is_valid of this DeviceinfoSerialNumberInfo.
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def item_description(self):
        """
        Gets the item_description of this DeviceinfoSerialNumberInfo.

        :return: The item_description of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._item_description

    @item_description.setter
    def item_description(self, item_description):
        """
        Sets the item_description of this DeviceinfoSerialNumberInfo.

        :param item_description: The item_description of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._item_description = item_description

    @property
    def orderable_pid(self):
        """
        Gets the orderable_pid of this DeviceinfoSerialNumberInfo.

        :return: The orderable_pid of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._orderable_pid

    @orderable_pid.setter
    def orderable_pid(self, orderable_pid):
        """
        Sets the orderable_pid of this DeviceinfoSerialNumberInfo.

        :param orderable_pid: The orderable_pid of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._orderable_pid = orderable_pid

    @property
    def registered_device(self):
        """
        Gets the registered_device of this DeviceinfoSerialNumberInfo.

        :return: The registered_device of this DeviceinfoSerialNumberInfo.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this DeviceinfoSerialNumberInfo.

        :param registered_device: The registered_device of this DeviceinfoSerialNumberInfo.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def serial_number(self):
        """
        Gets the serial_number of this DeviceinfoSerialNumberInfo.

        :return: The serial_number of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this DeviceinfoSerialNumberInfo.

        :param serial_number: The serial_number of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._serial_number = serial_number

    @property
    def service_contract_number(self):
        """
        Gets the service_contract_number of this DeviceinfoSerialNumberInfo.

        :return: The service_contract_number of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._service_contract_number

    @service_contract_number.setter
    def service_contract_number(self, service_contract_number):
        """
        Sets the service_contract_number of this DeviceinfoSerialNumberInfo.

        :param service_contract_number: The service_contract_number of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._service_contract_number = service_contract_number

    @property
    def service_line_descr(self):
        """
        Gets the service_line_descr of this DeviceinfoSerialNumberInfo.

        :return: The service_line_descr of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._service_line_descr

    @service_line_descr.setter
    def service_line_descr(self, service_line_descr):
        """
        Sets the service_line_descr of this DeviceinfoSerialNumberInfo.

        :param service_line_descr: The service_line_descr of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._service_line_descr = service_line_descr

    @property
    def warranty_end_date(self):
        """
        Gets the warranty_end_date of this DeviceinfoSerialNumberInfo.

        :return: The warranty_end_date of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._warranty_end_date

    @warranty_end_date.setter
    def warranty_end_date(self, warranty_end_date):
        """
        Sets the warranty_end_date of this DeviceinfoSerialNumberInfo.

        :param warranty_end_date: The warranty_end_date of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._warranty_end_date = warranty_end_date

    @property
    def warranty_type(self):
        """
        Gets the warranty_type of this DeviceinfoSerialNumberInfo.

        :return: The warranty_type of this DeviceinfoSerialNumberInfo.
        :rtype: str
        """
        return self._warranty_type

    @warranty_type.setter
    def warranty_type(self, warranty_type):
        """
        Sets the warranty_type of this DeviceinfoSerialNumberInfo.

        :param warranty_type: The warranty_type of this DeviceinfoSerialNumberInfo.
        :type: str
        """

        self._warranty_type = warranty_type

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
        if not isinstance(other, DeviceinfoSerialNumberInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
