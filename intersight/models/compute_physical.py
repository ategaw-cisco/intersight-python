# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-265
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ComputePhysical(object):
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
        'admin_power_state': 'str',
        'asset_tag': 'str',
        'available_memory': 'int',
        'fault_summary': 'int',
        'kvm_ip_addresses': 'list[ComputeIpAddress]',
        'memory_speed': 'str',
        'num_adaptors': 'int',
        'num_cpu_cores': 'int',
        'num_cpu_cores_enabled': 'int',
        'num_cpus': 'int',
        'num_eth_host_interfaces': 'int',
        'num_fc_host_interfaces': 'int',
        'num_threads': 'int',
        'oper_power_state': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'platform_type': 'str',
        'presence': 'str',
        'service_profile': 'str',
        'total_memory': 'int',
        'user_label': 'str',
        'uuid': 'str'
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
        'admin_power_state': 'AdminPowerState',
        'asset_tag': 'AssetTag',
        'available_memory': 'AvailableMemory',
        'fault_summary': 'FaultSummary',
        'kvm_ip_addresses': 'KvmIpAddresses',
        'memory_speed': 'MemorySpeed',
        'num_adaptors': 'NumAdaptors',
        'num_cpu_cores': 'NumCpuCores',
        'num_cpu_cores_enabled': 'NumCpuCoresEnabled',
        'num_cpus': 'NumCpus',
        'num_eth_host_interfaces': 'NumEthHostInterfaces',
        'num_fc_host_interfaces': 'NumFcHostInterfaces',
        'num_threads': 'NumThreads',
        'oper_power_state': 'OperPowerState',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'platform_type': 'PlatformType',
        'presence': 'Presence',
        'service_profile': 'ServiceProfile',
        'total_memory': 'TotalMemory',
        'user_label': 'UserLabel',
        'uuid': 'Uuid'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, admin_power_state=None, asset_tag=None, available_memory=None, fault_summary=None, kvm_ip_addresses=None, memory_speed=None, num_adaptors=None, num_cpu_cores=None, num_cpu_cores_enabled=None, num_cpus=None, num_eth_host_interfaces=None, num_fc_host_interfaces=None, num_threads=None, oper_power_state=None, oper_state=None, operability=None, platform_type=None, presence=None, service_profile=None, total_memory=None, user_label=None, uuid=None):
        """
        ComputePhysical - a model defined in Swagger
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
        self._admin_power_state = None
        self._asset_tag = None
        self._available_memory = None
        self._fault_summary = None
        self._kvm_ip_addresses = None
        self._memory_speed = None
        self._num_adaptors = None
        self._num_cpu_cores = None
        self._num_cpu_cores_enabled = None
        self._num_cpus = None
        self._num_eth_host_interfaces = None
        self._num_fc_host_interfaces = None
        self._num_threads = None
        self._oper_power_state = None
        self._oper_state = None
        self._operability = None
        self._platform_type = None
        self._presence = None
        self._service_profile = None
        self._total_memory = None
        self._user_label = None
        self._uuid = None

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
        if admin_power_state is not None:
          self.admin_power_state = admin_power_state
        if asset_tag is not None:
          self.asset_tag = asset_tag
        if available_memory is not None:
          self.available_memory = available_memory
        if fault_summary is not None:
          self.fault_summary = fault_summary
        if kvm_ip_addresses is not None:
          self.kvm_ip_addresses = kvm_ip_addresses
        if memory_speed is not None:
          self.memory_speed = memory_speed
        if num_adaptors is not None:
          self.num_adaptors = num_adaptors
        if num_cpu_cores is not None:
          self.num_cpu_cores = num_cpu_cores
        if num_cpu_cores_enabled is not None:
          self.num_cpu_cores_enabled = num_cpu_cores_enabled
        if num_cpus is not None:
          self.num_cpus = num_cpus
        if num_eth_host_interfaces is not None:
          self.num_eth_host_interfaces = num_eth_host_interfaces
        if num_fc_host_interfaces is not None:
          self.num_fc_host_interfaces = num_fc_host_interfaces
        if num_threads is not None:
          self.num_threads = num_threads
        if oper_power_state is not None:
          self.oper_power_state = oper_power_state
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if platform_type is not None:
          self.platform_type = platform_type
        if presence is not None:
          self.presence = presence
        if service_profile is not None:
          self.service_profile = service_profile
        if total_memory is not None:
          self.total_memory = total_memory
        if user_label is not None:
          self.user_label = user_label
        if uuid is not None:
          self.uuid = uuid

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ComputePhysical.
        The Account ID for this managed object.  

        :return: The account_moid of this ComputePhysical.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ComputePhysical.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ComputePhysical.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ComputePhysical.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ComputePhysical.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ComputePhysical.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ComputePhysical.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ComputePhysical.
        The time when this managed object was created.  

        :return: The create_time of this ComputePhysical.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ComputePhysical.
        The time when this managed object was created.  

        :param create_time: The create_time of this ComputePhysical.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ComputePhysical.
        The time when this managed object was last modified.  

        :return: The mod_time of this ComputePhysical.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ComputePhysical.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ComputePhysical.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ComputePhysical.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this ComputePhysical.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ComputePhysical.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this ComputePhysical.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ComputePhysical.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ComputePhysical.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ComputePhysical.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ComputePhysical.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ComputePhysical.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this ComputePhysical.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ComputePhysical.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ComputePhysical.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ComputePhysical.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ComputePhysical.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ComputePhysical.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ComputePhysical.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this ComputePhysical.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this ComputePhysical.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ComputePhysical.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this ComputePhysical.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this ComputePhysical.
        The versioning info for this managed object   

        :return: The version_context of this ComputePhysical.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this ComputePhysical.
        The versioning info for this managed object   

        :param version_context: The version_context of this ComputePhysical.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this ComputePhysical.

        :return: The device_mo_id of this ComputePhysical.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this ComputePhysical.

        :param device_mo_id: The device_mo_id of this ComputePhysical.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this ComputePhysical.

        :return: The dn of this ComputePhysical.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this ComputePhysical.

        :param dn: The dn of this ComputePhysical.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this ComputePhysical.

        :return: The rn of this ComputePhysical.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this ComputePhysical.

        :param rn: The rn of this ComputePhysical.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this ComputePhysical.

        :return: The model of this ComputePhysical.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ComputePhysical.

        :param model: The model of this ComputePhysical.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this ComputePhysical.

        :return: The revision of this ComputePhysical.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ComputePhysical.

        :param revision: The revision of this ComputePhysical.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this ComputePhysical.

        :return: The serial of this ComputePhysical.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this ComputePhysical.

        :param serial: The serial of this ComputePhysical.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this ComputePhysical.

        :return: The vendor of this ComputePhysical.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this ComputePhysical.

        :param vendor: The vendor of this ComputePhysical.
        :type: str
        """

        self._vendor = vendor

    @property
    def admin_power_state(self):
        """
        Gets the admin_power_state of this ComputePhysical.

        :return: The admin_power_state of this ComputePhysical.
        :rtype: str
        """
        return self._admin_power_state

    @admin_power_state.setter
    def admin_power_state(self, admin_power_state):
        """
        Sets the admin_power_state of this ComputePhysical.

        :param admin_power_state: The admin_power_state of this ComputePhysical.
        :type: str
        """

        self._admin_power_state = admin_power_state

    @property
    def asset_tag(self):
        """
        Gets the asset_tag of this ComputePhysical.

        :return: The asset_tag of this ComputePhysical.
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """
        Sets the asset_tag of this ComputePhysical.

        :param asset_tag: The asset_tag of this ComputePhysical.
        :type: str
        """

        self._asset_tag = asset_tag

    @property
    def available_memory(self):
        """
        Gets the available_memory of this ComputePhysical.

        :return: The available_memory of this ComputePhysical.
        :rtype: int
        """
        return self._available_memory

    @available_memory.setter
    def available_memory(self, available_memory):
        """
        Sets the available_memory of this ComputePhysical.

        :param available_memory: The available_memory of this ComputePhysical.
        :type: int
        """

        self._available_memory = available_memory

    @property
    def fault_summary(self):
        """
        Gets the fault_summary of this ComputePhysical.

        :return: The fault_summary of this ComputePhysical.
        :rtype: int
        """
        return self._fault_summary

    @fault_summary.setter
    def fault_summary(self, fault_summary):
        """
        Sets the fault_summary of this ComputePhysical.

        :param fault_summary: The fault_summary of this ComputePhysical.
        :type: int
        """

        self._fault_summary = fault_summary

    @property
    def kvm_ip_addresses(self):
        """
        Gets the kvm_ip_addresses of this ComputePhysical.

        :return: The kvm_ip_addresses of this ComputePhysical.
        :rtype: list[ComputeIpAddress]
        """
        return self._kvm_ip_addresses

    @kvm_ip_addresses.setter
    def kvm_ip_addresses(self, kvm_ip_addresses):
        """
        Sets the kvm_ip_addresses of this ComputePhysical.

        :param kvm_ip_addresses: The kvm_ip_addresses of this ComputePhysical.
        :type: list[ComputeIpAddress]
        """

        self._kvm_ip_addresses = kvm_ip_addresses

    @property
    def memory_speed(self):
        """
        Gets the memory_speed of this ComputePhysical.

        :return: The memory_speed of this ComputePhysical.
        :rtype: str
        """
        return self._memory_speed

    @memory_speed.setter
    def memory_speed(self, memory_speed):
        """
        Sets the memory_speed of this ComputePhysical.

        :param memory_speed: The memory_speed of this ComputePhysical.
        :type: str
        """

        self._memory_speed = memory_speed

    @property
    def num_adaptors(self):
        """
        Gets the num_adaptors of this ComputePhysical.

        :return: The num_adaptors of this ComputePhysical.
        :rtype: int
        """
        return self._num_adaptors

    @num_adaptors.setter
    def num_adaptors(self, num_adaptors):
        """
        Sets the num_adaptors of this ComputePhysical.

        :param num_adaptors: The num_adaptors of this ComputePhysical.
        :type: int
        """

        self._num_adaptors = num_adaptors

    @property
    def num_cpu_cores(self):
        """
        Gets the num_cpu_cores of this ComputePhysical.

        :return: The num_cpu_cores of this ComputePhysical.
        :rtype: int
        """
        return self._num_cpu_cores

    @num_cpu_cores.setter
    def num_cpu_cores(self, num_cpu_cores):
        """
        Sets the num_cpu_cores of this ComputePhysical.

        :param num_cpu_cores: The num_cpu_cores of this ComputePhysical.
        :type: int
        """

        self._num_cpu_cores = num_cpu_cores

    @property
    def num_cpu_cores_enabled(self):
        """
        Gets the num_cpu_cores_enabled of this ComputePhysical.

        :return: The num_cpu_cores_enabled of this ComputePhysical.
        :rtype: int
        """
        return self._num_cpu_cores_enabled

    @num_cpu_cores_enabled.setter
    def num_cpu_cores_enabled(self, num_cpu_cores_enabled):
        """
        Sets the num_cpu_cores_enabled of this ComputePhysical.

        :param num_cpu_cores_enabled: The num_cpu_cores_enabled of this ComputePhysical.
        :type: int
        """

        self._num_cpu_cores_enabled = num_cpu_cores_enabled

    @property
    def num_cpus(self):
        """
        Gets the num_cpus of this ComputePhysical.

        :return: The num_cpus of this ComputePhysical.
        :rtype: int
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        """
        Sets the num_cpus of this ComputePhysical.

        :param num_cpus: The num_cpus of this ComputePhysical.
        :type: int
        """

        self._num_cpus = num_cpus

    @property
    def num_eth_host_interfaces(self):
        """
        Gets the num_eth_host_interfaces of this ComputePhysical.

        :return: The num_eth_host_interfaces of this ComputePhysical.
        :rtype: int
        """
        return self._num_eth_host_interfaces

    @num_eth_host_interfaces.setter
    def num_eth_host_interfaces(self, num_eth_host_interfaces):
        """
        Sets the num_eth_host_interfaces of this ComputePhysical.

        :param num_eth_host_interfaces: The num_eth_host_interfaces of this ComputePhysical.
        :type: int
        """

        self._num_eth_host_interfaces = num_eth_host_interfaces

    @property
    def num_fc_host_interfaces(self):
        """
        Gets the num_fc_host_interfaces of this ComputePhysical.

        :return: The num_fc_host_interfaces of this ComputePhysical.
        :rtype: int
        """
        return self._num_fc_host_interfaces

    @num_fc_host_interfaces.setter
    def num_fc_host_interfaces(self, num_fc_host_interfaces):
        """
        Sets the num_fc_host_interfaces of this ComputePhysical.

        :param num_fc_host_interfaces: The num_fc_host_interfaces of this ComputePhysical.
        :type: int
        """

        self._num_fc_host_interfaces = num_fc_host_interfaces

    @property
    def num_threads(self):
        """
        Gets the num_threads of this ComputePhysical.

        :return: The num_threads of this ComputePhysical.
        :rtype: int
        """
        return self._num_threads

    @num_threads.setter
    def num_threads(self, num_threads):
        """
        Sets the num_threads of this ComputePhysical.

        :param num_threads: The num_threads of this ComputePhysical.
        :type: int
        """

        self._num_threads = num_threads

    @property
    def oper_power_state(self):
        """
        Gets the oper_power_state of this ComputePhysical.

        :return: The oper_power_state of this ComputePhysical.
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """
        Sets the oper_power_state of this ComputePhysical.

        :param oper_power_state: The oper_power_state of this ComputePhysical.
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def oper_state(self):
        """
        Gets the oper_state of this ComputePhysical.

        :return: The oper_state of this ComputePhysical.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this ComputePhysical.

        :param oper_state: The oper_state of this ComputePhysical.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this ComputePhysical.

        :return: The operability of this ComputePhysical.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this ComputePhysical.

        :param operability: The operability of this ComputePhysical.
        :type: str
        """

        self._operability = operability

    @property
    def platform_type(self):
        """
        Gets the platform_type of this ComputePhysical.

        :return: The platform_type of this ComputePhysical.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this ComputePhysical.

        :param platform_type: The platform_type of this ComputePhysical.
        :type: str
        """

        self._platform_type = platform_type

    @property
    def presence(self):
        """
        Gets the presence of this ComputePhysical.

        :return: The presence of this ComputePhysical.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this ComputePhysical.

        :param presence: The presence of this ComputePhysical.
        :type: str
        """

        self._presence = presence

    @property
    def service_profile(self):
        """
        Gets the service_profile of this ComputePhysical.

        :return: The service_profile of this ComputePhysical.
        :rtype: str
        """
        return self._service_profile

    @service_profile.setter
    def service_profile(self, service_profile):
        """
        Sets the service_profile of this ComputePhysical.

        :param service_profile: The service_profile of this ComputePhysical.
        :type: str
        """

        self._service_profile = service_profile

    @property
    def total_memory(self):
        """
        Gets the total_memory of this ComputePhysical.

        :return: The total_memory of this ComputePhysical.
        :rtype: int
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """
        Sets the total_memory of this ComputePhysical.

        :param total_memory: The total_memory of this ComputePhysical.
        :type: int
        """

        self._total_memory = total_memory

    @property
    def user_label(self):
        """
        Gets the user_label of this ComputePhysical.

        :return: The user_label of this ComputePhysical.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """
        Sets the user_label of this ComputePhysical.

        :param user_label: The user_label of this ComputePhysical.
        :type: str
        """

        self._user_label = user_label

    @property
    def uuid(self):
        """
        Gets the uuid of this ComputePhysical.

        :return: The uuid of this ComputePhysical.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this ComputePhysical.

        :param uuid: The uuid of this ComputePhysical.
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, ComputePhysical):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
