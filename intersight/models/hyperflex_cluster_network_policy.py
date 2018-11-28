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


class HyperflexClusterNetworkPolicy(object):
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
        'cluster_profiles': 'list[HyperflexClusterProfileRef]',
        'jumbo_frame': 'bool',
        'mgmt_vlan': 'HyperflexNamedVlan',
        'organization': 'IamAccountRef',
        'vm_migration_vlan': 'HyperflexNamedVlan',
        'vm_network_vlans': 'list[HyperflexNamedVlan]'
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
        'cluster_profiles': 'ClusterProfiles',
        'jumbo_frame': 'JumboFrame',
        'mgmt_vlan': 'MgmtVlan',
        'organization': 'Organization',
        'vm_migration_vlan': 'VmMigrationVlan',
        'vm_network_vlans': 'VmNetworkVlans'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, cluster_profiles=None, jumbo_frame=None, mgmt_vlan=None, organization=None, vm_migration_vlan=None, vm_network_vlans=None):
        """
        HyperflexClusterNetworkPolicy - a model defined in Swagger
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
        self._cluster_profiles = None
        self._jumbo_frame = None
        self._mgmt_vlan = None
        self._organization = None
        self._vm_migration_vlan = None
        self._vm_network_vlans = None

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
        if cluster_profiles is not None:
          self.cluster_profiles = cluster_profiles
        if jumbo_frame is not None:
          self.jumbo_frame = jumbo_frame
        if mgmt_vlan is not None:
          self.mgmt_vlan = mgmt_vlan
        if organization is not None:
          self.organization = organization
        if vm_migration_vlan is not None:
          self.vm_migration_vlan = vm_migration_vlan
        if vm_network_vlans is not None:
          self.vm_network_vlans = vm_network_vlans

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexClusterNetworkPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexClusterNetworkPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexClusterNetworkPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexClusterNetworkPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexClusterNetworkPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexClusterNetworkPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexClusterNetworkPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexClusterNetworkPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexClusterNetworkPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexClusterNetworkPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexClusterNetworkPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexClusterNetworkPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexClusterNetworkPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexClusterNetworkPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexClusterNetworkPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexClusterNetworkPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexClusterNetworkPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexClusterNetworkPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexClusterNetworkPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexClusterNetworkPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexClusterNetworkPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexClusterNetworkPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexClusterNetworkPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexClusterNetworkPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexClusterNetworkPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexClusterNetworkPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexClusterNetworkPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexClusterNetworkPolicy.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexClusterNetworkPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexClusterNetworkPolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexClusterNetworkPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this HyperflexClusterNetworkPolicy.
        Description of the policy.  

        :return: The description of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexClusterNetworkPolicy.
        Description of the policy.  

        :param description: The description of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexClusterNetworkPolicy.
        Name of the policy.   

        :return: The name of this HyperflexClusterNetworkPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexClusterNetworkPolicy.
        Name of the policy.   

        :param name: The name of this HyperflexClusterNetworkPolicy.
        :type: str
        """

        self._name = name

    @property
    def cluster_profiles(self):
        """
        Gets the cluster_profiles of this HyperflexClusterNetworkPolicy.
        List of cluster profiles using this policy 

        :return: The cluster_profiles of this HyperflexClusterNetworkPolicy.
        :rtype: list[HyperflexClusterProfileRef]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """
        Sets the cluster_profiles of this HyperflexClusterNetworkPolicy.
        List of cluster profiles using this policy 

        :param cluster_profiles: The cluster_profiles of this HyperflexClusterNetworkPolicy.
        :type: list[HyperflexClusterProfileRef]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def jumbo_frame(self):
        """
        Gets the jumbo_frame of this HyperflexClusterNetworkPolicy.
        Enable or disable Jumbo frames  

        :return: The jumbo_frame of this HyperflexClusterNetworkPolicy.
        :rtype: bool
        """
        return self._jumbo_frame

    @jumbo_frame.setter
    def jumbo_frame(self, jumbo_frame):
        """
        Sets the jumbo_frame of this HyperflexClusterNetworkPolicy.
        Enable or disable Jumbo frames  

        :param jumbo_frame: The jumbo_frame of this HyperflexClusterNetworkPolicy.
        :type: bool
        """

        self._jumbo_frame = jumbo_frame

    @property
    def mgmt_vlan(self):
        """
        Gets the mgmt_vlan of this HyperflexClusterNetworkPolicy.
        Management VLAN  

        :return: The mgmt_vlan of this HyperflexClusterNetworkPolicy.
        :rtype: HyperflexNamedVlan
        """
        return self._mgmt_vlan

    @mgmt_vlan.setter
    def mgmt_vlan(self, mgmt_vlan):
        """
        Sets the mgmt_vlan of this HyperflexClusterNetworkPolicy.
        Management VLAN  

        :param mgmt_vlan: The mgmt_vlan of this HyperflexClusterNetworkPolicy.
        :type: HyperflexNamedVlan
        """

        self._mgmt_vlan = mgmt_vlan

    @property
    def organization(self):
        """
        Gets the organization of this HyperflexClusterNetworkPolicy.
        Organization 

        :return: The organization of this HyperflexClusterNetworkPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this HyperflexClusterNetworkPolicy.
        Organization 

        :param organization: The organization of this HyperflexClusterNetworkPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def vm_migration_vlan(self):
        """
        Gets the vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        VM migration VLAN  

        :return: The vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        :rtype: HyperflexNamedVlan
        """
        return self._vm_migration_vlan

    @vm_migration_vlan.setter
    def vm_migration_vlan(self, vm_migration_vlan):
        """
        Sets the vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        VM migration VLAN  

        :param vm_migration_vlan: The vm_migration_vlan of this HyperflexClusterNetworkPolicy.
        :type: HyperflexNamedVlan
        """

        self._vm_migration_vlan = vm_migration_vlan

    @property
    def vm_network_vlans(self):
        """
        Gets the vm_network_vlans of this HyperflexClusterNetworkPolicy.
        VM traffic VLANs   

        :return: The vm_network_vlans of this HyperflexClusterNetworkPolicy.
        :rtype: list[HyperflexNamedVlan]
        """
        return self._vm_network_vlans

    @vm_network_vlans.setter
    def vm_network_vlans(self, vm_network_vlans):
        """
        Sets the vm_network_vlans of this HyperflexClusterNetworkPolicy.
        VM traffic VLANs   

        :param vm_network_vlans: The vm_network_vlans of this HyperflexClusterNetworkPolicy.
        :type: list[HyperflexNamedVlan]
        """

        self._vm_network_vlans = vm_network_vlans

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
        if not isinstance(other, HyperflexClusterNetworkPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
