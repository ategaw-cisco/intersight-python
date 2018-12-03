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


class HyperflexConfigResultEntry(object):
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
        'completed_time': 'str',
        'context': 'PolicyConfigResultContext',
        'message': 'str',
        'owner_id': 'str',
        'state': 'str',
        'type': 'str',
        'config_result': 'HyperflexConfigResultRef'
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
        'completed_time': 'CompletedTime',
        'context': 'Context',
        'message': 'Message',
        'owner_id': 'OwnerId',
        'state': 'State',
        'type': 'Type',
        'config_result': 'ConfigResult'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, completed_time=None, context=None, message=None, owner_id=None, state=None, type=None, config_result=None):
        """
        HyperflexConfigResultEntry - a model defined in Swagger
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
        self._completed_time = None
        self._context = None
        self._message = None
        self._owner_id = None
        self._state = None
        self._type = None
        self._config_result = None

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
        if completed_time is not None:
          self.completed_time = completed_time
        if context is not None:
          self.context = context
        if message is not None:
          self.message = message
        if owner_id is not None:
          self.owner_id = owner_id
        if state is not None:
          self.state = state
        if type is not None:
          self.type = type
        if config_result is not None:
          self.config_result = config_result

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexConfigResultEntry.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexConfigResultEntry.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexConfigResultEntry.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexConfigResultEntry.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexConfigResultEntry.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexConfigResultEntry.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexConfigResultEntry.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexConfigResultEntry.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexConfigResultEntry.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexConfigResultEntry.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexConfigResultEntry.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexConfigResultEntry.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexConfigResultEntry.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexConfigResultEntry.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexConfigResultEntry.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexConfigResultEntry.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexConfigResultEntry.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexConfigResultEntry.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexConfigResultEntry.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexConfigResultEntry.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexConfigResultEntry.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexConfigResultEntry.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexConfigResultEntry.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexConfigResultEntry.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexConfigResultEntry.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexConfigResultEntry.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexConfigResultEntry.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexConfigResultEntry.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexConfigResultEntry.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexConfigResultEntry.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexConfigResultEntry.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexConfigResultEntry.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexConfigResultEntry.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexConfigResultEntry.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexConfigResultEntry.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexConfigResultEntry.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexConfigResultEntry.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def completed_time(self):
        """
        Gets the completed_time of this HyperflexConfigResultEntry.
        The completed time of the task in installer  

        :return: The completed_time of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._completed_time

    @completed_time.setter
    def completed_time(self, completed_time):
        """
        Sets the completed_time of this HyperflexConfigResultEntry.
        The completed time of the task in installer  

        :param completed_time: The completed_time of this HyperflexConfigResultEntry.
        :type: str
        """

        self._completed_time = completed_time

    @property
    def context(self):
        """
        Gets the context of this HyperflexConfigResultEntry.

        :return: The context of this HyperflexConfigResultEntry.
        :rtype: PolicyConfigResultContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this HyperflexConfigResultEntry.

        :param context: The context of this HyperflexConfigResultEntry.
        :type: PolicyConfigResultContext
        """

        self._context = context

    @property
    def message(self):
        """
        Gets the message of this HyperflexConfigResultEntry.
        Localized message based on the locale setting of the user's context  

        :return: The message of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this HyperflexConfigResultEntry.
        Localized message based on the locale setting of the user's context  

        :param message: The message of this HyperflexConfigResultEntry.
        :type: str
        """

        self._message = message

    @property
    def owner_id(self):
        """
        Gets the owner_id of this HyperflexConfigResultEntry.

        :return: The owner_id of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this HyperflexConfigResultEntry.

        :param owner_id: The owner_id of this HyperflexConfigResultEntry.
        :type: str
        """

        self._owner_id = owner_id

    @property
    def state(self):
        """
        Gets the state of this HyperflexConfigResultEntry.
        Values  -- ok, ok-with-warning, errored  

        :return: The state of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this HyperflexConfigResultEntry.
        Values  -- ok, ok-with-warning, errored  

        :param state: The state of this HyperflexConfigResultEntry.
        :type: str
        """

        self._state = state

    @property
    def type(self):
        """
        Gets the type of this HyperflexConfigResultEntry.
        Indicates if the result is reported during the logical model validation/resource allocation phase or the configuration applying phase. Values -- validation, config   

        :return: The type of this HyperflexConfigResultEntry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this HyperflexConfigResultEntry.
        Indicates if the result is reported during the logical model validation/resource allocation phase or the configuration applying phase. Values -- validation, config   

        :param type: The type of this HyperflexConfigResultEntry.
        :type: str
        """

        self._type = type

    @property
    def config_result(self):
        """
        Gets the config_result of this HyperflexConfigResultEntry.

        :return: The config_result of this HyperflexConfigResultEntry.
        :rtype: HyperflexConfigResultRef
        """
        return self._config_result

    @config_result.setter
    def config_result(self, config_result):
        """
        Sets the config_result of this HyperflexConfigResultEntry.

        :param config_result: The config_result of this HyperflexConfigResultEntry.
        :type: HyperflexConfigResultRef
        """

        self._config_result = config_result

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
        if not isinstance(other, HyperflexConfigResultEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
