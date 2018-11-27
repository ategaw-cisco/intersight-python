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


class HyperflexClusterProfile(object):
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
        'description': 'str',
        'name': 'str',
        'src_template': 'PolicyAbstractProfileRef',
        'type': 'str',
        'action': 'str',
        'config_context': 'PolicyConfigContext',
        'auto_support': 'HyperflexAutoSupportPolicyRef',
        'cluster_network': 'HyperflexClusterNetworkPolicyRef',
        'cluster_storage': 'HyperflexClusterStoragePolicyRef',
        'config_result': 'HyperflexConfigResultRef',
        'data_ip_address': 'str',
        'ext_fc_storage': 'HyperflexExtFcStoragePolicyRef',
        'ext_iscsi_storage': 'HyperflexExtIscsiStoragePolicyRef',
        'hxdp_version': 'str',
        'hypervisor_type': 'str',
        'local_credential': 'HyperflexLocalCredentialPolicyRef',
        'mac_address_prefix': 'str',
        'mgmt_ip_address': 'str',
        'mgmt_platform': 'str',
        'node_config': 'HyperflexNodeConfigPolicyRef',
        'node_profile_config': 'list[HyperflexNodeProfileRef]',
        'organization': 'IamAccountRef',
        'proxy_setting': 'HyperflexProxySettingPolicyRef',
        'replication': 'int',
        'storage_data_vlan': 'HyperflexNamedVlan',
        'sys_config': 'HyperflexSysConfigPolicyRef',
        'ucsm_config': 'HyperflexUcsmConfigPolicyRef',
        'vcenter_config': 'HyperflexVcenterConfigPolicyRef',
        'wwxn_prefix': 'str'
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
        'description': 'Description',
        'name': 'Name',
        'src_template': 'SrcTemplate',
        'type': 'Type',
        'action': 'Action',
        'config_context': 'ConfigContext',
        'auto_support': 'AutoSupport',
        'cluster_network': 'ClusterNetwork',
        'cluster_storage': 'ClusterStorage',
        'config_result': 'ConfigResult',
        'data_ip_address': 'DataIpAddress',
        'ext_fc_storage': 'ExtFcStorage',
        'ext_iscsi_storage': 'ExtIscsiStorage',
        'hxdp_version': 'HxdpVersion',
        'hypervisor_type': 'HypervisorType',
        'local_credential': 'LocalCredential',
        'mac_address_prefix': 'MacAddressPrefix',
        'mgmt_ip_address': 'MgmtIpAddress',
        'mgmt_platform': 'MgmtPlatform',
        'node_config': 'NodeConfig',
        'node_profile_config': 'NodeProfileConfig',
        'organization': 'Organization',
        'proxy_setting': 'ProxySetting',
        'replication': 'Replication',
        'storage_data_vlan': 'StorageDataVlan',
        'sys_config': 'SysConfig',
        'ucsm_config': 'UcsmConfig',
        'vcenter_config': 'VcenterConfig',
        'wwxn_prefix': 'WwxnPrefix'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, src_template=None, type='instance', action=None, config_context=None, auto_support=None, cluster_network=None, cluster_storage=None, config_result=None, data_ip_address=None, ext_fc_storage=None, ext_iscsi_storage=None, hxdp_version=None, hypervisor_type='ESXi', local_credential=None, mac_address_prefix=None, mgmt_ip_address=None, mgmt_platform='FI', node_config=None, node_profile_config=None, organization=None, proxy_setting=None, replication=None, storage_data_vlan=None, sys_config=None, ucsm_config=None, vcenter_config=None, wwxn_prefix=None):
        """
        HyperflexClusterProfile - a model defined in Swagger
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
        self._description = None
        self._name = None
        self._src_template = None
        self._type = None
        self._action = None
        self._config_context = None
        self._auto_support = None
        self._cluster_network = None
        self._cluster_storage = None
        self._config_result = None
        self._data_ip_address = None
        self._ext_fc_storage = None
        self._ext_iscsi_storage = None
        self._hxdp_version = None
        self._hypervisor_type = None
        self._local_credential = None
        self._mac_address_prefix = None
        self._mgmt_ip_address = None
        self._mgmt_platform = None
        self._node_config = None
        self._node_profile_config = None
        self._organization = None
        self._proxy_setting = None
        self._replication = None
        self._storage_data_vlan = None
        self._sys_config = None
        self._ucsm_config = None
        self._vcenter_config = None
        self._wwxn_prefix = None

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
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if src_template is not None:
          self.src_template = src_template
        if type is not None:
          self.type = type
        if action is not None:
          self.action = action
        if config_context is not None:
          self.config_context = config_context
        if auto_support is not None:
          self.auto_support = auto_support
        if cluster_network is not None:
          self.cluster_network = cluster_network
        if cluster_storage is not None:
          self.cluster_storage = cluster_storage
        if config_result is not None:
          self.config_result = config_result
        if data_ip_address is not None:
          self.data_ip_address = data_ip_address
        if ext_fc_storage is not None:
          self.ext_fc_storage = ext_fc_storage
        if ext_iscsi_storage is not None:
          self.ext_iscsi_storage = ext_iscsi_storage
        if hxdp_version is not None:
          self.hxdp_version = hxdp_version
        if hypervisor_type is not None:
          self.hypervisor_type = hypervisor_type
        if local_credential is not None:
          self.local_credential = local_credential
        if mac_address_prefix is not None:
          self.mac_address_prefix = mac_address_prefix
        if mgmt_ip_address is not None:
          self.mgmt_ip_address = mgmt_ip_address
        if mgmt_platform is not None:
          self.mgmt_platform = mgmt_platform
        if node_config is not None:
          self.node_config = node_config
        if node_profile_config is not None:
          self.node_profile_config = node_profile_config
        if organization is not None:
          self.organization = organization
        if proxy_setting is not None:
          self.proxy_setting = proxy_setting
        if replication is not None:
          self.replication = replication
        if storage_data_vlan is not None:
          self.storage_data_vlan = storage_data_vlan
        if sys_config is not None:
          self.sys_config = sys_config
        if ucsm_config is not None:
          self.ucsm_config = ucsm_config
        if vcenter_config is not None:
          self.vcenter_config = vcenter_config
        if wwxn_prefix is not None:
          self.wwxn_prefix = wwxn_prefix

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexClusterProfile.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexClusterProfile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexClusterProfile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexClusterProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexClusterProfile.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexClusterProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexClusterProfile.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexClusterProfile.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexClusterProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexClusterProfile.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexClusterProfile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexClusterProfile.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexClusterProfile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexClusterProfile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexClusterProfile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexClusterProfile.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexClusterProfile.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexClusterProfile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexClusterProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexClusterProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexClusterProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexClusterProfile.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexClusterProfile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexClusterProfile.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexClusterProfile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexClusterProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexClusterProfile.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexClusterProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexClusterProfile.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexClusterProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexClusterProfile.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexClusterProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexClusterProfile.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexClusterProfile.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexClusterProfile.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexClusterProfile.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexClusterProfile.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this HyperflexClusterProfile.
        Description of the profile.  

        :return: The description of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexClusterProfile.
        Description of the profile.  

        :param description: The description of this HyperflexClusterProfile.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexClusterProfile.
        Name of the profile.  

        :return: The name of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexClusterProfile.
        Name of the profile.  

        :param name: The name of this HyperflexClusterProfile.
        :type: str
        """

        self._name = name

    @property
    def src_template(self):
        """
        Gets the src_template of this HyperflexClusterProfile.

        :return: The src_template of this HyperflexClusterProfile.
        :rtype: PolicyAbstractProfileRef
        """
        return self._src_template

    @src_template.setter
    def src_template(self, src_template):
        """
        Sets the src_template of this HyperflexClusterProfile.

        :param src_template: The src_template of this HyperflexClusterProfile.
        :type: PolicyAbstractProfileRef
        """

        self._src_template = src_template

    @property
    def type(self):
        """
        Gets the type of this HyperflexClusterProfile.
        Defines the type of the profile. Accepted value is instance.   

        :return: The type of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this HyperflexClusterProfile.
        Defines the type of the profile. Accepted value is instance.   

        :param type: The type of this HyperflexClusterProfile.
        :type: str
        """
        allowed_values = ["instance"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def action(self):
        """
        Gets the action of this HyperflexClusterProfile.
        User initiated action. Each profile type has its own supported actions. For hyperflex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign  

        :return: The action of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this HyperflexClusterProfile.
        User initiated action. Each profile type has its own supported actions. For hyperflex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign  

        :param action: The action of this HyperflexClusterProfile.
        :type: str
        """

        self._action = action

    @property
    def config_context(self):
        """
        Gets the config_context of this HyperflexClusterProfile.

        :return: The config_context of this HyperflexClusterProfile.
        :rtype: PolicyConfigContext
        """
        return self._config_context

    @config_context.setter
    def config_context(self, config_context):
        """
        Sets the config_context of this HyperflexClusterProfile.

        :param config_context: The config_context of this HyperflexClusterProfile.
        :type: PolicyConfigContext
        """

        self._config_context = config_context

    @property
    def auto_support(self):
        """
        Gets the auto_support of this HyperflexClusterProfile.

        :return: The auto_support of this HyperflexClusterProfile.
        :rtype: HyperflexAutoSupportPolicyRef
        """
        return self._auto_support

    @auto_support.setter
    def auto_support(self, auto_support):
        """
        Sets the auto_support of this HyperflexClusterProfile.

        :param auto_support: The auto_support of this HyperflexClusterProfile.
        :type: HyperflexAutoSupportPolicyRef
        """

        self._auto_support = auto_support

    @property
    def cluster_network(self):
        """
        Gets the cluster_network of this HyperflexClusterProfile.

        :return: The cluster_network of this HyperflexClusterProfile.
        :rtype: HyperflexClusterNetworkPolicyRef
        """
        return self._cluster_network

    @cluster_network.setter
    def cluster_network(self, cluster_network):
        """
        Sets the cluster_network of this HyperflexClusterProfile.

        :param cluster_network: The cluster_network of this HyperflexClusterProfile.
        :type: HyperflexClusterNetworkPolicyRef
        """

        self._cluster_network = cluster_network

    @property
    def cluster_storage(self):
        """
        Gets the cluster_storage of this HyperflexClusterProfile.

        :return: The cluster_storage of this HyperflexClusterProfile.
        :rtype: HyperflexClusterStoragePolicyRef
        """
        return self._cluster_storage

    @cluster_storage.setter
    def cluster_storage(self, cluster_storage):
        """
        Sets the cluster_storage of this HyperflexClusterProfile.

        :param cluster_storage: The cluster_storage of this HyperflexClusterProfile.
        :type: HyperflexClusterStoragePolicyRef
        """

        self._cluster_storage = cluster_storage

    @property
    def config_result(self):
        """
        Gets the config_result of this HyperflexClusterProfile.
        The profile configuration (deploy, validation) results with the overall state and detailed result messages. 

        :return: The config_result of this HyperflexClusterProfile.
        :rtype: HyperflexConfigResultRef
        """
        return self._config_result

    @config_result.setter
    def config_result(self, config_result):
        """
        Sets the config_result of this HyperflexClusterProfile.
        The profile configuration (deploy, validation) results with the overall state and detailed result messages. 

        :param config_result: The config_result of this HyperflexClusterProfile.
        :type: HyperflexConfigResultRef
        """

        self._config_result = config_result

    @property
    def data_ip_address(self):
        """
        Gets the data_ip_address of this HyperflexClusterProfile.
        Storage data IP address for the HyperFlex cluster  

        :return: The data_ip_address of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._data_ip_address

    @data_ip_address.setter
    def data_ip_address(self, data_ip_address):
        """
        Sets the data_ip_address of this HyperflexClusterProfile.
        Storage data IP address for the HyperFlex cluster  

        :param data_ip_address: The data_ip_address of this HyperflexClusterProfile.
        :type: str
        """

        self._data_ip_address = data_ip_address

    @property
    def ext_fc_storage(self):
        """
        Gets the ext_fc_storage of this HyperflexClusterProfile.

        :return: The ext_fc_storage of this HyperflexClusterProfile.
        :rtype: HyperflexExtFcStoragePolicyRef
        """
        return self._ext_fc_storage

    @ext_fc_storage.setter
    def ext_fc_storage(self, ext_fc_storage):
        """
        Sets the ext_fc_storage of this HyperflexClusterProfile.

        :param ext_fc_storage: The ext_fc_storage of this HyperflexClusterProfile.
        :type: HyperflexExtFcStoragePolicyRef
        """

        self._ext_fc_storage = ext_fc_storage

    @property
    def ext_iscsi_storage(self):
        """
        Gets the ext_iscsi_storage of this HyperflexClusterProfile.

        :return: The ext_iscsi_storage of this HyperflexClusterProfile.
        :rtype: HyperflexExtIscsiStoragePolicyRef
        """
        return self._ext_iscsi_storage

    @ext_iscsi_storage.setter
    def ext_iscsi_storage(self, ext_iscsi_storage):
        """
        Sets the ext_iscsi_storage of this HyperflexClusterProfile.

        :param ext_iscsi_storage: The ext_iscsi_storage of this HyperflexClusterProfile.
        :type: HyperflexExtIscsiStoragePolicyRef
        """

        self._ext_iscsi_storage = ext_iscsi_storage

    @property
    def hxdp_version(self):
        """
        Gets the hxdp_version of this HyperflexClusterProfile.
        Specifies the HyperFlex Data Platform version to be installed  

        :return: The hxdp_version of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._hxdp_version

    @hxdp_version.setter
    def hxdp_version(self, hxdp_version):
        """
        Sets the hxdp_version of this HyperflexClusterProfile.
        Specifies the HyperFlex Data Platform version to be installed  

        :param hxdp_version: The hxdp_version of this HyperflexClusterProfile.
        :type: str
        """

        self._hxdp_version = hxdp_version

    @property
    def hypervisor_type(self):
        """
        Gets the hypervisor_type of this HyperflexClusterProfile.
        Hypervisor type for the HyperFlex cluster  

        :return: The hypervisor_type of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._hypervisor_type

    @hypervisor_type.setter
    def hypervisor_type(self, hypervisor_type):
        """
        Sets the hypervisor_type of this HyperflexClusterProfile.
        Hypervisor type for the HyperFlex cluster  

        :param hypervisor_type: The hypervisor_type of this HyperflexClusterProfile.
        :type: str
        """
        allowed_values = ["ESXi"]
        if hypervisor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `hypervisor_type` ({0}), must be one of {1}"
                .format(hypervisor_type, allowed_values)
            )

        self._hypervisor_type = hypervisor_type

    @property
    def local_credential(self):
        """
        Gets the local_credential of this HyperflexClusterProfile.

        :return: The local_credential of this HyperflexClusterProfile.
        :rtype: HyperflexLocalCredentialPolicyRef
        """
        return self._local_credential

    @local_credential.setter
    def local_credential(self, local_credential):
        """
        Sets the local_credential of this HyperflexClusterProfile.

        :param local_credential: The local_credential of this HyperflexClusterProfile.
        :type: HyperflexLocalCredentialPolicyRef
        """

        self._local_credential = local_credential

    @property
    def mac_address_prefix(self):
        """
        Gets the mac_address_prefix of this HyperflexClusterProfile.
        MAC address prefix 00:25:B5:XX  

        :return: The mac_address_prefix of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._mac_address_prefix

    @mac_address_prefix.setter
    def mac_address_prefix(self, mac_address_prefix):
        """
        Sets the mac_address_prefix of this HyperflexClusterProfile.
        MAC address prefix 00:25:B5:XX  

        :param mac_address_prefix: The mac_address_prefix of this HyperflexClusterProfile.
        :type: str
        """

        self._mac_address_prefix = mac_address_prefix

    @property
    def mgmt_ip_address(self):
        """
        Gets the mgmt_ip_address of this HyperflexClusterProfile.
        Management IP address for the HyperFlex cluster  

        :return: The mgmt_ip_address of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._mgmt_ip_address

    @mgmt_ip_address.setter
    def mgmt_ip_address(self, mgmt_ip_address):
        """
        Sets the mgmt_ip_address of this HyperflexClusterProfile.
        Management IP address for the HyperFlex cluster  

        :param mgmt_ip_address: The mgmt_ip_address of this HyperflexClusterProfile.
        :type: str
        """

        self._mgmt_ip_address = mgmt_ip_address

    @property
    def mgmt_platform(self):
        """
        Gets the mgmt_platform of this HyperflexClusterProfile.
        Management platform for the HyperFlex cluster  

        :return: The mgmt_platform of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._mgmt_platform

    @mgmt_platform.setter
    def mgmt_platform(self, mgmt_platform):
        """
        Sets the mgmt_platform of this HyperflexClusterProfile.
        Management platform for the HyperFlex cluster  

        :param mgmt_platform: The mgmt_platform of this HyperflexClusterProfile.
        :type: str
        """
        allowed_values = ["FI", "EDGE"]
        if mgmt_platform not in allowed_values:
            raise ValueError(
                "Invalid value for `mgmt_platform` ({0}), must be one of {1}"
                .format(mgmt_platform, allowed_values)
            )

        self._mgmt_platform = mgmt_platform

    @property
    def node_config(self):
        """
        Gets the node_config of this HyperflexClusterProfile.

        :return: The node_config of this HyperflexClusterProfile.
        :rtype: HyperflexNodeConfigPolicyRef
        """
        return self._node_config

    @node_config.setter
    def node_config(self, node_config):
        """
        Sets the node_config of this HyperflexClusterProfile.

        :param node_config: The node_config of this HyperflexClusterProfile.
        :type: HyperflexNodeConfigPolicyRef
        """

        self._node_config = node_config

    @property
    def node_profile_config(self):
        """
        Gets the node_profile_config of this HyperflexClusterProfile.
        List of node profiles representing the configuraion of the corresponding HX cluster nodes 

        :return: The node_profile_config of this HyperflexClusterProfile.
        :rtype: list[HyperflexNodeProfileRef]
        """
        return self._node_profile_config

    @node_profile_config.setter
    def node_profile_config(self, node_profile_config):
        """
        Sets the node_profile_config of this HyperflexClusterProfile.
        List of node profiles representing the configuraion of the corresponding HX cluster nodes 

        :param node_profile_config: The node_profile_config of this HyperflexClusterProfile.
        :type: list[HyperflexNodeProfileRef]
        """

        self._node_profile_config = node_profile_config

    @property
    def organization(self):
        """
        Gets the organization of this HyperflexClusterProfile.
        Organization 

        :return: The organization of this HyperflexClusterProfile.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this HyperflexClusterProfile.
        Organization 

        :param organization: The organization of this HyperflexClusterProfile.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def proxy_setting(self):
        """
        Gets the proxy_setting of this HyperflexClusterProfile.

        :return: The proxy_setting of this HyperflexClusterProfile.
        :rtype: HyperflexProxySettingPolicyRef
        """
        return self._proxy_setting

    @proxy_setting.setter
    def proxy_setting(self, proxy_setting):
        """
        Sets the proxy_setting of this HyperflexClusterProfile.

        :param proxy_setting: The proxy_setting of this HyperflexClusterProfile.
        :type: HyperflexProxySettingPolicyRef
        """

        self._proxy_setting = proxy_setting

    @property
    def replication(self):
        """
        Gets the replication of this HyperflexClusterProfile.
        Specifies the number of copies of each data block written  

        :return: The replication of this HyperflexClusterProfile.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """
        Sets the replication of this HyperflexClusterProfile.
        Specifies the number of copies of each data block written  

        :param replication: The replication of this HyperflexClusterProfile.
        :type: int
        """

        self._replication = replication

    @property
    def storage_data_vlan(self):
        """
        Gets the storage_data_vlan of this HyperflexClusterProfile.
        VLAN for the HyperFlex storage data traffic  

        :return: The storage_data_vlan of this HyperflexClusterProfile.
        :rtype: HyperflexNamedVlan
        """
        return self._storage_data_vlan

    @storage_data_vlan.setter
    def storage_data_vlan(self, storage_data_vlan):
        """
        Sets the storage_data_vlan of this HyperflexClusterProfile.
        VLAN for the HyperFlex storage data traffic  

        :param storage_data_vlan: The storage_data_vlan of this HyperflexClusterProfile.
        :type: HyperflexNamedVlan
        """

        self._storage_data_vlan = storage_data_vlan

    @property
    def sys_config(self):
        """
        Gets the sys_config of this HyperflexClusterProfile.

        :return: The sys_config of this HyperflexClusterProfile.
        :rtype: HyperflexSysConfigPolicyRef
        """
        return self._sys_config

    @sys_config.setter
    def sys_config(self, sys_config):
        """
        Sets the sys_config of this HyperflexClusterProfile.

        :param sys_config: The sys_config of this HyperflexClusterProfile.
        :type: HyperflexSysConfigPolicyRef
        """

        self._sys_config = sys_config

    @property
    def ucsm_config(self):
        """
        Gets the ucsm_config of this HyperflexClusterProfile.

        :return: The ucsm_config of this HyperflexClusterProfile.
        :rtype: HyperflexUcsmConfigPolicyRef
        """
        return self._ucsm_config

    @ucsm_config.setter
    def ucsm_config(self, ucsm_config):
        """
        Sets the ucsm_config of this HyperflexClusterProfile.

        :param ucsm_config: The ucsm_config of this HyperflexClusterProfile.
        :type: HyperflexUcsmConfigPolicyRef
        """

        self._ucsm_config = ucsm_config

    @property
    def vcenter_config(self):
        """
        Gets the vcenter_config of this HyperflexClusterProfile.

        :return: The vcenter_config of this HyperflexClusterProfile.
        :rtype: HyperflexVcenterConfigPolicyRef
        """
        return self._vcenter_config

    @vcenter_config.setter
    def vcenter_config(self, vcenter_config):
        """
        Sets the vcenter_config of this HyperflexClusterProfile.

        :param vcenter_config: The vcenter_config of this HyperflexClusterProfile.
        :type: HyperflexVcenterConfigPolicyRef
        """

        self._vcenter_config = vcenter_config

    @property
    def wwxn_prefix(self):
        """
        Gets the wwxn_prefix of this HyperflexClusterProfile.
        WWxN prefix 20:00:00:25:B5:XX   

        :return: The wwxn_prefix of this HyperflexClusterProfile.
        :rtype: str
        """
        return self._wwxn_prefix

    @wwxn_prefix.setter
    def wwxn_prefix(self, wwxn_prefix):
        """
        Sets the wwxn_prefix of this HyperflexClusterProfile.
        WWxN prefix 20:00:00:25:B5:XX   

        :param wwxn_prefix: The wwxn_prefix of this HyperflexClusterProfile.
        :type: str
        """

        self._wwxn_prefix = wwxn_prefix

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
        if not isinstance(other, HyperflexClusterProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
