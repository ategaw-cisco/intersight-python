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


class PolicyAbstractConfigChangeDetail(object):
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
        'changes': 'list[str]',
        'config_change_context': 'PolicyConfigResultContext',
        'disruptions': 'list[str]',
        'message': 'str',
        'mod_status': 'str'
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
        'changes': 'Changes',
        'config_change_context': 'ConfigChangeContext',
        'disruptions': 'Disruptions',
        'message': 'Message',
        'mod_status': 'ModStatus'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, changes=None, config_change_context=None, disruptions=None, message=None, mod_status='None'):
        """
        PolicyAbstractConfigChangeDetail - a model defined in Swagger
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
        self._changes = None
        self._config_change_context = None
        self._disruptions = None
        self._message = None
        self._mod_status = None

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
        if changes is not None:
          self.changes = changes
        if config_change_context is not None:
          self.config_change_context = config_change_context
        if disruptions is not None:
          self.disruptions = disruptions
        if message is not None:
          self.message = message
        if mod_status is not None:
          self.mod_status = mod_status

    @property
    def account_moid(self):
        """
        Gets the account_moid of this PolicyAbstractConfigChangeDetail.
        The Account ID for this managed object.  

        :return: The account_moid of this PolicyAbstractConfigChangeDetail.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this PolicyAbstractConfigChangeDetail.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this PolicyAbstractConfigChangeDetail.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this PolicyAbstractConfigChangeDetail.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this PolicyAbstractConfigChangeDetail.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this PolicyAbstractConfigChangeDetail.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this PolicyAbstractConfigChangeDetail.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this PolicyAbstractConfigChangeDetail.
        The time when this managed object was created.  

        :return: The create_time of this PolicyAbstractConfigChangeDetail.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this PolicyAbstractConfigChangeDetail.
        The time when this managed object was created.  

        :param create_time: The create_time of this PolicyAbstractConfigChangeDetail.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this PolicyAbstractConfigChangeDetail.
        The time when this managed object was last modified.  

        :return: The mod_time of this PolicyAbstractConfigChangeDetail.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this PolicyAbstractConfigChangeDetail.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this PolicyAbstractConfigChangeDetail.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this PolicyAbstractConfigChangeDetail.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this PolicyAbstractConfigChangeDetail.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this PolicyAbstractConfigChangeDetail.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this PolicyAbstractConfigChangeDetail.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this PolicyAbstractConfigChangeDetail.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this PolicyAbstractConfigChangeDetail.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this PolicyAbstractConfigChangeDetail.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this PolicyAbstractConfigChangeDetail.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this PolicyAbstractConfigChangeDetail.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this PolicyAbstractConfigChangeDetail.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this PolicyAbstractConfigChangeDetail.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this PolicyAbstractConfigChangeDetail.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this PolicyAbstractConfigChangeDetail.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this PolicyAbstractConfigChangeDetail.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this PolicyAbstractConfigChangeDetail.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this PolicyAbstractConfigChangeDetail.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this PolicyAbstractConfigChangeDetail.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this PolicyAbstractConfigChangeDetail.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this PolicyAbstractConfigChangeDetail.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this PolicyAbstractConfigChangeDetail.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this PolicyAbstractConfigChangeDetail.
        The versioning info for this managed object   

        :return: The version_context of this PolicyAbstractConfigChangeDetail.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this PolicyAbstractConfigChangeDetail.
        The versioning info for this managed object   

        :param version_context: The version_context of this PolicyAbstractConfigChangeDetail.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def changes(self):
        """
        Gets the changes of this PolicyAbstractConfigChangeDetail.
        Type of the configuration change  

        :return: The changes of this PolicyAbstractConfigChangeDetail.
        :rtype: list[str]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """
        Sets the changes of this PolicyAbstractConfigChangeDetail.
        Type of the configuration change  

        :param changes: The changes of this PolicyAbstractConfigChangeDetail.
        :type: list[str]
        """

        self._changes = changes

    @property
    def config_change_context(self):
        """
        Gets the config_change_context of this PolicyAbstractConfigChangeDetail.
        Context information on the change.  

        :return: The config_change_context of this PolicyAbstractConfigChangeDetail.
        :rtype: PolicyConfigResultContext
        """
        return self._config_change_context

    @config_change_context.setter
    def config_change_context(self, config_change_context):
        """
        Sets the config_change_context of this PolicyAbstractConfigChangeDetail.
        Context information on the change.  

        :param config_change_context: The config_change_context of this PolicyAbstractConfigChangeDetail.
        :type: PolicyConfigResultContext
        """

        self._config_change_context = config_change_context

    @property
    def disruptions(self):
        """
        Gets the disruptions of this PolicyAbstractConfigChangeDetail.
        Possible discrution the configuration change might cause  

        :return: The disruptions of this PolicyAbstractConfigChangeDetail.
        :rtype: list[str]
        """
        return self._disruptions

    @disruptions.setter
    def disruptions(self, disruptions):
        """
        Sets the disruptions of this PolicyAbstractConfigChangeDetail.
        Possible discrution the configuration change might cause  

        :param disruptions: The disruptions of this PolicyAbstractConfigChangeDetail.
        :type: list[str]
        """

        self._disruptions = disruptions

    @property
    def message(self):
        """
        Gets the message of this PolicyAbstractConfigChangeDetail.
        Detailed description of the config change  

        :return: The message of this PolicyAbstractConfigChangeDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this PolicyAbstractConfigChangeDetail.
        Detailed description of the config change  

        :param message: The message of this PolicyAbstractConfigChangeDetail.
        :type: str
        """

        self._message = message

    @property
    def mod_status(self):
        """
        Gets the mod_status of this PolicyAbstractConfigChangeDetail.
        Modification status of the mo in this config change   

        :return: The mod_status of this PolicyAbstractConfigChangeDetail.
        :rtype: str
        """
        return self._mod_status

    @mod_status.setter
    def mod_status(self, mod_status):
        """
        Sets the mod_status of this PolicyAbstractConfigChangeDetail.
        Modification status of the mo in this config change   

        :param mod_status: The mod_status of this PolicyAbstractConfigChangeDetail.
        :type: str
        """
        allowed_values = ["None", "Created", "Modified", "Deleted"]
        if mod_status not in allowed_values:
            raise ValueError(
                "Invalid value for `mod_status` ({0}), must be one of {1}"
                .format(mod_status, allowed_values)
            )

        self._mod_status = mod_status

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
        if not isinstance(other, PolicyAbstractConfigChangeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
