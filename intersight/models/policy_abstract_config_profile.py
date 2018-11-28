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


class PolicyAbstractConfigProfile(object):
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
        'config_context': 'PolicyConfigContext'
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
        'config_context': 'ConfigContext'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, src_template=None, type='instance', action=None, config_context=None):
        """
        PolicyAbstractConfigProfile - a model defined in Swagger
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

    @property
    def account_moid(self):
        """
        Gets the account_moid of this PolicyAbstractConfigProfile.
        The Account ID for this managed object.  

        :return: The account_moid of this PolicyAbstractConfigProfile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this PolicyAbstractConfigProfile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this PolicyAbstractConfigProfile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this PolicyAbstractConfigProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this PolicyAbstractConfigProfile.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this PolicyAbstractConfigProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this PolicyAbstractConfigProfile.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this PolicyAbstractConfigProfile.
        The time when this managed object was created.  

        :return: The create_time of this PolicyAbstractConfigProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this PolicyAbstractConfigProfile.
        The time when this managed object was created.  

        :param create_time: The create_time of this PolicyAbstractConfigProfile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this PolicyAbstractConfigProfile.
        The time when this managed object was last modified.  

        :return: The mod_time of this PolicyAbstractConfigProfile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this PolicyAbstractConfigProfile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this PolicyAbstractConfigProfile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this PolicyAbstractConfigProfile.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this PolicyAbstractConfigProfile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this PolicyAbstractConfigProfile.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this PolicyAbstractConfigProfile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this PolicyAbstractConfigProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this PolicyAbstractConfigProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this PolicyAbstractConfigProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this PolicyAbstractConfigProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this PolicyAbstractConfigProfile.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this PolicyAbstractConfigProfile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this PolicyAbstractConfigProfile.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this PolicyAbstractConfigProfile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this PolicyAbstractConfigProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this PolicyAbstractConfigProfile.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this PolicyAbstractConfigProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this PolicyAbstractConfigProfile.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this PolicyAbstractConfigProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this PolicyAbstractConfigProfile.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this PolicyAbstractConfigProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this PolicyAbstractConfigProfile.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this PolicyAbstractConfigProfile.
        The versioning info for this managed object   

        :return: The version_context of this PolicyAbstractConfigProfile.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this PolicyAbstractConfigProfile.
        The versioning info for this managed object   

        :param version_context: The version_context of this PolicyAbstractConfigProfile.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this PolicyAbstractConfigProfile.
        Description of the profile.  

        :return: The description of this PolicyAbstractConfigProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PolicyAbstractConfigProfile.
        Description of the profile.  

        :param description: The description of this PolicyAbstractConfigProfile.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this PolicyAbstractConfigProfile.
        Name of the profile.  

        :return: The name of this PolicyAbstractConfigProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyAbstractConfigProfile.
        Name of the profile.  

        :param name: The name of this PolicyAbstractConfigProfile.
        :type: str
        """

        self._name = name

    @property
    def src_template(self):
        """
        Gets the src_template of this PolicyAbstractConfigProfile.

        :return: The src_template of this PolicyAbstractConfigProfile.
        :rtype: PolicyAbstractProfileRef
        """
        return self._src_template

    @src_template.setter
    def src_template(self, src_template):
        """
        Sets the src_template of this PolicyAbstractConfigProfile.

        :param src_template: The src_template of this PolicyAbstractConfigProfile.
        :type: PolicyAbstractProfileRef
        """

        self._src_template = src_template

    @property
    def type(self):
        """
        Gets the type of this PolicyAbstractConfigProfile.
        Defines the type of the profile. Accepted value is instance.   

        :return: The type of this PolicyAbstractConfigProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PolicyAbstractConfigProfile.
        Defines the type of the profile. Accepted value is instance.   

        :param type: The type of this PolicyAbstractConfigProfile.
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
        Gets the action of this PolicyAbstractConfigProfile.
        User initiated action. Each profile type has its own supported actions. For hyperflex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign  

        :return: The action of this PolicyAbstractConfigProfile.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PolicyAbstractConfigProfile.
        User initiated action. Each profile type has its own supported actions. For hyperflex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign  

        :param action: The action of this PolicyAbstractConfigProfile.
        :type: str
        """

        self._action = action

    @property
    def config_context(self):
        """
        Gets the config_context of this PolicyAbstractConfigProfile.

        :return: The config_context of this PolicyAbstractConfigProfile.
        :rtype: PolicyConfigContext
        """
        return self._config_context

    @config_context.setter
    def config_context(self, config_context):
        """
        Sets the config_context of this PolicyAbstractConfigProfile.

        :param config_context: The config_context of this PolicyAbstractConfigProfile.
        :type: PolicyConfigContext
        """

        self._config_context = config_context

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
        if not isinstance(other, PolicyAbstractConfigProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
