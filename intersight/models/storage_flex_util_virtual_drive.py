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


class StorageFlexUtilVirtualDrive(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'drive_status': 'str',
        'drive_type': 'str',
        'partition_id': 'str',
        'partition_name': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'resident_image': 'str',
        'size': 'str',
        'storage_flex_util_controller': 'StorageFlexUtilControllerRef',
        'virtual_drive': 'str'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'drive_status': 'DriveStatus',
        'drive_type': 'DriveType',
        'partition_id': 'PartitionId',
        'partition_name': 'PartitionName',
        'registered_device': 'RegisteredDevice',
        'resident_image': 'ResidentImage',
        'size': 'Size',
        'storage_flex_util_controller': 'StorageFlexUtilController',
        'virtual_drive': 'VirtualDrive'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, drive_status=None, drive_type=None, partition_id=None, partition_name=None, registered_device=None, resident_image=None, size=None, storage_flex_util_controller=None, virtual_drive=None):
        """
        StorageFlexUtilVirtualDrive - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._drive_status = None
        self._drive_type = None
        self._partition_id = None
        self._partition_name = None
        self._registered_device = None
        self._resident_image = None
        self._size = None
        self._storage_flex_util_controller = None
        self._virtual_drive = None

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
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if drive_status is not None:
          self.drive_status = drive_status
        if drive_type is not None:
          self.drive_type = drive_type
        if partition_id is not None:
          self.partition_id = partition_id
        if partition_name is not None:
          self.partition_name = partition_name
        if registered_device is not None:
          self.registered_device = registered_device
        if resident_image is not None:
          self.resident_image = resident_image
        if size is not None:
          self.size = size
        if storage_flex_util_controller is not None:
          self.storage_flex_util_controller = storage_flex_util_controller
        if virtual_drive is not None:
          self.virtual_drive = virtual_drive

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageFlexUtilVirtualDrive.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageFlexUtilVirtualDrive.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageFlexUtilVirtualDrive.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageFlexUtilVirtualDrive.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageFlexUtilVirtualDrive.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageFlexUtilVirtualDrive.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageFlexUtilVirtualDrive.
        The time when this managed object was created.  

        :return: The create_time of this StorageFlexUtilVirtualDrive.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageFlexUtilVirtualDrive.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageFlexUtilVirtualDrive.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageFlexUtilVirtualDrive.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageFlexUtilVirtualDrive.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageFlexUtilVirtualDrive.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageFlexUtilVirtualDrive.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageFlexUtilVirtualDrive.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageFlexUtilVirtualDrive.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageFlexUtilVirtualDrive.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageFlexUtilVirtualDrive.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageFlexUtilVirtualDrive.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageFlexUtilVirtualDrive.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageFlexUtilVirtualDrive.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageFlexUtilVirtualDrive.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageFlexUtilVirtualDrive.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageFlexUtilVirtualDrive.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageFlexUtilVirtualDrive.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageFlexUtilVirtualDrive.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this StorageFlexUtilVirtualDrive.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageFlexUtilVirtualDrive.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageFlexUtilVirtualDrive.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageFlexUtilVirtualDrive.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageFlexUtilVirtualDrive.
        The versioning info for this managed object   

        :return: The version_context of this StorageFlexUtilVirtualDrive.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageFlexUtilVirtualDrive.
        The versioning info for this managed object   

        :param version_context: The version_context of this StorageFlexUtilVirtualDrive.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageFlexUtilVirtualDrive.

        :return: The device_mo_id of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageFlexUtilVirtualDrive.

        :param device_mo_id: The device_mo_id of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageFlexUtilVirtualDrive.

        :return: The dn of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageFlexUtilVirtualDrive.

        :param dn: The dn of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageFlexUtilVirtualDrive.

        :return: The rn of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageFlexUtilVirtualDrive.

        :param rn: The rn of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._rn = rn

    @property
    def drive_status(self):
        """
        Gets the drive_status of this StorageFlexUtilVirtualDrive.

        :return: The drive_status of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._drive_status

    @drive_status.setter
    def drive_status(self, drive_status):
        """
        Sets the drive_status of this StorageFlexUtilVirtualDrive.

        :param drive_status: The drive_status of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._drive_status = drive_status

    @property
    def drive_type(self):
        """
        Gets the drive_type of this StorageFlexUtilVirtualDrive.

        :return: The drive_type of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._drive_type

    @drive_type.setter
    def drive_type(self, drive_type):
        """
        Sets the drive_type of this StorageFlexUtilVirtualDrive.

        :param drive_type: The drive_type of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._drive_type = drive_type

    @property
    def partition_id(self):
        """
        Gets the partition_id of this StorageFlexUtilVirtualDrive.

        :return: The partition_id of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """
        Sets the partition_id of this StorageFlexUtilVirtualDrive.

        :param partition_id: The partition_id of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._partition_id = partition_id

    @property
    def partition_name(self):
        """
        Gets the partition_name of this StorageFlexUtilVirtualDrive.

        :return: The partition_name of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        """
        Sets the partition_name of this StorageFlexUtilVirtualDrive.

        :param partition_name: The partition_name of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._partition_name = partition_name

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageFlexUtilVirtualDrive.

        :return: The registered_device of this StorageFlexUtilVirtualDrive.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageFlexUtilVirtualDrive.

        :param registered_device: The registered_device of this StorageFlexUtilVirtualDrive.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def resident_image(self):
        """
        Gets the resident_image of this StorageFlexUtilVirtualDrive.

        :return: The resident_image of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._resident_image

    @resident_image.setter
    def resident_image(self, resident_image):
        """
        Sets the resident_image of this StorageFlexUtilVirtualDrive.

        :param resident_image: The resident_image of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._resident_image = resident_image

    @property
    def size(self):
        """
        Gets the size of this StorageFlexUtilVirtualDrive.

        :return: The size of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this StorageFlexUtilVirtualDrive.

        :param size: The size of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._size = size

    @property
    def storage_flex_util_controller(self):
        """
        Gets the storage_flex_util_controller of this StorageFlexUtilVirtualDrive.

        :return: The storage_flex_util_controller of this StorageFlexUtilVirtualDrive.
        :rtype: StorageFlexUtilControllerRef
        """
        return self._storage_flex_util_controller

    @storage_flex_util_controller.setter
    def storage_flex_util_controller(self, storage_flex_util_controller):
        """
        Sets the storage_flex_util_controller of this StorageFlexUtilVirtualDrive.

        :param storage_flex_util_controller: The storage_flex_util_controller of this StorageFlexUtilVirtualDrive.
        :type: StorageFlexUtilControllerRef
        """

        self._storage_flex_util_controller = storage_flex_util_controller

    @property
    def virtual_drive(self):
        """
        Gets the virtual_drive of this StorageFlexUtilVirtualDrive.

        :return: The virtual_drive of this StorageFlexUtilVirtualDrive.
        :rtype: str
        """
        return self._virtual_drive

    @virtual_drive.setter
    def virtual_drive(self, virtual_drive):
        """
        Sets the virtual_drive of this StorageFlexUtilVirtualDrive.

        :param virtual_drive: The virtual_drive of this StorageFlexUtilVirtualDrive.
        :type: str
        """

        self._virtual_drive = virtual_drive

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
        if not isinstance(other, StorageFlexUtilVirtualDrive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
