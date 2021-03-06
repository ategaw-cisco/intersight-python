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


class IaasDeviceStatus(object):
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
        'account_name': 'str',
        'account_type': 'str',
        'connection_status': 'str',
        'device_model': 'str',
        'device_vendor': 'str',
        'device_version': 'str',
        'guid': 'IaasUcsdInfoRef',
        'ip_address': 'str',
        'pod': 'str',
        'pod_type': 'str'
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
        'account_name': 'AccountName',
        'account_type': 'AccountType',
        'connection_status': 'ConnectionStatus',
        'device_model': 'DeviceModel',
        'device_vendor': 'DeviceVendor',
        'device_version': 'DeviceVersion',
        'guid': 'Guid',
        'ip_address': 'IpAddress',
        'pod': 'Pod',
        'pod_type': 'PodType'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, account_name=None, account_type=None, connection_status=None, device_model=None, device_vendor=None, device_version=None, guid=None, ip_address=None, pod=None, pod_type=None):
        """
        IaasDeviceStatus - a model defined in Swagger
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
        self._account_name = None
        self._account_type = None
        self._connection_status = None
        self._device_model = None
        self._device_vendor = None
        self._device_version = None
        self._guid = None
        self._ip_address = None
        self._pod = None
        self._pod_type = None

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
        if account_name is not None:
          self.account_name = account_name
        if account_type is not None:
          self.account_type = account_type
        if connection_status is not None:
          self.connection_status = connection_status
        if device_model is not None:
          self.device_model = device_model
        if device_vendor is not None:
          self.device_vendor = device_vendor
        if device_version is not None:
          self.device_version = device_version
        if guid is not None:
          self.guid = guid
        if ip_address is not None:
          self.ip_address = ip_address
        if pod is not None:
          self.pod = pod
        if pod_type is not None:
          self.pod_type = pod_type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IaasDeviceStatus.
        The Account ID for this managed object.  

        :return: The account_moid of this IaasDeviceStatus.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IaasDeviceStatus.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IaasDeviceStatus.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IaasDeviceStatus.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IaasDeviceStatus.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IaasDeviceStatus.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IaasDeviceStatus.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IaasDeviceStatus.
        The time when this managed object was created.  

        :return: The create_time of this IaasDeviceStatus.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IaasDeviceStatus.
        The time when this managed object was created.  

        :param create_time: The create_time of this IaasDeviceStatus.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IaasDeviceStatus.
        The time when this managed object was last modified.  

        :return: The mod_time of this IaasDeviceStatus.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IaasDeviceStatus.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IaasDeviceStatus.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IaasDeviceStatus.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IaasDeviceStatus.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IaasDeviceStatus.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IaasDeviceStatus.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IaasDeviceStatus.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IaasDeviceStatus.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IaasDeviceStatus.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IaasDeviceStatus.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IaasDeviceStatus.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IaasDeviceStatus.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IaasDeviceStatus.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IaasDeviceStatus.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IaasDeviceStatus.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IaasDeviceStatus.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IaasDeviceStatus.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IaasDeviceStatus.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IaasDeviceStatus.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IaasDeviceStatus.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IaasDeviceStatus.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IaasDeviceStatus.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IaasDeviceStatus.
        The versioning info for this managed object   

        :return: The version_context of this IaasDeviceStatus.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IaasDeviceStatus.
        The versioning info for this managed object   

        :param version_context: The version_context of this IaasDeviceStatus.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account_name(self):
        """
        Gets the account_name of this IaasDeviceStatus.
        The UCSD infra account name. Account Name is created when UCSD admin adds any new infra account(Physical/Virtual/Compute/Network) to be managed by UCSD  

        :return: The account_name of this IaasDeviceStatus.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this IaasDeviceStatus.
        The UCSD infra account name. Account Name is created when UCSD admin adds any new infra account(Physical/Virtual/Compute/Network) to be managed by UCSD  

        :param account_name: The account_name of this IaasDeviceStatus.
        :type: str
        """

        self._account_name = account_name

    @property
    def account_type(self):
        """
        Gets the account_type of this IaasDeviceStatus.
        The UCSD Infra Account type  

        :return: The account_type of this IaasDeviceStatus.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this IaasDeviceStatus.
        The UCSD Infra Account type  

        :param account_type: The account_type of this IaasDeviceStatus.
        :type: str
        """

        self._account_type = account_type

    @property
    def connection_status(self):
        """
        Gets the connection_status of this IaasDeviceStatus.
        Describes about the connection status between the UCSD and the actual end device  

        :return: The connection_status of this IaasDeviceStatus.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this IaasDeviceStatus.
        Describes about the connection status between the UCSD and the actual end device  

        :param connection_status: The connection_status of this IaasDeviceStatus.
        :type: str
        """

        self._connection_status = connection_status

    @property
    def device_model(self):
        """
        Gets the device_model of this IaasDeviceStatus.
        Describes about the device model  

        :return: The device_model of this IaasDeviceStatus.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this IaasDeviceStatus.
        Describes about the device model  

        :param device_model: The device_model of this IaasDeviceStatus.
        :type: str
        """

        self._device_model = device_model

    @property
    def device_vendor(self):
        """
        Gets the device_vendor of this IaasDeviceStatus.
        Describes about the device vendor/manufacturer of the device  

        :return: The device_vendor of this IaasDeviceStatus.
        :rtype: str
        """
        return self._device_vendor

    @device_vendor.setter
    def device_vendor(self, device_vendor):
        """
        Sets the device_vendor of this IaasDeviceStatus.
        Describes about the device vendor/manufacturer of the device  

        :param device_vendor: The device_vendor of this IaasDeviceStatus.
        :type: str
        """

        self._device_vendor = device_vendor

    @property
    def device_version(self):
        """
        Gets the device_version of this IaasDeviceStatus.
        Describes about the current firmware version running on the device  

        :return: The device_version of this IaasDeviceStatus.
        :rtype: str
        """
        return self._device_version

    @device_version.setter
    def device_version(self, device_version):
        """
        Sets the device_version of this IaasDeviceStatus.
        Describes about the current firmware version running on the device  

        :param device_version: The device_version of this IaasDeviceStatus.
        :type: str
        """

        self._device_version = device_version

    @property
    def guid(self):
        """
        Gets the guid of this IaasDeviceStatus.

        :return: The guid of this IaasDeviceStatus.
        :rtype: IaasUcsdInfoRef
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this IaasDeviceStatus.

        :param guid: The guid of this IaasDeviceStatus.
        :type: IaasUcsdInfoRef
        """

        self._guid = guid

    @property
    def ip_address(self):
        """
        Gets the ip_address of this IaasDeviceStatus.
        The IPAddress of the device  

        :return: The ip_address of this IaasDeviceStatus.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this IaasDeviceStatus.
        The IPAddress of the device  

        :param ip_address: The ip_address of this IaasDeviceStatus.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def pod(self):
        """
        Gets the pod of this IaasDeviceStatus.
        Describes about the pod to which this device belongs to in UCSD  

        :return: The pod of this IaasDeviceStatus.
        :rtype: str
        """
        return self._pod

    @pod.setter
    def pod(self, pod):
        """
        Sets the pod of this IaasDeviceStatus.
        Describes about the pod to which this device belongs to in UCSD  

        :param pod: The pod of this IaasDeviceStatus.
        :type: str
        """

        self._pod = pod

    @property
    def pod_type(self):
        """
        Gets the pod_type of this IaasDeviceStatus.
        Describes about the podType of Pod to which this device belongs to in UCSD   

        :return: The pod_type of this IaasDeviceStatus.
        :rtype: str
        """
        return self._pod_type

    @pod_type.setter
    def pod_type(self, pod_type):
        """
        Sets the pod_type of this IaasDeviceStatus.
        Describes about the podType of Pod to which this device belongs to in UCSD   

        :param pod_type: The pod_type of this IaasDeviceStatus.
        :type: str
        """

        self._pod_type = pod_type

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
        if not isinstance(other, IaasDeviceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
