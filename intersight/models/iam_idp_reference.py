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


class IamIdpReference(object):
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
        'domain_name': 'str',
        'idp': 'IamIdpRef',
        'idp_entity_id': 'str',
        'multi_factor_authentication': 'bool',
        'name': 'str',
        'user_login_time': 'list[IamUserLoginTimeRef]',
        'user_preferences': 'list[IamUserPreferenceRef]',
        'usergroups': 'list[IamUserGroupRef]',
        'users': 'list[IamUserRef]'
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
        'domain_name': 'DomainName',
        'idp': 'Idp',
        'idp_entity_id': 'IdpEntityId',
        'multi_factor_authentication': 'MultiFactorAuthentication',
        'name': 'Name',
        'user_login_time': 'UserLoginTime',
        'user_preferences': 'UserPreferences',
        'usergroups': 'Usergroups',
        'users': 'Users'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, account=None, domain_name=None, idp=None, idp_entity_id=None, multi_factor_authentication=None, name=None, user_login_time=None, user_preferences=None, usergroups=None, users=None):
        """
        IamIdpReference - a model defined in Swagger
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
        self._domain_name = None
        self._idp = None
        self._idp_entity_id = None
        self._multi_factor_authentication = None
        self._name = None
        self._user_login_time = None
        self._user_preferences = None
        self._usergroups = None
        self._users = None

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
        if domain_name is not None:
          self.domain_name = domain_name
        if idp is not None:
          self.idp = idp
        if idp_entity_id is not None:
          self.idp_entity_id = idp_entity_id
        if multi_factor_authentication is not None:
          self.multi_factor_authentication = multi_factor_authentication
        if name is not None:
          self.name = name
        if user_login_time is not None:
          self.user_login_time = user_login_time
        if user_preferences is not None:
          self.user_preferences = user_preferences
        if usergroups is not None:
          self.usergroups = usergroups
        if users is not None:
          self.users = users

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamIdpReference.
        The Account ID for this managed object.  

        :return: The account_moid of this IamIdpReference.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamIdpReference.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamIdpReference.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamIdpReference.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamIdpReference.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamIdpReference.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamIdpReference.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamIdpReference.
        The time when this managed object was created.  

        :return: The create_time of this IamIdpReference.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamIdpReference.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamIdpReference.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamIdpReference.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamIdpReference.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamIdpReference.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamIdpReference.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamIdpReference.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamIdpReference.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamIdpReference.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamIdpReference.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamIdpReference.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamIdpReference.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamIdpReference.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamIdpReference.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamIdpReference.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamIdpReference.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamIdpReference.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamIdpReference.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamIdpReference.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamIdpReference.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamIdpReference.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamIdpReference.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamIdpReference.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamIdpReference.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamIdpReference.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamIdpReference.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamIdpReference.
        The versioning info for this managed object   

        :return: The version_context of this IamIdpReference.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamIdpReference.
        The versioning info for this managed object   

        :param version_context: The version_context of this IamIdpReference.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this IamIdpReference.

        :return: The account of this IamIdpReference.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this IamIdpReference.

        :param account: The account of this IamIdpReference.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def domain_name(self):
        """
        Gets the domain_name of this IamIdpReference.
        User's email domain name for this IdP. When a user enters an email during login in the Intersight home page, the IdP is picked by matching this domain name with the email domain name for authentication.  

        :return: The domain_name of this IamIdpReference.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this IamIdpReference.
        User's email domain name for this IdP. When a user enters an email during login in the Intersight home page, the IdP is picked by matching this domain name with the email domain name for authentication.  

        :param domain_name: The domain_name of this IamIdpReference.
        :type: str
        """

        self._domain_name = domain_name

    @property
    def idp(self):
        """
        Gets the idp of this IamIdpReference.
        Reference to System default Cisco IdP. 

        :return: The idp of this IamIdpReference.
        :rtype: IamIdpRef
        """
        return self._idp

    @idp.setter
    def idp(self, idp):
        """
        Sets the idp of this IamIdpReference.
        Reference to System default Cisco IdP. 

        :param idp: The idp of this IamIdpReference.
        :type: IamIdpRef
        """

        self._idp = idp

    @property
    def idp_entity_id(self):
        """
        Gets the idp_entity_id of this IamIdpReference.
        Entity ID of the IdP. In SAML, the entity ID uniquely identifies the IdP/Service Provider.  

        :return: The idp_entity_id of this IamIdpReference.
        :rtype: str
        """
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, idp_entity_id):
        """
        Sets the idp_entity_id of this IamIdpReference.
        Entity ID of the IdP. In SAML, the entity ID uniquely identifies the IdP/Service Provider.  

        :param idp_entity_id: The idp_entity_id of this IamIdpReference.
        :type: str
        """

        self._idp_entity_id = idp_entity_id

    @property
    def multi_factor_authentication(self):
        """
        Gets the multi_factor_authentication of this IamIdpReference.
        Flag represents if multi factor authentication is required for Cisco IdP users.  

        :return: The multi_factor_authentication of this IamIdpReference.
        :rtype: bool
        """
        return self._multi_factor_authentication

    @multi_factor_authentication.setter
    def multi_factor_authentication(self, multi_factor_authentication):
        """
        Sets the multi_factor_authentication of this IamIdpReference.
        Flag represents if multi factor authentication is required for Cisco IdP users.  

        :param multi_factor_authentication: The multi_factor_authentication of this IamIdpReference.
        :type: bool
        """

        self._multi_factor_authentication = multi_factor_authentication

    @property
    def name(self):
        """
        Gets the name of this IamIdpReference.
        Cisco IdP reference in an account.   

        :return: The name of this IamIdpReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamIdpReference.
        Cisco IdP reference in an account.   

        :param name: The name of this IamIdpReference.
        :type: str
        """

        self._name = name

    @property
    def user_login_time(self):
        """
        Gets the user_login_time of this IamIdpReference.
        Represents the last login session details for each logged in user of this IdP. 

        :return: The user_login_time of this IamIdpReference.
        :rtype: list[IamUserLoginTimeRef]
        """
        return self._user_login_time

    @user_login_time.setter
    def user_login_time(self, user_login_time):
        """
        Sets the user_login_time of this IamIdpReference.
        Represents the last login session details for each logged in user of this IdP. 

        :param user_login_time: The user_login_time of this IamIdpReference.
        :type: list[IamUserLoginTimeRef]
        """

        self._user_login_time = user_login_time

    @property
    def user_preferences(self):
        """
        Gets the user_preferences of this IamIdpReference.
        Represents the UI preference object for each user logged in through this IdP. 

        :return: The user_preferences of this IamIdpReference.
        :rtype: list[IamUserPreferenceRef]
        """
        return self._user_preferences

    @user_preferences.setter
    def user_preferences(self, user_preferences):
        """
        Sets the user_preferences of this IamIdpReference.
        Represents the UI preference object for each user logged in through this IdP. 

        :param user_preferences: The user_preferences of this IamIdpReference.
        :type: list[IamUserPreferenceRef]
        """

        self._user_preferences = user_preferences

    @property
    def usergroups(self):
        """
        Gets the usergroups of this IamIdpReference.
        User groups added in an IdP. User group provides a way to configure permission assignment for a group of users based on IdP attributes received after authentication. 

        :return: The usergroups of this IamIdpReference.
        :rtype: list[IamUserGroupRef]
        """
        return self._usergroups

    @usergroups.setter
    def usergroups(self, usergroups):
        """
        Sets the usergroups of this IamIdpReference.
        User groups added in an IdP. User group provides a way to configure permission assignment for a group of users based on IdP attributes received after authentication. 

        :param usergroups: The usergroups of this IamIdpReference.
        :type: list[IamUserGroupRef]
        """

        self._usergroups = usergroups

    @property
    def users(self):
        """
        Gets the users of this IamIdpReference.
        Added or logged in users of an IdP who can access an Intersight account. 

        :return: The users of this IamIdpReference.
        :rtype: list[IamUserRef]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this IamIdpReference.
        Added or logged in users of an IdP who can access an Intersight account. 

        :param users: The users of this IamIdpReference.
        :type: list[IamUserRef]
        """

        self._users = users

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
        if not isinstance(other, IamIdpReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
