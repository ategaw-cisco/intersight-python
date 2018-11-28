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


class IamUser(object):
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
        'api_keys': 'list[IamApiKeyRef]',
        'client_ip_address': 'str',
        'email': 'str',
        'first_name': 'str',
        'idp': 'IamIdpRef',
        'idpreference': 'IamIdpReferenceRef',
        'last_login_time': 'datetime',
        'last_name': 'str',
        'name': 'str',
        'permissions': 'list[IamPermissionRef]',
        'sessions': 'list[IamSessionRef]',
        'user_type': 'str'
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
        'api_keys': 'ApiKeys',
        'client_ip_address': 'ClientIpAddress',
        'email': 'Email',
        'first_name': 'FirstName',
        'idp': 'Idp',
        'idpreference': 'Idpreference',
        'last_login_time': 'LastLoginTime',
        'last_name': 'LastName',
        'name': 'Name',
        'permissions': 'Permissions',
        'sessions': 'Sessions',
        'user_type': 'UserType'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, api_keys=None, client_ip_address=None, email=None, first_name=None, idp=None, idpreference=None, last_login_time=None, last_name=None, name=None, permissions=None, sessions=None, user_type=None):
        """
        IamUser - a model defined in Swagger
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
        self._api_keys = None
        self._client_ip_address = None
        self._email = None
        self._first_name = None
        self._idp = None
        self._idpreference = None
        self._last_login_time = None
        self._last_name = None
        self._name = None
        self._permissions = None
        self._sessions = None
        self._user_type = None

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
        if api_keys is not None:
          self.api_keys = api_keys
        if client_ip_address is not None:
          self.client_ip_address = client_ip_address
        if email is not None:
          self.email = email
        if first_name is not None:
          self.first_name = first_name
        if idp is not None:
          self.idp = idp
        if idpreference is not None:
          self.idpreference = idpreference
        if last_login_time is not None:
          self.last_login_time = last_login_time
        if last_name is not None:
          self.last_name = last_name
        if name is not None:
          self.name = name
        if permissions is not None:
          self.permissions = permissions
        if sessions is not None:
          self.sessions = sessions
        if user_type is not None:
          self.user_type = user_type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamUser.
        The Account ID for this managed object.  

        :return: The account_moid of this IamUser.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamUser.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamUser.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamUser.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamUser.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamUser.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamUser.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamUser.
        The time when this managed object was created.  

        :return: The create_time of this IamUser.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamUser.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamUser.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamUser.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamUser.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamUser.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamUser.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamUser.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamUser.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamUser.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamUser.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamUser.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamUser.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamUser.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamUser.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamUser.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamUser.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamUser.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamUser.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamUser.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamUser.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamUser.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamUser.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamUser.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamUser.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamUser.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamUser.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamUser.
        The versioning info for this managed object   

        :return: The version_context of this IamUser.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamUser.
        The versioning info for this managed object   

        :param version_context: The version_context of this IamUser.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def api_keys(self):
        """
        Gets the api_keys of this IamUser.
        Current API keys of the user. API keys are used to programatically perform API calls. 

        :return: The api_keys of this IamUser.
        :rtype: list[IamApiKeyRef]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """
        Sets the api_keys of this IamUser.
        Current API keys of the user. API keys are used to programatically perform API calls. 

        :param api_keys: The api_keys of this IamUser.
        :type: list[IamApiKeyRef]
        """

        self._api_keys = api_keys

    @property
    def client_ip_address(self):
        """
        Gets the client_ip_address of this IamUser.
        Specifies the IP address from which the user logged in the last time.  

        :return: The client_ip_address of this IamUser.
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address):
        """
        Sets the client_ip_address of this IamUser.
        Specifies the IP address from which the user logged in the last time.  

        :param client_ip_address: The client_ip_address of this IamUser.
        :type: str
        """

        self._client_ip_address = client_ip_address

    @property
    def email(self):
        """
        Gets the email of this IamUser.
        Email of the user. Users are added to Intersight using the email configured in the IdP.  

        :return: The email of this IamUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this IamUser.
        Email of the user. Users are added to Intersight using the email configured in the IdP.  

        :param email: The email of this IamUser.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this IamUser.
        First name of the user. This field is populated from the IdP attributes received after authentication.  

        :return: The first_name of this IamUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this IamUser.
        First name of the user. This field is populated from the IdP attributes received after authentication.  

        :param first_name: The first_name of this IamUser.
        :type: str
        """

        self._first_name = first_name

    @property
    def idp(self):
        """
        Gets the idp of this IamUser.

        :return: The idp of this IamUser.
        :rtype: IamIdpRef
        """
        return self._idp

    @idp.setter
    def idp(self, idp):
        """
        Sets the idp of this IamUser.

        :param idp: The idp of this IamUser.
        :type: IamIdpRef
        """

        self._idp = idp

    @property
    def idpreference(self):
        """
        Gets the idpreference of this IamUser.

        :return: The idpreference of this IamUser.
        :rtype: IamIdpReferenceRef
        """
        return self._idpreference

    @idpreference.setter
    def idpreference(self, idpreference):
        """
        Sets the idpreference of this IamUser.

        :param idpreference: The idpreference of this IamUser.
        :type: IamIdpReferenceRef
        """

        self._idpreference = idpreference

    @property
    def last_login_time(self):
        """
        Gets the last_login_time of this IamUser.
        Specifies the last login time for user.  

        :return: The last_login_time of this IamUser.
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """
        Sets the last_login_time of this IamUser.
        Specifies the last login time for user.  

        :param last_login_time: The last_login_time of this IamUser.
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def last_name(self):
        """
        Gets the last_name of this IamUser.
        Last name of the user. This field is populated from the IdP attributes received after authentication.  

        :return: The last_name of this IamUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this IamUser.
        Last name of the user. This field is populated from the IdP attributes received after authentication.  

        :param last_name: The last_name of this IamUser.
        :type: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """
        Gets the name of this IamUser.
        UserID as configured in the IdP.  

        :return: The name of this IamUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamUser.
        UserID as configured in the IdP.  

        :param name: The name of this IamUser.
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """
        Gets the permissions of this IamUser.
        Permissions assigned to the user. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy. 

        :return: The permissions of this IamUser.
        :rtype: list[IamPermissionRef]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this IamUser.
        Permissions assigned to the user. Permission provides a way to assign roles to a user or user group to perform operations on object hierarchy. 

        :param permissions: The permissions of this IamUser.
        :type: list[IamPermissionRef]
        """

        self._permissions = permissions

    @property
    def sessions(self):
        """
        Gets the sessions of this IamUser.
        Current web sessions of the user. After a user logs into Intersight, a session object is created. This session object is deleted upon logout, idle timeout, expiry timeout, or manual deletion. 

        :return: The sessions of this IamUser.
        :rtype: list[IamSessionRef]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """
        Sets the sessions of this IamUser.
        Current web sessions of the user. After a user logs into Intersight, a session object is created. This session object is deleted upon logout, idle timeout, expiry timeout, or manual deletion. 

        :param sessions: The sessions of this IamUser.
        :type: list[IamSessionRef]
        """

        self._sessions = sessions

    @property
    def user_type(self):
        """
        Gets the user_type of this IamUser.
        Specifies if the user is added manually by specifying email, or has logged in using groups, based on IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic.   

        :return: The user_type of this IamUser.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """
        Sets the user_type of this IamUser.
        Specifies if the user is added manually by specifying email, or has logged in using groups, based on IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic.   

        :param user_type: The user_type of this IamUser.
        :type: str
        """

        self._user_type = user_type

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
        if not isinstance(other, IamUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
