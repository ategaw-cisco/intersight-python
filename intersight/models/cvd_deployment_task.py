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


class CvdDeploymentTask(object):
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
        'input_data': 'object',
        'organization': 'IamAccountRef',
        'result': 'object',
        'template': 'CvdTemplateRef'
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
        'input_data': 'InputData',
        'organization': 'Organization',
        'result': 'Result',
        'template': 'Template'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, input_data=None, organization=None, result=None, template=None):
        """
        CvdDeploymentTask - a model defined in Swagger
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
        self._input_data = None
        self._organization = None
        self._result = None
        self._template = None

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
        if input_data is not None:
          self.input_data = input_data
        if organization is not None:
          self.organization = organization
        if result is not None:
          self.result = result
        if template is not None:
          self.template = template

    @property
    def account_moid(self):
        """
        Gets the account_moid of this CvdDeploymentTask.
        The Account ID for this managed object.  

        :return: The account_moid of this CvdDeploymentTask.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this CvdDeploymentTask.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this CvdDeploymentTask.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this CvdDeploymentTask.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this CvdDeploymentTask.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this CvdDeploymentTask.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this CvdDeploymentTask.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this CvdDeploymentTask.
        The time when this managed object was created.  

        :return: The create_time of this CvdDeploymentTask.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this CvdDeploymentTask.
        The time when this managed object was created.  

        :param create_time: The create_time of this CvdDeploymentTask.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this CvdDeploymentTask.
        The time when this managed object was last modified.  

        :return: The mod_time of this CvdDeploymentTask.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this CvdDeploymentTask.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this CvdDeploymentTask.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this CvdDeploymentTask.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this CvdDeploymentTask.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this CvdDeploymentTask.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this CvdDeploymentTask.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this CvdDeploymentTask.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this CvdDeploymentTask.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this CvdDeploymentTask.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this CvdDeploymentTask.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this CvdDeploymentTask.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this CvdDeploymentTask.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this CvdDeploymentTask.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this CvdDeploymentTask.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this CvdDeploymentTask.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this CvdDeploymentTask.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this CvdDeploymentTask.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this CvdDeploymentTask.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this CvdDeploymentTask.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this CvdDeploymentTask.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CvdDeploymentTask.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this CvdDeploymentTask.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this CvdDeploymentTask.
        The versioning info for this managed object   

        :return: The version_context of this CvdDeploymentTask.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this CvdDeploymentTask.
        The versioning info for this managed object   

        :param version_context: The version_context of this CvdDeploymentTask.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def input_data(self):
        """
        Gets the input_data of this CvdDeploymentTask.
        Input data set to be provided to the deployment workflow  

        :return: The input_data of this CvdDeploymentTask.
        :rtype: object
        """
        return self._input_data

    @input_data.setter
    def input_data(self, input_data):
        """
        Sets the input_data of this CvdDeploymentTask.
        Input data set to be provided to the deployment workflow  

        :param input_data: The input_data of this CvdDeploymentTask.
        :type: object
        """

        self._input_data = input_data

    @property
    def organization(self):
        """
        Gets the organization of this CvdDeploymentTask.
        Organization 

        :return: The organization of this CvdDeploymentTask.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this CvdDeploymentTask.
        Organization 

        :param organization: The organization of this CvdDeploymentTask.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def result(self):
        """
        Gets the result of this CvdDeploymentTask.
        Result of the deployment operation   

        :return: The result of this CvdDeploymentTask.
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this CvdDeploymentTask.
        Result of the deployment operation   

        :param result: The result of this CvdDeploymentTask.
        :type: object
        """

        self._result = result

    @property
    def template(self):
        """
        Gets the template of this CvdDeploymentTask.
        eCVD instance for which the deployment task is being run 

        :return: The template of this CvdDeploymentTask.
        :rtype: CvdTemplateRef
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CvdDeploymentTask.
        eCVD instance for which the deployment task is being run 

        :param template: The template of this CvdDeploymentTask.
        :type: CvdTemplateRef
        """

        self._template = template

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
        if not isinstance(other, CvdDeploymentTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
