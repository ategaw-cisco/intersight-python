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


class HyperflexConfigResult(object):
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
        'config_stage': 'str',
        'config_state': 'str',
        'validation_state': 'str',
        'cluster_profile': 'HyperflexClusterProfileRef',
        'config_progress': 'str',
        'duration': 'str',
        'result_entries': 'list[HyperflexConfigResultEntryRef]',
        'start_time': 'str'
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
        'config_stage': 'ConfigStage',
        'config_state': 'ConfigState',
        'validation_state': 'ValidationState',
        'cluster_profile': 'ClusterProfile',
        'config_progress': 'ConfigProgress',
        'duration': 'Duration',
        'result_entries': 'ResultEntries',
        'start_time': 'StartTime'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, config_stage=None, config_state=None, validation_state=None, cluster_profile=None, config_progress=None, duration=None, result_entries=None, start_time=None):
        """
        HyperflexConfigResult - a model defined in Swagger
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
        self._config_stage = None
        self._config_state = None
        self._validation_state = None
        self._cluster_profile = None
        self._config_progress = None
        self._duration = None
        self._result_entries = None
        self._start_time = None

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
        if config_stage is not None:
          self.config_stage = config_stage
        if config_state is not None:
          self.config_state = config_state
        if validation_state is not None:
          self.validation_state = validation_state
        if cluster_profile is not None:
          self.cluster_profile = cluster_profile
        if config_progress is not None:
          self.config_progress = config_progress
        if duration is not None:
          self.duration = duration
        if result_entries is not None:
          self.result_entries = result_entries
        if start_time is not None:
          self.start_time = start_time

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexConfigResult.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexConfigResult.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexConfigResult.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexConfigResult.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexConfigResult.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexConfigResult.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexConfigResult.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexConfigResult.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexConfigResult.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexConfigResult.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexConfigResult.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexConfigResult.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexConfigResult.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexConfigResult.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexConfigResult.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexConfigResult.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexConfigResult.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexConfigResult.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexConfigResult.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexConfigResult.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexConfigResult.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexConfigResult.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexConfigResult.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexConfigResult.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexConfigResult.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexConfigResult.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexConfigResult.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexConfigResult.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexConfigResult.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexConfigResult.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexConfigResult.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexConfigResult.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexConfigResult.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexConfigResult.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexConfigResult.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexConfigResult.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexConfigResult.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexConfigResult.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexConfigResult.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexConfigResult.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def config_stage(self):
        """
        Gets the config_stage of this HyperflexConfigResult.
        The current running stage of the configuration or workflow.  

        :return: The config_stage of this HyperflexConfigResult.
        :rtype: str
        """
        return self._config_stage

    @config_stage.setter
    def config_stage(self, config_stage):
        """
        Sets the config_stage of this HyperflexConfigResult.
        The current running stage of the configuration or workflow.  

        :param config_stage: The config_stage of this HyperflexConfigResult.
        :type: str
        """

        self._config_stage = config_stage

    @property
    def config_state(self):
        """
        Gets the config_state of this HyperflexConfigResult.
        Indicates overall configuration state for applying the configuration to the end point Values  -- ok, ok-with-warning, errored  

        :return: The config_state of this HyperflexConfigResult.
        :rtype: str
        """
        return self._config_state

    @config_state.setter
    def config_state(self, config_state):
        """
        Sets the config_state of this HyperflexConfigResult.
        Indicates overall configuration state for applying the configuration to the end point Values  -- ok, ok-with-warning, errored  

        :param config_state: The config_state of this HyperflexConfigResult.
        :type: str
        """

        self._config_state = config_state

    @property
    def validation_state(self):
        """
        Gets the validation_state of this HyperflexConfigResult.
        Indicates overall state for logical model validation Values  -- ok, ok-with-warning, errored   

        :return: The validation_state of this HyperflexConfigResult.
        :rtype: str
        """
        return self._validation_state

    @validation_state.setter
    def validation_state(self, validation_state):
        """
        Sets the validation_state of this HyperflexConfigResult.
        Indicates overall state for logical model validation Values  -- ok, ok-with-warning, errored   

        :param validation_state: The validation_state of this HyperflexConfigResult.
        :type: str
        """

        self._validation_state = validation_state

    @property
    def cluster_profile(self):
        """
        Gets the cluster_profile of this HyperflexConfigResult.

        :return: The cluster_profile of this HyperflexConfigResult.
        :rtype: HyperflexClusterProfileRef
        """
        return self._cluster_profile

    @cluster_profile.setter
    def cluster_profile(self, cluster_profile):
        """
        Sets the cluster_profile of this HyperflexConfigResult.

        :param cluster_profile: The cluster_profile of this HyperflexConfigResult.
        :type: HyperflexClusterProfileRef
        """

        self._cluster_profile = cluster_profile

    @property
    def config_progress(self):
        """
        Gets the config_progress of this HyperflexConfigResult.
        The progress percentage of the running configuration or workflow  

        :return: The config_progress of this HyperflexConfigResult.
        :rtype: str
        """
        return self._config_progress

    @config_progress.setter
    def config_progress(self, config_progress):
        """
        Sets the config_progress of this HyperflexConfigResult.
        The progress percentage of the running configuration or workflow  

        :param config_progress: The config_progress of this HyperflexConfigResult.
        :type: str
        """

        self._config_progress = config_progress

    @property
    def duration(self):
        """
        Gets the duration of this HyperflexConfigResult.
        The duration of the running configuration or workflow  

        :return: The duration of this HyperflexConfigResult.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this HyperflexConfigResult.
        The duration of the running configuration or workflow  

        :param duration: The duration of this HyperflexConfigResult.
        :type: str
        """

        self._duration = duration

    @property
    def result_entries(self):
        """
        Gets the result_entries of this HyperflexConfigResult.
        Detailed result entries for both validation & configration. Each result entry can be error/warning/info messages and the context. 

        :return: The result_entries of this HyperflexConfigResult.
        :rtype: list[HyperflexConfigResultEntryRef]
        """
        return self._result_entries

    @result_entries.setter
    def result_entries(self, result_entries):
        """
        Sets the result_entries of this HyperflexConfigResult.
        Detailed result entries for both validation & configration. Each result entry can be error/warning/info messages and the context. 

        :param result_entries: The result_entries of this HyperflexConfigResult.
        :type: list[HyperflexConfigResultEntryRef]
        """

        self._result_entries = result_entries

    @property
    def start_time(self):
        """
        Gets the start_time of this HyperflexConfigResult.
        The start time of the configuration or workflow   

        :return: The start_time of this HyperflexConfigResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this HyperflexConfigResult.
        The start time of the configuration or workflow   

        :param start_time: The start_time of this HyperflexConfigResult.
        :type: str
        """

        self._start_time = start_time

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
        if not isinstance(other, HyperflexConfigResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
