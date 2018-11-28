# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-263
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StorageEnclosure(object):
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
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'chassis_id': 'int',
        'compute_blade': 'ComputeBladeRef',
        'compute_rack_unit': 'ComputeRackUnitRef',
        'description': 'str',
        'enclosure_id': 'int',
        'equipment_chassis': 'EquipmentChassisRef',
        'num_slots': 'int',
        'physical_disks': 'list[StoragePhysicalDiskRef]',
        'presence': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'server_id': 'int',
        'type': 'str'
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
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'chassis_id': 'ChassisId',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'description': 'Description',
        'enclosure_id': 'EnclosureId',
        'equipment_chassis': 'EquipmentChassis',
        'num_slots': 'NumSlots',
        'physical_disks': 'PhysicalDisks',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice',
        'server_id': 'ServerId',
        'type': 'Type'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, chassis_id=None, compute_blade=None, compute_rack_unit=None, description=None, enclosure_id=None, equipment_chassis=None, num_slots=None, physical_disks=None, presence=None, registered_device=None, server_id=None, type=None):
        """
        StorageEnclosure - a model defined in Swagger
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
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._chassis_id = None
        self._compute_blade = None
        self._compute_rack_unit = None
        self._description = None
        self._enclosure_id = None
        self._equipment_chassis = None
        self._num_slots = None
        self._physical_disks = None
        self._presence = None
        self._registered_device = None
        self._server_id = None
        self._type = None

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
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if chassis_id is not None:
          self.chassis_id = chassis_id
        if compute_blade is not None:
          self.compute_blade = compute_blade
        if compute_rack_unit is not None:
          self.compute_rack_unit = compute_rack_unit
        if description is not None:
          self.description = description
        if enclosure_id is not None:
          self.enclosure_id = enclosure_id
        if equipment_chassis is not None:
          self.equipment_chassis = equipment_chassis
        if num_slots is not None:
          self.num_slots = num_slots
        if physical_disks is not None:
          self.physical_disks = physical_disks
        if presence is not None:
          self.presence = presence
        if registered_device is not None:
          self.registered_device = registered_device
        if server_id is not None:
          self.server_id = server_id
        if type is not None:
          self.type = type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageEnclosure.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageEnclosure.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageEnclosure.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageEnclosure.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageEnclosure.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageEnclosure.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageEnclosure.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageEnclosure.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageEnclosure.
        The time when this managed object was created.  

        :return: The create_time of this StorageEnclosure.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageEnclosure.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageEnclosure.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageEnclosure.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageEnclosure.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageEnclosure.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageEnclosure.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageEnclosure.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageEnclosure.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageEnclosure.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageEnclosure.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageEnclosure.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageEnclosure.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageEnclosure.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageEnclosure.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageEnclosure.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageEnclosure.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageEnclosure.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageEnclosure.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageEnclosure.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageEnclosure.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageEnclosure.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageEnclosure.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this StorageEnclosure.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageEnclosure.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageEnclosure.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageEnclosure.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageEnclosure.
        The versioning info for this managed object   

        :return: The version_context of this StorageEnclosure.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageEnclosure.
        The versioning info for this managed object   

        :param version_context: The version_context of this StorageEnclosure.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageEnclosure.

        :return: The device_mo_id of this StorageEnclosure.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageEnclosure.

        :param device_mo_id: The device_mo_id of this StorageEnclosure.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageEnclosure.

        :return: The dn of this StorageEnclosure.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageEnclosure.

        :param dn: The dn of this StorageEnclosure.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageEnclosure.

        :return: The rn of this StorageEnclosure.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageEnclosure.

        :param rn: The rn of this StorageEnclosure.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageEnclosure.

        :return: The model of this StorageEnclosure.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageEnclosure.

        :param model: The model of this StorageEnclosure.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this StorageEnclosure.

        :return: The revision of this StorageEnclosure.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this StorageEnclosure.

        :param revision: The revision of this StorageEnclosure.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this StorageEnclosure.

        :return: The serial of this StorageEnclosure.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageEnclosure.

        :param serial: The serial of this StorageEnclosure.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageEnclosure.

        :return: The vendor of this StorageEnclosure.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageEnclosure.

        :param vendor: The vendor of this StorageEnclosure.
        :type: str
        """

        self._vendor = vendor

    @property
    def chassis_id(self):
        """
        Gets the chassis_id of this StorageEnclosure.

        :return: The chassis_id of this StorageEnclosure.
        :rtype: int
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        """
        Sets the chassis_id of this StorageEnclosure.

        :param chassis_id: The chassis_id of this StorageEnclosure.
        :type: int
        """

        self._chassis_id = chassis_id

    @property
    def compute_blade(self):
        """
        Gets the compute_blade of this StorageEnclosure.

        :return: The compute_blade of this StorageEnclosure.
        :rtype: ComputeBladeRef
        """
        return self._compute_blade

    @compute_blade.setter
    def compute_blade(self, compute_blade):
        """
        Sets the compute_blade of this StorageEnclosure.

        :param compute_blade: The compute_blade of this StorageEnclosure.
        :type: ComputeBladeRef
        """

        self._compute_blade = compute_blade

    @property
    def compute_rack_unit(self):
        """
        Gets the compute_rack_unit of this StorageEnclosure.

        :return: The compute_rack_unit of this StorageEnclosure.
        :rtype: ComputeRackUnitRef
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """
        Sets the compute_rack_unit of this StorageEnclosure.

        :param compute_rack_unit: The compute_rack_unit of this StorageEnclosure.
        :type: ComputeRackUnitRef
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def description(self):
        """
        Gets the description of this StorageEnclosure.

        :return: The description of this StorageEnclosure.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StorageEnclosure.

        :param description: The description of this StorageEnclosure.
        :type: str
        """

        self._description = description

    @property
    def enclosure_id(self):
        """
        Gets the enclosure_id of this StorageEnclosure.

        :return: The enclosure_id of this StorageEnclosure.
        :rtype: int
        """
        return self._enclosure_id

    @enclosure_id.setter
    def enclosure_id(self, enclosure_id):
        """
        Sets the enclosure_id of this StorageEnclosure.

        :param enclosure_id: The enclosure_id of this StorageEnclosure.
        :type: int
        """

        self._enclosure_id = enclosure_id

    @property
    def equipment_chassis(self):
        """
        Gets the equipment_chassis of this StorageEnclosure.

        :return: The equipment_chassis of this StorageEnclosure.
        :rtype: EquipmentChassisRef
        """
        return self._equipment_chassis

    @equipment_chassis.setter
    def equipment_chassis(self, equipment_chassis):
        """
        Sets the equipment_chassis of this StorageEnclosure.

        :param equipment_chassis: The equipment_chassis of this StorageEnclosure.
        :type: EquipmentChassisRef
        """

        self._equipment_chassis = equipment_chassis

    @property
    def num_slots(self):
        """
        Gets the num_slots of this StorageEnclosure.

        :return: The num_slots of this StorageEnclosure.
        :rtype: int
        """
        return self._num_slots

    @num_slots.setter
    def num_slots(self, num_slots):
        """
        Sets the num_slots of this StorageEnclosure.

        :param num_slots: The num_slots of this StorageEnclosure.
        :type: int
        """

        self._num_slots = num_slots

    @property
    def physical_disks(self):
        """
        Gets the physical_disks of this StorageEnclosure.

        :return: The physical_disks of this StorageEnclosure.
        :rtype: list[StoragePhysicalDiskRef]
        """
        return self._physical_disks

    @physical_disks.setter
    def physical_disks(self, physical_disks):
        """
        Sets the physical_disks of this StorageEnclosure.

        :param physical_disks: The physical_disks of this StorageEnclosure.
        :type: list[StoragePhysicalDiskRef]
        """

        self._physical_disks = physical_disks

    @property
    def presence(self):
        """
        Gets the presence of this StorageEnclosure.

        :return: The presence of this StorageEnclosure.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this StorageEnclosure.

        :param presence: The presence of this StorageEnclosure.
        :type: str
        """

        self._presence = presence

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageEnclosure.

        :return: The registered_device of this StorageEnclosure.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageEnclosure.

        :param registered_device: The registered_device of this StorageEnclosure.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def server_id(self):
        """
        Gets the server_id of this StorageEnclosure.

        :return: The server_id of this StorageEnclosure.
        :rtype: int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """
        Sets the server_id of this StorageEnclosure.

        :param server_id: The server_id of this StorageEnclosure.
        :type: int
        """

        self._server_id = server_id

    @property
    def type(self):
        """
        Gets the type of this StorageEnclosure.

        :return: The type of this StorageEnclosure.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StorageEnclosure.

        :param type: The type of this StorageEnclosure.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, StorageEnclosure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
