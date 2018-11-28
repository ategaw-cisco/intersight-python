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


class IamPrivilege(object):
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
        'method': 'str',
        'name': 'str',
        'rest_path': 'str',
        'system': 'IamSystemRef'
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
        'method': 'Method',
        'name': 'Name',
        'rest_path': 'RestPath',
        'system': 'System'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, account=None, method=None, name=None, rest_path=None, system=None):
        """
        IamPrivilege - a model defined in Swagger
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
        self._method = None
        self._name = None
        self._rest_path = None
        self._system = None

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
        if method is not None:
          self.method = method
        if name is not None:
          self.name = name
        if rest_path is not None:
          self.rest_path = rest_path
        if system is not None:
          self.system = system

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamPrivilege.
        The Account ID for this managed object.  

        :return: The account_moid of this IamPrivilege.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamPrivilege.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamPrivilege.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamPrivilege.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamPrivilege.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamPrivilege.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamPrivilege.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamPrivilege.
        The time when this managed object was created.  

        :return: The create_time of this IamPrivilege.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamPrivilege.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamPrivilege.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamPrivilege.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamPrivilege.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamPrivilege.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamPrivilege.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamPrivilege.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamPrivilege.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamPrivilege.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamPrivilege.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamPrivilege.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamPrivilege.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamPrivilege.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamPrivilege.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamPrivilege.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamPrivilege.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamPrivilege.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamPrivilege.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamPrivilege.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamPrivilege.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamPrivilege.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamPrivilege.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamPrivilege.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamPrivilege.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamPrivilege.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamPrivilege.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamPrivilege.
        The versioning info for this managed object   

        :return: The version_context of this IamPrivilege.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamPrivilege.
        The versioning info for this managed object   

        :param version_context: The version_context of this IamPrivilege.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this IamPrivilege.

        :return: The account of this IamPrivilege.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this IamPrivilege.

        :param account: The account of this IamPrivilege.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def method(self):
        """
        Gets the method of this IamPrivilege.
        Represents the API method on the rest resource corresponding to privilege. For example READ, CREATE, UPDATE etc.  

        :return: The method of this IamPrivilege.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this IamPrivilege.
        Represents the API method on the rest resource corresponding to privilege. For example READ, CREATE, UPDATE etc.  

        :param method: The method of this IamPrivilege.
        :type: str
        """

        self._method = method

    @property
    def name(self):
        """
        Gets the name of this IamPrivilege.
        Name of the privilege.   

        :return: The name of this IamPrivilege.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamPrivilege.
        Name of the privilege.   

        :param name: The name of this IamPrivilege.
        :type: str
        """

        self._name = name

    @property
    def rest_path(self):
        """
        Gets the rest_path of this IamPrivilege.
        Represents the rest path of the resource corresponding to this privilege. For example /v1/iam/Accounts, /v1/iam/Sessions etc.    

        :return: The rest_path of this IamPrivilege.
        :rtype: str
        """
        return self._rest_path

    @rest_path.setter
    def rest_path(self, rest_path):
        """
        Sets the rest_path of this IamPrivilege.
        Represents the rest path of the resource corresponding to this privilege. For example /v1/iam/Accounts, /v1/iam/Sessions etc.    

        :param rest_path: The rest_path of this IamPrivilege.
        :type: str
        """

        self._rest_path = rest_path

    @property
    def system(self):
        """
        Gets the system of this IamPrivilege.

        :return: The system of this IamPrivilege.
        :rtype: IamSystemRef
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this IamPrivilege.

        :param system: The system of this IamPrivilege.
        :type: IamSystemRef
        """

        self._system = system

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
        if not isinstance(other, IamPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
