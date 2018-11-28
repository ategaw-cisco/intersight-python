# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-263
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IamSessionLimits(object):
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
        'account': 'IamAccountRef',
        'idle_time_out': 'int',
        'maximum_limit': 'int',
        'per_user_limit': 'int',
        'session_time_out': 'int'
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
        'account': 'Account',
        'idle_time_out': 'IdleTimeOut',
        'maximum_limit': 'MaximumLimit',
        'per_user_limit': 'PerUserLimit',
        'session_time_out': 'SessionTimeOut'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, account=None, idle_time_out=None, maximum_limit=None, per_user_limit=None, session_time_out=None):
        """
        IamSessionLimits - a model defined in Swagger
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
        self._account = None
        self._idle_time_out = None
        self._maximum_limit = None
        self._per_user_limit = None
        self._session_time_out = None

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
        if account is not None:
          self.account = account
        if idle_time_out is not None:
          self.idle_time_out = idle_time_out
        if maximum_limit is not None:
          self.maximum_limit = maximum_limit
        if per_user_limit is not None:
          self.per_user_limit = per_user_limit
        if session_time_out is not None:
          self.session_time_out = session_time_out

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamSessionLimits.
        The Account ID for this managed object.  

        :return: The account_moid of this IamSessionLimits.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamSessionLimits.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamSessionLimits.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamSessionLimits.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamSessionLimits.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamSessionLimits.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamSessionLimits.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamSessionLimits.
        The time when this managed object was created.  

        :return: The create_time of this IamSessionLimits.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamSessionLimits.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamSessionLimits.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamSessionLimits.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamSessionLimits.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamSessionLimits.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamSessionLimits.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamSessionLimits.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamSessionLimits.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamSessionLimits.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamSessionLimits.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamSessionLimits.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamSessionLimits.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamSessionLimits.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamSessionLimits.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamSessionLimits.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamSessionLimits.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamSessionLimits.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamSessionLimits.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamSessionLimits.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamSessionLimits.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamSessionLimits.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamSessionLimits.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamSessionLimits.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamSessionLimits.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamSessionLimits.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamSessionLimits.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamSessionLimits.
        The versioning info for this managed object   

        :return: The version_context of this IamSessionLimits.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamSessionLimits.
        The versioning info for this managed object   

        :param version_context: The version_context of this IamSessionLimits.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this IamSessionLimits.

        :return: The account of this IamSessionLimits.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this IamSessionLimits.

        :param account: The account of this IamSessionLimits.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def idle_time_out(self):
        """
        Gets the idle_time_out of this IamSessionLimits.
        Duration in seconds specifying the idle timeout interval of web session. Default value is 1800 seconds. When a session is not refreshed for this duration, backend will mark the session as idle and remove the session.  

        :return: The idle_time_out of this IamSessionLimits.
        :rtype: int
        """
        return self._idle_time_out

    @idle_time_out.setter
    def idle_time_out(self, idle_time_out):
        """
        Sets the idle_time_out of this IamSessionLimits.
        Duration in seconds specifying the idle timeout interval of web session. Default value is 1800 seconds. When a session is not refreshed for this duration, backend will mark the session as idle and remove the session.  

        :param idle_time_out: The idle_time_out of this IamSessionLimits.
        :type: int
        """

        self._idle_time_out = idle_time_out

    @property
    def maximum_limit(self):
        """
        Gets the maximum_limit of this IamSessionLimits.
        Maximum sessions allowed in an account. Default value is 128.  

        :return: The maximum_limit of this IamSessionLimits.
        :rtype: int
        """
        return self._maximum_limit

    @maximum_limit.setter
    def maximum_limit(self, maximum_limit):
        """
        Sets the maximum_limit of this IamSessionLimits.
        Maximum sessions allowed in an account. Default value is 128.  

        :param maximum_limit: The maximum_limit of this IamSessionLimits.
        :type: int
        """

        self._maximum_limit = maximum_limit

    @property
    def per_user_limit(self):
        """
        Gets the per_user_limit of this IamSessionLimits.
        Maximum sessions allowed per user. Default value is 32.   

        :return: The per_user_limit of this IamSessionLimits.
        :rtype: int
        """
        return self._per_user_limit

    @per_user_limit.setter
    def per_user_limit(self, per_user_limit):
        """
        Sets the per_user_limit of this IamSessionLimits.
        Maximum sessions allowed per user. Default value is 32.   

        :param per_user_limit: The per_user_limit of this IamSessionLimits.
        :type: int
        """

        self._per_user_limit = per_user_limit

    @property
    def session_time_out(self):
        """
        Gets the session_time_out of this IamSessionLimits.
        Session expiry duration in seconds. Default value is 57600 seconds or 16 hours.   

        :return: The session_time_out of this IamSessionLimits.
        :rtype: int
        """
        return self._session_time_out

    @session_time_out.setter
    def session_time_out(self, session_time_out):
        """
        Sets the session_time_out of this IamSessionLimits.
        Session expiry duration in seconds. Default value is 57600 seconds or 16 hours.   

        :param session_time_out: The session_time_out of this IamSessionLimits.
        :type: int
        """

        self._session_time_out = session_time_out

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
        if not isinstance(other, IamSessionLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
