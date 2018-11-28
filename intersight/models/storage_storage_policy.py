# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-264
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StorageStoragePolicy(object):
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
        'disk_group_policies': 'list[StorageDiskGroupPolicyRef]',
        'global_hot_spares': 'list[StorageLocalDisk]',
        'organization': 'IamAccountRef',
        'profiles': 'list[PolicyAbstractConfigProfileRef]',
        'retain_policy_virtual_drives': 'bool',
        'unused_disks_state': 'str',
        'virtual_drives': 'list[StorageVirtualDriveConfig]'
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
        'disk_group_policies': 'DiskGroupPolicies',
        'global_hot_spares': 'GlobalHotSpares',
        'organization': 'Organization',
        'profiles': 'Profiles',
        'retain_policy_virtual_drives': 'RetainPolicyVirtualDrives',
        'unused_disks_state': 'UnusedDisksState',
        'virtual_drives': 'VirtualDrives'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, disk_group_policies=None, global_hot_spares=None, organization=None, profiles=None, retain_policy_virtual_drives=None, unused_disks_state='UnconfiguredGood', virtual_drives=None):
        """
        StorageStoragePolicy - a model defined in Swagger
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
        self._disk_group_policies = None
        self._global_hot_spares = None
        self._organization = None
        self._profiles = None
        self._retain_policy_virtual_drives = None
        self._unused_disks_state = None
        self._virtual_drives = None

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
        if disk_group_policies is not None:
          self.disk_group_policies = disk_group_policies
        if global_hot_spares is not None:
          self.global_hot_spares = global_hot_spares
        if organization is not None:
          self.organization = organization
        if profiles is not None:
          self.profiles = profiles
        if retain_policy_virtual_drives is not None:
          self.retain_policy_virtual_drives = retain_policy_virtual_drives
        if unused_disks_state is not None:
          self.unused_disks_state = unused_disks_state
        if virtual_drives is not None:
          self.virtual_drives = virtual_drives

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageStoragePolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageStoragePolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageStoragePolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageStoragePolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageStoragePolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageStoragePolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageStoragePolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageStoragePolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageStoragePolicy.
        The time when this managed object was created.  

        :return: The create_time of this StorageStoragePolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageStoragePolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageStoragePolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageStoragePolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageStoragePolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageStoragePolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageStoragePolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageStoragePolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageStoragePolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageStoragePolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageStoragePolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageStoragePolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageStoragePolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageStoragePolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageStoragePolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageStoragePolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageStoragePolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageStoragePolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageStoragePolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageStoragePolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageStoragePolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageStoragePolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageStoragePolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this StorageStoragePolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageStoragePolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageStoragePolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageStoragePolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageStoragePolicy.
        The versioning info for this managed object   

        :return: The version_context of this StorageStoragePolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageStoragePolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this StorageStoragePolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this StorageStoragePolicy.
        Description of the policy.  

        :return: The description of this StorageStoragePolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StorageStoragePolicy.
        Description of the policy.  

        :param description: The description of this StorageStoragePolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this StorageStoragePolicy.
        Name of the policy.   

        :return: The name of this StorageStoragePolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StorageStoragePolicy.
        Name of the policy.   

        :param name: The name of this StorageStoragePolicy.
        :type: str
        """

        self._name = name

    @property
    def disk_group_policies(self):
        """
        Gets the disk_group_policies of this StorageStoragePolicy.
        Relationship to the used disk group policies 

        :return: The disk_group_policies of this StorageStoragePolicy.
        :rtype: list[StorageDiskGroupPolicyRef]
        """
        return self._disk_group_policies

    @disk_group_policies.setter
    def disk_group_policies(self, disk_group_policies):
        """
        Sets the disk_group_policies of this StorageStoragePolicy.
        Relationship to the used disk group policies 

        :param disk_group_policies: The disk_group_policies of this StorageStoragePolicy.
        :type: list[StorageDiskGroupPolicyRef]
        """

        self._disk_group_policies = disk_group_policies

    @property
    def global_hot_spares(self):
        """
        Gets the global_hot_spares of this StorageStoragePolicy.
        A collection of disks used as hot spares globally for all the RAID groups   

        :return: The global_hot_spares of this StorageStoragePolicy.
        :rtype: list[StorageLocalDisk]
        """
        return self._global_hot_spares

    @global_hot_spares.setter
    def global_hot_spares(self, global_hot_spares):
        """
        Sets the global_hot_spares of this StorageStoragePolicy.
        A collection of disks used as hot spares globally for all the RAID groups   

        :param global_hot_spares: The global_hot_spares of this StorageStoragePolicy.
        :type: list[StorageLocalDisk]
        """

        self._global_hot_spares = global_hot_spares

    @property
    def organization(self):
        """
        Gets the organization of this StorageStoragePolicy.
        Organization 

        :return: The organization of this StorageStoragePolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this StorageStoragePolicy.
        Organization 

        :param organization: The organization of this StorageStoragePolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def profiles(self):
        """
        Gets the profiles of this StorageStoragePolicy.
        Relationship to the profile objects 

        :return: The profiles of this StorageStoragePolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this StorageStoragePolicy.
        Relationship to the profile objects 

        :param profiles: The profiles of this StorageStoragePolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

    @property
    def retain_policy_virtual_drives(self):
        """
        Gets the retain_policy_virtual_drives of this StorageStoragePolicy.
        Retains the virtual drives defined in policy if they exist already. If this flag is false, the existing virtual drives are removed and created again based on virtual drives in the policy   

        :return: The retain_policy_virtual_drives of this StorageStoragePolicy.
        :rtype: bool
        """
        return self._retain_policy_virtual_drives

    @retain_policy_virtual_drives.setter
    def retain_policy_virtual_drives(self, retain_policy_virtual_drives):
        """
        Sets the retain_policy_virtual_drives of this StorageStoragePolicy.
        Retains the virtual drives defined in policy if they exist already. If this flag is false, the existing virtual drives are removed and created again based on virtual drives in the policy   

        :param retain_policy_virtual_drives: The retain_policy_virtual_drives of this StorageStoragePolicy.
        :type: bool
        """

        self._retain_policy_virtual_drives = retain_policy_virtual_drives

    @property
    def unused_disks_state(self):
        """
        Gets the unused_disks_state of this StorageStoragePolicy.
        This is used to specify the state, unconfigured good or jbod, in which the disks that are not used in this policy should be moved  

        :return: The unused_disks_state of this StorageStoragePolicy.
        :rtype: str
        """
        return self._unused_disks_state

    @unused_disks_state.setter
    def unused_disks_state(self, unused_disks_state):
        """
        Sets the unused_disks_state of this StorageStoragePolicy.
        This is used to specify the state, unconfigured good or jbod, in which the disks that are not used in this policy should be moved  

        :param unused_disks_state: The unused_disks_state of this StorageStoragePolicy.
        :type: str
        """
        allowed_values = ["UnconfiguredGood", "Jbod"]
        if unused_disks_state not in allowed_values:
            raise ValueError(
                "Invalid value for `unused_disks_state` ({0}), must be one of {1}"
                .format(unused_disks_state, allowed_values)
            )

        self._unused_disks_state = unused_disks_state

    @property
    def virtual_drives(self):
        """
        Gets the virtual_drives of this StorageStoragePolicy.
        The list of virtual drives and the disk groups that need to be created through this policy   

        :return: The virtual_drives of this StorageStoragePolicy.
        :rtype: list[StorageVirtualDriveConfig]
        """
        return self._virtual_drives

    @virtual_drives.setter
    def virtual_drives(self, virtual_drives):
        """
        Sets the virtual_drives of this StorageStoragePolicy.
        The list of virtual drives and the disk groups that need to be created through this policy   

        :param virtual_drives: The virtual_drives of this StorageStoragePolicy.
        :type: list[StorageVirtualDriveConfig]
        """

        self._virtual_drives = virtual_drives

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
        if not isinstance(other, StorageStoragePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
