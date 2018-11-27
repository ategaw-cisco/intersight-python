# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-260
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TestcryptReadOnlyUser(object):
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
        'rouser': 'list[TestcryptUser]'
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
        'rouser': 'Rouser'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, account=None, rouser=None):
        """
        TestcryptReadOnlyUser - a model defined in Swagger
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
        self._rouser = None

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
        if rouser is not None:
          self.rouser = rouser

    @property
    def account_moid(self):
        """
        Gets the account_moid of this TestcryptReadOnlyUser.
        The Account ID for this managed object.  

        :return: The account_moid of this TestcryptReadOnlyUser.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this TestcryptReadOnlyUser.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this TestcryptReadOnlyUser.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this TestcryptReadOnlyUser.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this TestcryptReadOnlyUser.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this TestcryptReadOnlyUser.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this TestcryptReadOnlyUser.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this TestcryptReadOnlyUser.
        The time when this managed object was created.  

        :return: The create_time of this TestcryptReadOnlyUser.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this TestcryptReadOnlyUser.
        The time when this managed object was created.  

        :param create_time: The create_time of this TestcryptReadOnlyUser.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this TestcryptReadOnlyUser.
        The time when this managed object was last modified.  

        :return: The mod_time of this TestcryptReadOnlyUser.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this TestcryptReadOnlyUser.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this TestcryptReadOnlyUser.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this TestcryptReadOnlyUser.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this TestcryptReadOnlyUser.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this TestcryptReadOnlyUser.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this TestcryptReadOnlyUser.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this TestcryptReadOnlyUser.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this TestcryptReadOnlyUser.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this TestcryptReadOnlyUser.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this TestcryptReadOnlyUser.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this TestcryptReadOnlyUser.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this TestcryptReadOnlyUser.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this TestcryptReadOnlyUser.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this TestcryptReadOnlyUser.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this TestcryptReadOnlyUser.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this TestcryptReadOnlyUser.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this TestcryptReadOnlyUser.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this TestcryptReadOnlyUser.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this TestcryptReadOnlyUser.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this TestcryptReadOnlyUser.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TestcryptReadOnlyUser.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this TestcryptReadOnlyUser.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this TestcryptReadOnlyUser.
        The versioning info for this managed object   

        :return: The version_context of this TestcryptReadOnlyUser.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this TestcryptReadOnlyUser.
        The versioning info for this managed object   

        :param version_context: The version_context of this TestcryptReadOnlyUser.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this TestcryptReadOnlyUser.

        :return: The account of this TestcryptReadOnlyUser.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this TestcryptReadOnlyUser.

        :param account: The account of this TestcryptReadOnlyUser.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def rouser(self):
        """
        Gets the rouser of this TestcryptReadOnlyUser.

        :return: The rouser of this TestcryptReadOnlyUser.
        :rtype: list[TestcryptUser]
        """
        return self._rouser

    @rouser.setter
    def rouser(self, rouser):
        """
        Sets the rouser of this TestcryptReadOnlyUser.

        :param rouser: The rouser of this TestcryptReadOnlyUser.
        :type: list[TestcryptUser]
        """

        self._rouser = rouser

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
        if not isinstance(other, TestcryptReadOnlyUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
