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


class ComputeBoard(object):
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
        'board_id': 'int',
        'compute_blade': 'ComputeBladeRef',
        'compute_rack_unit': 'ComputeRackUnitRef',
        'cpu_type_controller': 'str',
        'equipment_tpms': 'list[EquipmentTpmRef]',
        'graphics_cards': 'list[GraphicsCardRef]',
        'memory_arrays': 'list[MemoryArrayRef]',
        'oper_power_state': 'str',
        'presence': 'str',
        'processors': 'list[ProcessorUnitRef]',
        'registered_device': 'AssetDeviceRegistrationRef',
        'security_units': 'list[SecurityUnitRef]',
        'storage_controllers': 'list[StorageControllerRef]',
        'storage_flex_flash_controllers': 'list[StorageFlexFlashControllerRef]',
        'storage_flex_util_controllers': 'list[StorageFlexUtilControllerRef]'
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
        'board_id': 'BoardId',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'cpu_type_controller': 'CpuTypeController',
        'equipment_tpms': 'EquipmentTpms',
        'graphics_cards': 'GraphicsCards',
        'memory_arrays': 'MemoryArrays',
        'oper_power_state': 'OperPowerState',
        'presence': 'Presence',
        'processors': 'Processors',
        'registered_device': 'RegisteredDevice',
        'security_units': 'SecurityUnits',
        'storage_controllers': 'StorageControllers',
        'storage_flex_flash_controllers': 'StorageFlexFlashControllers',
        'storage_flex_util_controllers': 'StorageFlexUtilControllers'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, board_id=None, compute_blade=None, compute_rack_unit=None, cpu_type_controller=None, equipment_tpms=None, graphics_cards=None, memory_arrays=None, oper_power_state=None, presence=None, processors=None, registered_device=None, security_units=None, storage_controllers=None, storage_flex_flash_controllers=None, storage_flex_util_controllers=None):
        """
        ComputeBoard - a model defined in Swagger
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
        self._board_id = None
        self._compute_blade = None
        self._compute_rack_unit = None
        self._cpu_type_controller = None
        self._equipment_tpms = None
        self._graphics_cards = None
        self._memory_arrays = None
        self._oper_power_state = None
        self._presence = None
        self._processors = None
        self._registered_device = None
        self._security_units = None
        self._storage_controllers = None
        self._storage_flex_flash_controllers = None
        self._storage_flex_util_controllers = None

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
        if board_id is not None:
          self.board_id = board_id
        if compute_blade is not None:
          self.compute_blade = compute_blade
        if compute_rack_unit is not None:
          self.compute_rack_unit = compute_rack_unit
        if cpu_type_controller is not None:
          self.cpu_type_controller = cpu_type_controller
        if equipment_tpms is not None:
          self.equipment_tpms = equipment_tpms
        if graphics_cards is not None:
          self.graphics_cards = graphics_cards
        if memory_arrays is not None:
          self.memory_arrays = memory_arrays
        if oper_power_state is not None:
          self.oper_power_state = oper_power_state
        if presence is not None:
          self.presence = presence
        if processors is not None:
          self.processors = processors
        if registered_device is not None:
          self.registered_device = registered_device
        if security_units is not None:
          self.security_units = security_units
        if storage_controllers is not None:
          self.storage_controllers = storage_controllers
        if storage_flex_flash_controllers is not None:
          self.storage_flex_flash_controllers = storage_flex_flash_controllers
        if storage_flex_util_controllers is not None:
          self.storage_flex_util_controllers = storage_flex_util_controllers

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ComputeBoard.
        The Account ID for this managed object.  

        :return: The account_moid of this ComputeBoard.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ComputeBoard.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ComputeBoard.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ComputeBoard.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ComputeBoard.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ComputeBoard.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ComputeBoard.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ComputeBoard.
        The time when this managed object was created.  

        :return: The create_time of this ComputeBoard.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ComputeBoard.
        The time when this managed object was created.  

        :param create_time: The create_time of this ComputeBoard.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ComputeBoard.
        The time when this managed object was last modified.  

        :return: The mod_time of this ComputeBoard.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ComputeBoard.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ComputeBoard.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ComputeBoard.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this ComputeBoard.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ComputeBoard.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this ComputeBoard.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ComputeBoard.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ComputeBoard.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ComputeBoard.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ComputeBoard.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ComputeBoard.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this ComputeBoard.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ComputeBoard.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ComputeBoard.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ComputeBoard.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ComputeBoard.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ComputeBoard.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ComputeBoard.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this ComputeBoard.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this ComputeBoard.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ComputeBoard.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this ComputeBoard.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this ComputeBoard.
        The versioning info for this managed object   

        :return: The version_context of this ComputeBoard.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this ComputeBoard.
        The versioning info for this managed object   

        :param version_context: The version_context of this ComputeBoard.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this ComputeBoard.

        :return: The device_mo_id of this ComputeBoard.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this ComputeBoard.

        :param device_mo_id: The device_mo_id of this ComputeBoard.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this ComputeBoard.

        :return: The dn of this ComputeBoard.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this ComputeBoard.

        :param dn: The dn of this ComputeBoard.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this ComputeBoard.

        :return: The rn of this ComputeBoard.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this ComputeBoard.

        :param rn: The rn of this ComputeBoard.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this ComputeBoard.

        :return: The model of this ComputeBoard.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ComputeBoard.

        :param model: The model of this ComputeBoard.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this ComputeBoard.

        :return: The revision of this ComputeBoard.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ComputeBoard.

        :param revision: The revision of this ComputeBoard.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this ComputeBoard.

        :return: The serial of this ComputeBoard.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this ComputeBoard.

        :param serial: The serial of this ComputeBoard.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this ComputeBoard.

        :return: The vendor of this ComputeBoard.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this ComputeBoard.

        :param vendor: The vendor of this ComputeBoard.
        :type: str
        """

        self._vendor = vendor

    @property
    def board_id(self):
        """
        Gets the board_id of this ComputeBoard.

        :return: The board_id of this ComputeBoard.
        :rtype: int
        """
        return self._board_id

    @board_id.setter
    def board_id(self, board_id):
        """
        Sets the board_id of this ComputeBoard.

        :param board_id: The board_id of this ComputeBoard.
        :type: int
        """

        self._board_id = board_id

    @property
    def compute_blade(self):
        """
        Gets the compute_blade of this ComputeBoard.

        :return: The compute_blade of this ComputeBoard.
        :rtype: ComputeBladeRef
        """
        return self._compute_blade

    @compute_blade.setter
    def compute_blade(self, compute_blade):
        """
        Sets the compute_blade of this ComputeBoard.

        :param compute_blade: The compute_blade of this ComputeBoard.
        :type: ComputeBladeRef
        """

        self._compute_blade = compute_blade

    @property
    def compute_rack_unit(self):
        """
        Gets the compute_rack_unit of this ComputeBoard.

        :return: The compute_rack_unit of this ComputeBoard.
        :rtype: ComputeRackUnitRef
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """
        Sets the compute_rack_unit of this ComputeBoard.

        :param compute_rack_unit: The compute_rack_unit of this ComputeBoard.
        :type: ComputeRackUnitRef
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def cpu_type_controller(self):
        """
        Gets the cpu_type_controller of this ComputeBoard.

        :return: The cpu_type_controller of this ComputeBoard.
        :rtype: str
        """
        return self._cpu_type_controller

    @cpu_type_controller.setter
    def cpu_type_controller(self, cpu_type_controller):
        """
        Sets the cpu_type_controller of this ComputeBoard.

        :param cpu_type_controller: The cpu_type_controller of this ComputeBoard.
        :type: str
        """

        self._cpu_type_controller = cpu_type_controller

    @property
    def equipment_tpms(self):
        """
        Gets the equipment_tpms of this ComputeBoard.

        :return: The equipment_tpms of this ComputeBoard.
        :rtype: list[EquipmentTpmRef]
        """
        return self._equipment_tpms

    @equipment_tpms.setter
    def equipment_tpms(self, equipment_tpms):
        """
        Sets the equipment_tpms of this ComputeBoard.

        :param equipment_tpms: The equipment_tpms of this ComputeBoard.
        :type: list[EquipmentTpmRef]
        """

        self._equipment_tpms = equipment_tpms

    @property
    def graphics_cards(self):
        """
        Gets the graphics_cards of this ComputeBoard.

        :return: The graphics_cards of this ComputeBoard.
        :rtype: list[GraphicsCardRef]
        """
        return self._graphics_cards

    @graphics_cards.setter
    def graphics_cards(self, graphics_cards):
        """
        Sets the graphics_cards of this ComputeBoard.

        :param graphics_cards: The graphics_cards of this ComputeBoard.
        :type: list[GraphicsCardRef]
        """

        self._graphics_cards = graphics_cards

    @property
    def memory_arrays(self):
        """
        Gets the memory_arrays of this ComputeBoard.

        :return: The memory_arrays of this ComputeBoard.
        :rtype: list[MemoryArrayRef]
        """
        return self._memory_arrays

    @memory_arrays.setter
    def memory_arrays(self, memory_arrays):
        """
        Sets the memory_arrays of this ComputeBoard.

        :param memory_arrays: The memory_arrays of this ComputeBoard.
        :type: list[MemoryArrayRef]
        """

        self._memory_arrays = memory_arrays

    @property
    def oper_power_state(self):
        """
        Gets the oper_power_state of this ComputeBoard.

        :return: The oper_power_state of this ComputeBoard.
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """
        Sets the oper_power_state of this ComputeBoard.

        :param oper_power_state: The oper_power_state of this ComputeBoard.
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def presence(self):
        """
        Gets the presence of this ComputeBoard.

        :return: The presence of this ComputeBoard.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this ComputeBoard.

        :param presence: The presence of this ComputeBoard.
        :type: str
        """

        self._presence = presence

    @property
    def processors(self):
        """
        Gets the processors of this ComputeBoard.

        :return: The processors of this ComputeBoard.
        :rtype: list[ProcessorUnitRef]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """
        Sets the processors of this ComputeBoard.

        :param processors: The processors of this ComputeBoard.
        :type: list[ProcessorUnitRef]
        """

        self._processors = processors

    @property
    def registered_device(self):
        """
        Gets the registered_device of this ComputeBoard.

        :return: The registered_device of this ComputeBoard.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this ComputeBoard.

        :param registered_device: The registered_device of this ComputeBoard.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def security_units(self):
        """
        Gets the security_units of this ComputeBoard.

        :return: The security_units of this ComputeBoard.
        :rtype: list[SecurityUnitRef]
        """
        return self._security_units

    @security_units.setter
    def security_units(self, security_units):
        """
        Sets the security_units of this ComputeBoard.

        :param security_units: The security_units of this ComputeBoard.
        :type: list[SecurityUnitRef]
        """

        self._security_units = security_units

    @property
    def storage_controllers(self):
        """
        Gets the storage_controllers of this ComputeBoard.

        :return: The storage_controllers of this ComputeBoard.
        :rtype: list[StorageControllerRef]
        """
        return self._storage_controllers

    @storage_controllers.setter
    def storage_controllers(self, storage_controllers):
        """
        Sets the storage_controllers of this ComputeBoard.

        :param storage_controllers: The storage_controllers of this ComputeBoard.
        :type: list[StorageControllerRef]
        """

        self._storage_controllers = storage_controllers

    @property
    def storage_flex_flash_controllers(self):
        """
        Gets the storage_flex_flash_controllers of this ComputeBoard.

        :return: The storage_flex_flash_controllers of this ComputeBoard.
        :rtype: list[StorageFlexFlashControllerRef]
        """
        return self._storage_flex_flash_controllers

    @storage_flex_flash_controllers.setter
    def storage_flex_flash_controllers(self, storage_flex_flash_controllers):
        """
        Sets the storage_flex_flash_controllers of this ComputeBoard.

        :param storage_flex_flash_controllers: The storage_flex_flash_controllers of this ComputeBoard.
        :type: list[StorageFlexFlashControllerRef]
        """

        self._storage_flex_flash_controllers = storage_flex_flash_controllers

    @property
    def storage_flex_util_controllers(self):
        """
        Gets the storage_flex_util_controllers of this ComputeBoard.

        :return: The storage_flex_util_controllers of this ComputeBoard.
        :rtype: list[StorageFlexUtilControllerRef]
        """
        return self._storage_flex_util_controllers

    @storage_flex_util_controllers.setter
    def storage_flex_util_controllers(self, storage_flex_util_controllers):
        """
        Sets the storage_flex_util_controllers of this ComputeBoard.

        :param storage_flex_util_controllers: The storage_flex_util_controllers of this ComputeBoard.
        :type: list[StorageFlexUtilControllerRef]
        """

        self._storage_flex_util_controllers = storage_flex_util_controllers

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
        if not isinstance(other, ComputeBoard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
