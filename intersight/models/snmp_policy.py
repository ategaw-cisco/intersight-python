# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-300
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SnmpPolicy(object):
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
        'access_community_string': 'str',
        'community_access': 'str',
        'enabled': 'bool',
        'engine_id': 'str',
        'organization': 'IamAccountRef',
        'profiles': 'list[PolicyAbstractConfigProfileRef]',
        'snmp_port': 'int',
        'snmp_traps': 'list[SnmpTrap]',
        'snmp_users': 'list[SnmpUser]',
        'sys_contact': 'str',
        'sys_location': 'str',
        'trap_community': 'str'
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
        'access_community_string': 'AccessCommunityString',
        'community_access': 'CommunityAccess',
        'enabled': 'Enabled',
        'engine_id': 'EngineId',
        'organization': 'Organization',
        'profiles': 'Profiles',
        'snmp_port': 'SnmpPort',
        'snmp_traps': 'SnmpTraps',
        'snmp_users': 'SnmpUsers',
        'sys_contact': 'SysContact',
        'sys_location': 'SysLocation',
        'trap_community': 'TrapCommunity'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, access_community_string=None, community_access='Disabled', enabled=None, engine_id=None, organization=None, profiles=None, snmp_port=None, snmp_traps=None, snmp_users=None, sys_contact=None, sys_location=None, trap_community=None):
        """
        SnmpPolicy - a model defined in Swagger
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
        self._access_community_string = None
        self._community_access = None
        self._enabled = None
        self._engine_id = None
        self._organization = None
        self._profiles = None
        self._snmp_port = None
        self._snmp_traps = None
        self._snmp_users = None
        self._sys_contact = None
        self._sys_location = None
        self._trap_community = None

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
        if access_community_string is not None:
          self.access_community_string = access_community_string
        if community_access is not None:
          self.community_access = community_access
        if enabled is not None:
          self.enabled = enabled
        if engine_id is not None:
          self.engine_id = engine_id
        if organization is not None:
          self.organization = organization
        if profiles is not None:
          self.profiles = profiles
        if snmp_port is not None:
          self.snmp_port = snmp_port
        if snmp_traps is not None:
          self.snmp_traps = snmp_traps
        if snmp_users is not None:
          self.snmp_users = snmp_users
        if sys_contact is not None:
          self.sys_contact = sys_contact
        if sys_location is not None:
          self.sys_location = sys_location
        if trap_community is not None:
          self.trap_community = trap_community

    @property
    def account_moid(self):
        """
        Gets the account_moid of this SnmpPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this SnmpPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this SnmpPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this SnmpPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this SnmpPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this SnmpPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this SnmpPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this SnmpPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this SnmpPolicy.
        The time when this managed object was created.  

        :return: The create_time of this SnmpPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this SnmpPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this SnmpPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this SnmpPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this SnmpPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this SnmpPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this SnmpPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this SnmpPolicy.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this SnmpPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this SnmpPolicy.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this SnmpPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this SnmpPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this SnmpPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SnmpPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this SnmpPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this SnmpPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this SnmpPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this SnmpPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this SnmpPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this SnmpPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this SnmpPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SnmpPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this SnmpPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this SnmpPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this SnmpPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SnmpPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this SnmpPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this SnmpPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this SnmpPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this SnmpPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this SnmpPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this SnmpPolicy.
        Description of the policy.  

        :return: The description of this SnmpPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SnmpPolicy.
        Description of the policy.  

        :param description: The description of this SnmpPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this SnmpPolicy.
        Name of the policy.   

        :return: The name of this SnmpPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SnmpPolicy.
        Name of the policy.   

        :param name: The name of this SnmpPolicy.
        :type: str
        """

        self._name = name

    @property
    def access_community_string(self):
        """
        Gets the access_community_string of this SnmpPolicy.
        The default SNMPv1, SNMPv2c community name or SNMPv3 username to include on any trap messages sent to the SNMP host. The name can be 18 characters long.  

        :return: The access_community_string of this SnmpPolicy.
        :rtype: str
        """
        return self._access_community_string

    @access_community_string.setter
    def access_community_string(self, access_community_string):
        """
        Sets the access_community_string of this SnmpPolicy.
        The default SNMPv1, SNMPv2c community name or SNMPv3 username to include on any trap messages sent to the SNMP host. The name can be 18 characters long.  

        :param access_community_string: The access_community_string of this SnmpPolicy.
        :type: str
        """

        self._access_community_string = access_community_string

    @property
    def community_access(self):
        """
        Gets the community_access of this SnmpPolicy.
        Controls access to the information in the inventory tables. Applicable only for SNMPv1 and SNMPv2c users.  

        :return: The community_access of this SnmpPolicy.
        :rtype: str
        """
        return self._community_access

    @community_access.setter
    def community_access(self, community_access):
        """
        Sets the community_access of this SnmpPolicy.
        Controls access to the information in the inventory tables. Applicable only for SNMPv1 and SNMPv2c users.  

        :param community_access: The community_access of this SnmpPolicy.
        :type: str
        """
        allowed_values = ["Disabled", "Limited", "Full"]
        if community_access not in allowed_values:
            raise ValueError(
                "Invalid value for `community_access` ({0}), must be one of {1}"
                .format(community_access, allowed_values)
            )

        self._community_access = community_access

    @property
    def enabled(self):
        """
        Gets the enabled of this SnmpPolicy.
        State of the SNMP Policy on the endpoint. If enabled, the endpoint sends SNMP traps to the designated host.  

        :return: The enabled of this SnmpPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SnmpPolicy.
        State of the SNMP Policy on the endpoint. If enabled, the endpoint sends SNMP traps to the designated host.  

        :param enabled: The enabled of this SnmpPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def engine_id(self):
        """
        Gets the engine_id of this SnmpPolicy.
        User-defined unique identification of the static engine  

        :return: The engine_id of this SnmpPolicy.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """
        Sets the engine_id of this SnmpPolicy.
        User-defined unique identification of the static engine  

        :param engine_id: The engine_id of this SnmpPolicy.
        :type: str
        """

        self._engine_id = engine_id

    @property
    def organization(self):
        """
        Gets the organization of this SnmpPolicy.
        Organization 

        :return: The organization of this SnmpPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this SnmpPolicy.
        Organization 

        :param organization: The organization of this SnmpPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def profiles(self):
        """
        Gets the profiles of this SnmpPolicy.
        Relationship to the profile object 

        :return: The profiles of this SnmpPolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this SnmpPolicy.
        Relationship to the profile object 

        :param profiles: The profiles of this SnmpPolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

    @property
    def snmp_port(self):
        """
        Gets the snmp_port of this SnmpPolicy.
        Port on which Cisco IMC SNMP agent runs  

        :return: The snmp_port of this SnmpPolicy.
        :rtype: int
        """
        return self._snmp_port

    @snmp_port.setter
    def snmp_port(self, snmp_port):
        """
        Sets the snmp_port of this SnmpPolicy.
        Port on which Cisco IMC SNMP agent runs  

        :param snmp_port: The snmp_port of this SnmpPolicy.
        :type: int
        """

        self._snmp_port = snmp_port

    @property
    def snmp_traps(self):
        """
        Gets the snmp_traps of this SnmpPolicy.
        List of SNMP Traps  

        :return: The snmp_traps of this SnmpPolicy.
        :rtype: list[SnmpTrap]
        """
        return self._snmp_traps

    @snmp_traps.setter
    def snmp_traps(self, snmp_traps):
        """
        Sets the snmp_traps of this SnmpPolicy.
        List of SNMP Traps  

        :param snmp_traps: The snmp_traps of this SnmpPolicy.
        :type: list[SnmpTrap]
        """

        self._snmp_traps = snmp_traps

    @property
    def snmp_users(self):
        """
        Gets the snmp_users of this SnmpPolicy.
        List of SNMP Users  

        :return: The snmp_users of this SnmpPolicy.
        :rtype: list[SnmpUser]
        """
        return self._snmp_users

    @snmp_users.setter
    def snmp_users(self, snmp_users):
        """
        Sets the snmp_users of this SnmpPolicy.
        List of SNMP Users  

        :param snmp_users: The snmp_users of this SnmpPolicy.
        :type: list[SnmpUser]
        """

        self._snmp_users = snmp_users

    @property
    def sys_contact(self):
        """
        Gets the sys_contact of this SnmpPolicy.
        Contact person responsible for the SNMP implementation. Enter a string up to 64 characters, such as an email address or a name and telephone number.  

        :return: The sys_contact of this SnmpPolicy.
        :rtype: str
        """
        return self._sys_contact

    @sys_contact.setter
    def sys_contact(self, sys_contact):
        """
        Sets the sys_contact of this SnmpPolicy.
        Contact person responsible for the SNMP implementation. Enter a string up to 64 characters, such as an email address or a name and telephone number.  

        :param sys_contact: The sys_contact of this SnmpPolicy.
        :type: str
        """

        self._sys_contact = sys_contact

    @property
    def sys_location(self):
        """
        Gets the sys_location of this SnmpPolicy.
        Location of host on which the SNMP agent(server) runs  

        :return: The sys_location of this SnmpPolicy.
        :rtype: str
        """
        return self._sys_location

    @sys_location.setter
    def sys_location(self, sys_location):
        """
        Sets the sys_location of this SnmpPolicy.
        Location of host on which the SNMP agent(server) runs  

        :param sys_location: The sys_location of this SnmpPolicy.
        :type: str
        """

        self._sys_location = sys_location

    @property
    def trap_community(self):
        """
        Gets the trap_community of this SnmpPolicy.
        SNMP community group used for sending SNMP trap to other devices. Valid only for SNMPv2c users   

        :return: The trap_community of this SnmpPolicy.
        :rtype: str
        """
        return self._trap_community

    @trap_community.setter
    def trap_community(self, trap_community):
        """
        Sets the trap_community of this SnmpPolicy.
        SNMP community group used for sending SNMP trap to other devices. Valid only for SNMPv2c users   

        :param trap_community: The trap_community of this SnmpPolicy.
        :type: str
        """

        self._trap_community = trap_community

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
        if not isinstance(other, SnmpPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
