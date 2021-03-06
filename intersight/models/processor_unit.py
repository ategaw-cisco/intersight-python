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


class ProcessorUnit(object):
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
        'architecture': 'str',
        'compute_board': 'ComputeBoardRef',
        'num_cores': 'int',
        'num_cores_enabled': 'str',
        'num_threads': 'str',
        'oper_power_state': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'presence': 'str',
        'processor_id': 'int',
        'registered_device': 'AssetDeviceRegistrationRef',
        'socket_designation': 'str',
        'speed': 'float',
        'stepping': 'str',
        'thermal': 'str'
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
        'architecture': 'Architecture',
        'compute_board': 'ComputeBoard',
        'num_cores': 'NumCores',
        'num_cores_enabled': 'NumCoresEnabled',
        'num_threads': 'NumThreads',
        'oper_power_state': 'OperPowerState',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'presence': 'Presence',
        'processor_id': 'ProcessorId',
        'registered_device': 'RegisteredDevice',
        'socket_designation': 'SocketDesignation',
        'speed': 'Speed',
        'stepping': 'Stepping',
        'thermal': 'Thermal'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, architecture=None, compute_board=None, num_cores=None, num_cores_enabled=None, num_threads=None, oper_power_state=None, oper_state=None, operability=None, presence=None, processor_id=None, registered_device=None, socket_designation=None, speed=None, stepping=None, thermal=None):
        """
        ProcessorUnit - a model defined in Swagger
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
        self._architecture = None
        self._compute_board = None
        self._num_cores = None
        self._num_cores_enabled = None
        self._num_threads = None
        self._oper_power_state = None
        self._oper_state = None
        self._operability = None
        self._presence = None
        self._processor_id = None
        self._registered_device = None
        self._socket_designation = None
        self._speed = None
        self._stepping = None
        self._thermal = None

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
        if architecture is not None:
          self.architecture = architecture
        if compute_board is not None:
          self.compute_board = compute_board
        if num_cores is not None:
          self.num_cores = num_cores
        if num_cores_enabled is not None:
          self.num_cores_enabled = num_cores_enabled
        if num_threads is not None:
          self.num_threads = num_threads
        if oper_power_state is not None:
          self.oper_power_state = oper_power_state
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if presence is not None:
          self.presence = presence
        if processor_id is not None:
          self.processor_id = processor_id
        if registered_device is not None:
          self.registered_device = registered_device
        if socket_designation is not None:
          self.socket_designation = socket_designation
        if speed is not None:
          self.speed = speed
        if stepping is not None:
          self.stepping = stepping
        if thermal is not None:
          self.thermal = thermal

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ProcessorUnit.
        The Account ID for this managed object.  

        :return: The account_moid of this ProcessorUnit.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ProcessorUnit.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ProcessorUnit.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ProcessorUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ProcessorUnit.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ProcessorUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ProcessorUnit.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ProcessorUnit.
        The time when this managed object was created.  

        :return: The create_time of this ProcessorUnit.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ProcessorUnit.
        The time when this managed object was created.  

        :param create_time: The create_time of this ProcessorUnit.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ProcessorUnit.
        The time when this managed object was last modified.  

        :return: The mod_time of this ProcessorUnit.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ProcessorUnit.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ProcessorUnit.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ProcessorUnit.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this ProcessorUnit.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ProcessorUnit.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this ProcessorUnit.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ProcessorUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ProcessorUnit.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ProcessorUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ProcessorUnit.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ProcessorUnit.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this ProcessorUnit.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ProcessorUnit.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ProcessorUnit.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ProcessorUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ProcessorUnit.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ProcessorUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ProcessorUnit.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this ProcessorUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this ProcessorUnit.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ProcessorUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this ProcessorUnit.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this ProcessorUnit.
        The versioning info for this managed object   

        :return: The version_context of this ProcessorUnit.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this ProcessorUnit.
        The versioning info for this managed object   

        :param version_context: The version_context of this ProcessorUnit.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this ProcessorUnit.

        :return: The device_mo_id of this ProcessorUnit.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this ProcessorUnit.

        :param device_mo_id: The device_mo_id of this ProcessorUnit.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this ProcessorUnit.

        :return: The dn of this ProcessorUnit.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this ProcessorUnit.

        :param dn: The dn of this ProcessorUnit.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this ProcessorUnit.

        :return: The rn of this ProcessorUnit.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this ProcessorUnit.

        :param rn: The rn of this ProcessorUnit.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this ProcessorUnit.

        :return: The model of this ProcessorUnit.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ProcessorUnit.

        :param model: The model of this ProcessorUnit.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this ProcessorUnit.

        :return: The revision of this ProcessorUnit.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ProcessorUnit.

        :param revision: The revision of this ProcessorUnit.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this ProcessorUnit.

        :return: The serial of this ProcessorUnit.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this ProcessorUnit.

        :param serial: The serial of this ProcessorUnit.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this ProcessorUnit.

        :return: The vendor of this ProcessorUnit.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this ProcessorUnit.

        :param vendor: The vendor of this ProcessorUnit.
        :type: str
        """

        self._vendor = vendor

    @property
    def architecture(self):
        """
        Gets the architecture of this ProcessorUnit.

        :return: The architecture of this ProcessorUnit.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this ProcessorUnit.

        :param architecture: The architecture of this ProcessorUnit.
        :type: str
        """

        self._architecture = architecture

    @property
    def compute_board(self):
        """
        Gets the compute_board of this ProcessorUnit.

        :return: The compute_board of this ProcessorUnit.
        :rtype: ComputeBoardRef
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """
        Sets the compute_board of this ProcessorUnit.

        :param compute_board: The compute_board of this ProcessorUnit.
        :type: ComputeBoardRef
        """

        self._compute_board = compute_board

    @property
    def num_cores(self):
        """
        Gets the num_cores of this ProcessorUnit.

        :return: The num_cores of this ProcessorUnit.
        :rtype: int
        """
        return self._num_cores

    @num_cores.setter
    def num_cores(self, num_cores):
        """
        Sets the num_cores of this ProcessorUnit.

        :param num_cores: The num_cores of this ProcessorUnit.
        :type: int
        """

        self._num_cores = num_cores

    @property
    def num_cores_enabled(self):
        """
        Gets the num_cores_enabled of this ProcessorUnit.

        :return: The num_cores_enabled of this ProcessorUnit.
        :rtype: str
        """
        return self._num_cores_enabled

    @num_cores_enabled.setter
    def num_cores_enabled(self, num_cores_enabled):
        """
        Sets the num_cores_enabled of this ProcessorUnit.

        :param num_cores_enabled: The num_cores_enabled of this ProcessorUnit.
        :type: str
        """

        self._num_cores_enabled = num_cores_enabled

    @property
    def num_threads(self):
        """
        Gets the num_threads of this ProcessorUnit.

        :return: The num_threads of this ProcessorUnit.
        :rtype: str
        """
        return self._num_threads

    @num_threads.setter
    def num_threads(self, num_threads):
        """
        Sets the num_threads of this ProcessorUnit.

        :param num_threads: The num_threads of this ProcessorUnit.
        :type: str
        """

        self._num_threads = num_threads

    @property
    def oper_power_state(self):
        """
        Gets the oper_power_state of this ProcessorUnit.

        :return: The oper_power_state of this ProcessorUnit.
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """
        Sets the oper_power_state of this ProcessorUnit.

        :param oper_power_state: The oper_power_state of this ProcessorUnit.
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def oper_state(self):
        """
        Gets the oper_state of this ProcessorUnit.

        :return: The oper_state of this ProcessorUnit.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this ProcessorUnit.

        :param oper_state: The oper_state of this ProcessorUnit.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this ProcessorUnit.

        :return: The operability of this ProcessorUnit.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this ProcessorUnit.

        :param operability: The operability of this ProcessorUnit.
        :type: str
        """

        self._operability = operability

    @property
    def presence(self):
        """
        Gets the presence of this ProcessorUnit.

        :return: The presence of this ProcessorUnit.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this ProcessorUnit.

        :param presence: The presence of this ProcessorUnit.
        :type: str
        """

        self._presence = presence

    @property
    def processor_id(self):
        """
        Gets the processor_id of this ProcessorUnit.

        :return: The processor_id of this ProcessorUnit.
        :rtype: int
        """
        return self._processor_id

    @processor_id.setter
    def processor_id(self, processor_id):
        """
        Sets the processor_id of this ProcessorUnit.

        :param processor_id: The processor_id of this ProcessorUnit.
        :type: int
        """

        self._processor_id = processor_id

    @property
    def registered_device(self):
        """
        Gets the registered_device of this ProcessorUnit.

        :return: The registered_device of this ProcessorUnit.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this ProcessorUnit.

        :param registered_device: The registered_device of this ProcessorUnit.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def socket_designation(self):
        """
        Gets the socket_designation of this ProcessorUnit.

        :return: The socket_designation of this ProcessorUnit.
        :rtype: str
        """
        return self._socket_designation

    @socket_designation.setter
    def socket_designation(self, socket_designation):
        """
        Sets the socket_designation of this ProcessorUnit.

        :param socket_designation: The socket_designation of this ProcessorUnit.
        :type: str
        """

        self._socket_designation = socket_designation

    @property
    def speed(self):
        """
        Gets the speed of this ProcessorUnit.

        :return: The speed of this ProcessorUnit.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """
        Sets the speed of this ProcessorUnit.

        :param speed: The speed of this ProcessorUnit.
        :type: float
        """

        self._speed = speed

    @property
    def stepping(self):
        """
        Gets the stepping of this ProcessorUnit.

        :return: The stepping of this ProcessorUnit.
        :rtype: str
        """
        return self._stepping

    @stepping.setter
    def stepping(self, stepping):
        """
        Sets the stepping of this ProcessorUnit.

        :param stepping: The stepping of this ProcessorUnit.
        :type: str
        """

        self._stepping = stepping

    @property
    def thermal(self):
        """
        Gets the thermal of this ProcessorUnit.

        :return: The thermal of this ProcessorUnit.
        :rtype: str
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """
        Sets the thermal of this ProcessorUnit.

        :param thermal: The thermal of this ProcessorUnit.
        :type: str
        """

        self._thermal = thermal

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
        if not isinstance(other, ProcessorUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
