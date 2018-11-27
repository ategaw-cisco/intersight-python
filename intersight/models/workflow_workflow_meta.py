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


class WorkflowWorkflowMeta(object):
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
        'description': 'str',
        'input_parameters': 'list[str]',
        'name': 'str',
        'output_parameters': 'object',
        'schema_version': 'int',
        'src': 'str',
        'tasks': 'object',
        'type': 'str',
        'version': 'int',
        'wait_on_duplicate': 'bool'
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
        'description': 'Description',
        'input_parameters': 'InputParameters',
        'name': 'Name',
        'output_parameters': 'OutputParameters',
        'schema_version': 'SchemaVersion',
        'src': 'Src',
        'tasks': 'Tasks',
        'type': 'Type',
        'version': 'Version',
        'wait_on_duplicate': 'WaitOnDuplicate'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, account=None, description=None, input_parameters=None, name=None, output_parameters=None, schema_version=None, src=None, tasks=None, type='SystemDefined', version=None, wait_on_duplicate=None):
        """
        WorkflowWorkflowMeta - a model defined in Swagger
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
        self._description = None
        self._input_parameters = None
        self._name = None
        self._output_parameters = None
        self._schema_version = None
        self._src = None
        self._tasks = None
        self._type = None
        self._version = None
        self._wait_on_duplicate = None

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
        if description is not None:
          self.description = description
        if input_parameters is not None:
          self.input_parameters = input_parameters
        if name is not None:
          self.name = name
        if output_parameters is not None:
          self.output_parameters = output_parameters
        if schema_version is not None:
          self.schema_version = schema_version
        if src is not None:
          self.src = src
        if tasks is not None:
          self.tasks = tasks
        if type is not None:
          self.type = type
        if version is not None:
          self.version = version
        if wait_on_duplicate is not None:
          self.wait_on_duplicate = wait_on_duplicate

    @property
    def account_moid(self):
        """
        Gets the account_moid of this WorkflowWorkflowMeta.
        The Account ID for this managed object.  

        :return: The account_moid of this WorkflowWorkflowMeta.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this WorkflowWorkflowMeta.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this WorkflowWorkflowMeta.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this WorkflowWorkflowMeta.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this WorkflowWorkflowMeta.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this WorkflowWorkflowMeta.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this WorkflowWorkflowMeta.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this WorkflowWorkflowMeta.
        The time when this managed object was created.  

        :return: The create_time of this WorkflowWorkflowMeta.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this WorkflowWorkflowMeta.
        The time when this managed object was created.  

        :param create_time: The create_time of this WorkflowWorkflowMeta.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this WorkflowWorkflowMeta.
        The time when this managed object was last modified.  

        :return: The mod_time of this WorkflowWorkflowMeta.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this WorkflowWorkflowMeta.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this WorkflowWorkflowMeta.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this WorkflowWorkflowMeta.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this WorkflowWorkflowMeta.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this WorkflowWorkflowMeta.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this WorkflowWorkflowMeta.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowWorkflowMeta.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this WorkflowWorkflowMeta.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowWorkflowMeta.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this WorkflowWorkflowMeta.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this WorkflowWorkflowMeta.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this WorkflowWorkflowMeta.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this WorkflowWorkflowMeta.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this WorkflowWorkflowMeta.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this WorkflowWorkflowMeta.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this WorkflowWorkflowMeta.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this WorkflowWorkflowMeta.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this WorkflowWorkflowMeta.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this WorkflowWorkflowMeta.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this WorkflowWorkflowMeta.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this WorkflowWorkflowMeta.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this WorkflowWorkflowMeta.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this WorkflowWorkflowMeta.
        The versioning info for this managed object   

        :return: The version_context of this WorkflowWorkflowMeta.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this WorkflowWorkflowMeta.
        The versioning info for this managed object   

        :param version_context: The version_context of this WorkflowWorkflowMeta.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this WorkflowWorkflowMeta.
        The account creates the workflow meta 

        :return: The account of this WorkflowWorkflowMeta.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this WorkflowWorkflowMeta.
        The account creates the workflow meta 

        :param account: The account of this WorkflowWorkflowMeta.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def description(self):
        """
        Gets the description of this WorkflowWorkflowMeta.
        The workflow description  

        :return: The description of this WorkflowWorkflowMeta.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowWorkflowMeta.
        The workflow description  

        :param description: The description of this WorkflowWorkflowMeta.
        :type: str
        """

        self._description = description

    @property
    def input_parameters(self):
        """
        Gets the input_parameters of this WorkflowWorkflowMeta.
        The workflow input parameters  

        :return: The input_parameters of this WorkflowWorkflowMeta.
        :rtype: list[str]
        """
        return self._input_parameters

    @input_parameters.setter
    def input_parameters(self, input_parameters):
        """
        Sets the input_parameters of this WorkflowWorkflowMeta.
        The workflow input parameters  

        :param input_parameters: The input_parameters of this WorkflowWorkflowMeta.
        :type: list[str]
        """

        self._input_parameters = input_parameters

    @property
    def name(self):
        """
        Gets the name of this WorkflowWorkflowMeta.
        The workflow name  

        :return: The name of this WorkflowWorkflowMeta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowWorkflowMeta.
        The workflow name  

        :param name: The name of this WorkflowWorkflowMeta.
        :type: str
        """

        self._name = name

    @property
    def output_parameters(self):
        """
        Gets the output_parameters of this WorkflowWorkflowMeta.
        The workflow output parameters  

        :return: The output_parameters of this WorkflowWorkflowMeta.
        :rtype: object
        """
        return self._output_parameters

    @output_parameters.setter
    def output_parameters(self, output_parameters):
        """
        Sets the output_parameters of this WorkflowWorkflowMeta.
        The workflow output parameters  

        :param output_parameters: The output_parameters of this WorkflowWorkflowMeta.
        :type: object
        """

        self._output_parameters = output_parameters

    @property
    def schema_version(self):
        """
        Gets the schema_version of this WorkflowWorkflowMeta.
        The Conductor schema version that decides what attribute can be suported  

        :return: The schema_version of this WorkflowWorkflowMeta.
        :rtype: int
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """
        Sets the schema_version of this WorkflowWorkflowMeta.
        The Conductor schema version that decides what attribute can be suported  

        :param schema_version: The schema_version of this WorkflowWorkflowMeta.
        :type: int
        """

        self._schema_version = schema_version

    @property
    def src(self):
        """
        Gets the src of this WorkflowWorkflowMeta.
        The src is workflow owner service  

        :return: The src of this WorkflowWorkflowMeta.
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """
        Sets the src of this WorkflowWorkflowMeta.
        The src is workflow owner service  

        :param src: The src of this WorkflowWorkflowMeta.
        :type: str
        """

        self._src = src

    @property
    def tasks(self):
        """
        Gets the tasks of this WorkflowWorkflowMeta.
        The tasks contained inside of the workflow  

        :return: The tasks of this WorkflowWorkflowMeta.
        :rtype: object
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this WorkflowWorkflowMeta.
        The tasks contained inside of the workflow  

        :param tasks: The tasks of this WorkflowWorkflowMeta.
        :type: object
        """

        self._tasks = tasks

    @property
    def type(self):
        """
        Gets the type of this WorkflowWorkflowMeta.
        The type of workflow  

        :return: The type of this WorkflowWorkflowMeta.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WorkflowWorkflowMeta.
        The type of workflow  

        :param type: The type of this WorkflowWorkflowMeta.
        :type: str
        """
        allowed_values = ["SystemDefined", "UserDefined", "Dynamic"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version(self):
        """
        Gets the version of this WorkflowWorkflowMeta.
        The workflow version which indicate the workflow meta changes  

        :return: The version of this WorkflowWorkflowMeta.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this WorkflowWorkflowMeta.
        The workflow version which indicate the workflow meta changes  

        :param version: The version of this WorkflowWorkflowMeta.
        :type: int
        """

        self._version = version

    @property
    def wait_on_duplicate(self):
        """
        Gets the wait_on_duplicate of this WorkflowWorkflowMeta.
        This parameter decides if workflows will wait for a duplicate to finish before starting a new one   

        :return: The wait_on_duplicate of this WorkflowWorkflowMeta.
        :rtype: bool
        """
        return self._wait_on_duplicate

    @wait_on_duplicate.setter
    def wait_on_duplicate(self, wait_on_duplicate):
        """
        Sets the wait_on_duplicate of this WorkflowWorkflowMeta.
        This parameter decides if workflows will wait for a duplicate to finish before starting a new one   

        :param wait_on_duplicate: The wait_on_duplicate of this WorkflowWorkflowMeta.
        :type: bool
        """

        self._wait_on_duplicate = wait_on_duplicate

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
        if not isinstance(other, WorkflowWorkflowMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
