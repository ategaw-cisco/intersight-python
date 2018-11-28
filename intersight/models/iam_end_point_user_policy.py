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


class IamEndPointUserPolicy(object):
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
        'end_point_user_roles': 'list[IamEndPointUserRoleRef]',
        'organization': 'IamAccountRef',
        'password_properties': 'IamEndPointPasswordProperties',
        'profiles': 'list[PolicyAbstractConfigProfileRef]'
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
        'end_point_user_roles': 'EndPointUserRoles',
        'organization': 'Organization',
        'password_properties': 'PasswordProperties',
        'profiles': 'Profiles'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, end_point_user_roles=None, organization=None, password_properties=None, profiles=None):
        """
        IamEndPointUserPolicy - a model defined in Swagger
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
        self._end_point_user_roles = None
        self._organization = None
        self._password_properties = None
        self._profiles = None

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
        if end_point_user_roles is not None:
          self.end_point_user_roles = end_point_user_roles
        if organization is not None:
          self.organization = organization
        if password_properties is not None:
          self.password_properties = password_properties
        if profiles is not None:
          self.profiles = profiles

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamEndPointUserPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this IamEndPointUserPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamEndPointUserPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamEndPointUserPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamEndPointUserPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamEndPointUserPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamEndPointUserPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamEndPointUserPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamEndPointUserPolicy.
        The time when this managed object was created.  

        :return: The create_time of this IamEndPointUserPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamEndPointUserPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamEndPointUserPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamEndPointUserPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamEndPointUserPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamEndPointUserPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamEndPointUserPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamEndPointUserPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamEndPointUserPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamEndPointUserPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamEndPointUserPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamEndPointUserPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamEndPointUserPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamEndPointUserPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamEndPointUserPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamEndPointUserPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamEndPointUserPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamEndPointUserPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamEndPointUserPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamEndPointUserPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamEndPointUserPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamEndPointUserPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamEndPointUserPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamEndPointUserPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamEndPointUserPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamEndPointUserPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamEndPointUserPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamEndPointUserPolicy.
        The versioning info for this managed object   

        :return: The version_context of this IamEndPointUserPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamEndPointUserPolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this IamEndPointUserPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this IamEndPointUserPolicy.
        Description of the policy.  

        :return: The description of this IamEndPointUserPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IamEndPointUserPolicy.
        Description of the policy.  

        :param description: The description of this IamEndPointUserPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this IamEndPointUserPolicy.
        Name of the policy.   

        :return: The name of this IamEndPointUserPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamEndPointUserPolicy.
        Name of the policy.   

        :param name: The name of this IamEndPointUserPolicy.
        :type: str
        """

        self._name = name

    @property
    def end_point_user_roles(self):
        """
        Gets the end_point_user_roles of this IamEndPointUserPolicy.
        Relationship to the collection of Endpoint user roles 

        :return: The end_point_user_roles of this IamEndPointUserPolicy.
        :rtype: list[IamEndPointUserRoleRef]
        """
        return self._end_point_user_roles

    @end_point_user_roles.setter
    def end_point_user_roles(self, end_point_user_roles):
        """
        Sets the end_point_user_roles of this IamEndPointUserPolicy.
        Relationship to the collection of Endpoint user roles 

        :param end_point_user_roles: The end_point_user_roles of this IamEndPointUserPolicy.
        :type: list[IamEndPointUserRoleRef]
        """

        self._end_point_user_roles = end_point_user_roles

    @property
    def organization(self):
        """
        Gets the organization of this IamEndPointUserPolicy.
        Organization 

        :return: The organization of this IamEndPointUserPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this IamEndPointUserPolicy.
        Organization 

        :param organization: The organization of this IamEndPointUserPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def password_properties(self):
        """
        Gets the password_properties of this IamEndPointUserPolicy.
        Set password properties for endpoint users   

        :return: The password_properties of this IamEndPointUserPolicy.
        :rtype: IamEndPointPasswordProperties
        """
        return self._password_properties

    @password_properties.setter
    def password_properties(self, password_properties):
        """
        Sets the password_properties of this IamEndPointUserPolicy.
        Set password properties for endpoint users   

        :param password_properties: The password_properties of this IamEndPointUserPolicy.
        :type: IamEndPointPasswordProperties
        """

        self._password_properties = password_properties

    @property
    def profiles(self):
        """
        Gets the profiles of this IamEndPointUserPolicy.
        Relationship to the server profile object 

        :return: The profiles of this IamEndPointUserPolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this IamEndPointUserPolicy.
        Relationship to the server profile object 

        :param profiles: The profiles of this IamEndPointUserPolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

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
        if not isinstance(other, IamEndPointUserPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
