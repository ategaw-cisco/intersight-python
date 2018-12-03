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


class SolPolicy(object):
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
        'baud_rate': 'int',
        'com_port': 'str',
        'enabled': 'bool',
        'organization': 'IamAccountRef',
        'profiles': 'list[PolicyAbstractConfigProfileRef]',
        'ssh_port': 'int'
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
        'baud_rate': 'BaudRate',
        'com_port': 'ComPort',
        'enabled': 'Enabled',
        'organization': 'Organization',
        'profiles': 'Profiles',
        'ssh_port': 'SshPort'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, baud_rate=None, com_port='com0', enabled=None, organization=None, profiles=None, ssh_port=None):
        """
        SolPolicy - a model defined in Swagger
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
        self._baud_rate = None
        self._com_port = None
        self._enabled = None
        self._organization = None
        self._profiles = None
        self._ssh_port = None

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
        if baud_rate is not None:
          self.baud_rate = baud_rate
        if com_port is not None:
          self.com_port = com_port
        if enabled is not None:
          self.enabled = enabled
        if organization is not None:
          self.organization = organization
        if profiles is not None:
          self.profiles = profiles
        if ssh_port is not None:
          self.ssh_port = ssh_port

    @property
    def account_moid(self):
        """
        Gets the account_moid of this SolPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this SolPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this SolPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this SolPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this SolPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this SolPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this SolPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this SolPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this SolPolicy.
        The time when this managed object was created.  

        :return: The create_time of this SolPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this SolPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this SolPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this SolPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this SolPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this SolPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this SolPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this SolPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this SolPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this SolPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this SolPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this SolPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this SolPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SolPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this SolPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this SolPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this SolPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this SolPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this SolPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this SolPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this SolPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SolPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this SolPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this SolPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this SolPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SolPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this SolPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this SolPolicy.
        The versioning info for this managed object   

        :return: The version_context of this SolPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this SolPolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this SolPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this SolPolicy.
        Description of the policy.  

        :return: The description of this SolPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SolPolicy.
        Description of the policy.  

        :param description: The description of this SolPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this SolPolicy.
        Name of the policy.   

        :return: The name of this SolPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SolPolicy.
        Name of the policy.   

        :param name: The name of this SolPolicy.
        :type: str
        """

        self._name = name

    @property
    def baud_rate(self):
        """
        Gets the baud_rate of this SolPolicy.
        Baud Rate used for Serial Over LAN communication  

        :return: The baud_rate of this SolPolicy.
        :rtype: int
        """
        return self._baud_rate

    @baud_rate.setter
    def baud_rate(self, baud_rate):
        """
        Sets the baud_rate of this SolPolicy.
        Baud Rate used for Serial Over LAN communication  

        :param baud_rate: The baud_rate of this SolPolicy.
        :type: int
        """

        self._baud_rate = baud_rate

    @property
    def com_port(self):
        """
        Gets the com_port of this SolPolicy.
        Serial port through which the system routes Serial Over LAN communication. This field is available only on some Cisco UCS C-Series servers. If it is unavailable, the server uses COM port 0 by default.  

        :return: The com_port of this SolPolicy.
        :rtype: str
        """
        return self._com_port

    @com_port.setter
    def com_port(self, com_port):
        """
        Sets the com_port of this SolPolicy.
        Serial port through which the system routes Serial Over LAN communication. This field is available only on some Cisco UCS C-Series servers. If it is unavailable, the server uses COM port 0 by default.  

        :param com_port: The com_port of this SolPolicy.
        :type: str
        """
        allowed_values = ["com0", "com1"]
        if com_port not in allowed_values:
            raise ValueError(
                "Invalid value for `com_port` ({0}), must be one of {1}"
                .format(com_port, allowed_values)
            )

        self._com_port = com_port

    @property
    def enabled(self):
        """
        Gets the enabled of this SolPolicy.
        State of Serial Over LAN service on the endpoint  

        :return: The enabled of this SolPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SolPolicy.
        State of Serial Over LAN service on the endpoint  

        :param enabled: The enabled of this SolPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def organization(self):
        """
        Gets the organization of this SolPolicy.
        Organization 

        :return: The organization of this SolPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this SolPolicy.
        Organization 

        :param organization: The organization of this SolPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def profiles(self):
        """
        Gets the profiles of this SolPolicy.
        Relationship to the profile object 

        :return: The profiles of this SolPolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this SolPolicy.
        Relationship to the profile object 

        :param profiles: The profiles of this SolPolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

    @property
    def ssh_port(self):
        """
        Gets the ssh_port of this SolPolicy.
        SSH port used to access Serial Over LAN directly. Enables bypassing Cisco IMC shell to provide direct access to Serial Over LAN.   

        :return: The ssh_port of this SolPolicy.
        :rtype: int
        """
        return self._ssh_port

    @ssh_port.setter
    def ssh_port(self, ssh_port):
        """
        Sets the ssh_port of this SolPolicy.
        SSH port used to access Serial Over LAN directly. Enables bypassing Cisco IMC shell to provide direct access to Serial Over LAN.   

        :param ssh_port: The ssh_port of this SolPolicy.
        :type: int
        """

        self._ssh_port = ssh_port

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
        if not isinstance(other, SolPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
