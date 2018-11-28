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


class FaultInstance(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'acknowledged': 'str',
        'affected_dn': 'str',
        'affected_mo_id': 'str',
        'affected_mo_type': 'str',
        'ancestor_mo_id': 'str',
        'ancestor_mo_type': 'str',
        'code': 'str',
        'creation_time': 'str',
        'description': 'str',
        'last_transition_time': 'str',
        'num_occurrences': 'int',
        'original_severity': 'str',
        'previous_severity': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'rule': 'str',
        'severity': 'str'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'acknowledged': 'Acknowledged',
        'affected_dn': 'AffectedDn',
        'affected_mo_id': 'AffectedMoId',
        'affected_mo_type': 'AffectedMoType',
        'ancestor_mo_id': 'AncestorMoId',
        'ancestor_mo_type': 'AncestorMoType',
        'code': 'Code',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'last_transition_time': 'LastTransitionTime',
        'num_occurrences': 'NumOccurrences',
        'original_severity': 'OriginalSeverity',
        'previous_severity': 'PreviousSeverity',
        'registered_device': 'RegisteredDevice',
        'rule': 'Rule',
        'severity': 'Severity'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, acknowledged=None, affected_dn=None, affected_mo_id=None, affected_mo_type=None, ancestor_mo_id=None, ancestor_mo_type=None, code=None, creation_time=None, description=None, last_transition_time=None, num_occurrences=None, original_severity=None, previous_severity=None, registered_device=None, rule=None, severity=None):
        """
        FaultInstance - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._acknowledged = None
        self._affected_dn = None
        self._affected_mo_id = None
        self._affected_mo_type = None
        self._ancestor_mo_id = None
        self._ancestor_mo_type = None
        self._code = None
        self._creation_time = None
        self._description = None
        self._last_transition_time = None
        self._num_occurrences = None
        self._original_severity = None
        self._previous_severity = None
        self._registered_device = None
        self._rule = None
        self._severity = None

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
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if acknowledged is not None:
          self.acknowledged = acknowledged
        if affected_dn is not None:
          self.affected_dn = affected_dn
        if affected_mo_id is not None:
          self.affected_mo_id = affected_mo_id
        if affected_mo_type is not None:
          self.affected_mo_type = affected_mo_type
        if ancestor_mo_id is not None:
          self.ancestor_mo_id = ancestor_mo_id
        if ancestor_mo_type is not None:
          self.ancestor_mo_type = ancestor_mo_type
        if code is not None:
          self.code = code
        if creation_time is not None:
          self.creation_time = creation_time
        if description is not None:
          self.description = description
        if last_transition_time is not None:
          self.last_transition_time = last_transition_time
        if num_occurrences is not None:
          self.num_occurrences = num_occurrences
        if original_severity is not None:
          self.original_severity = original_severity
        if previous_severity is not None:
          self.previous_severity = previous_severity
        if registered_device is not None:
          self.registered_device = registered_device
        if rule is not None:
          self.rule = rule
        if severity is not None:
          self.severity = severity

    @property
    def account_moid(self):
        """
        Gets the account_moid of this FaultInstance.
        The Account ID for this managed object.  

        :return: The account_moid of this FaultInstance.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this FaultInstance.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this FaultInstance.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this FaultInstance.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this FaultInstance.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this FaultInstance.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this FaultInstance.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this FaultInstance.
        The time when this managed object was created.  

        :return: The create_time of this FaultInstance.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this FaultInstance.
        The time when this managed object was created.  

        :param create_time: The create_time of this FaultInstance.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this FaultInstance.
        The time when this managed object was last modified.  

        :return: The mod_time of this FaultInstance.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this FaultInstance.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this FaultInstance.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this FaultInstance.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this FaultInstance.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this FaultInstance.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this FaultInstance.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this FaultInstance.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this FaultInstance.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this FaultInstance.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this FaultInstance.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this FaultInstance.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this FaultInstance.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this FaultInstance.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this FaultInstance.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this FaultInstance.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this FaultInstance.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this FaultInstance.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this FaultInstance.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this FaultInstance.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this FaultInstance.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this FaultInstance.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this FaultInstance.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this FaultInstance.
        The versioning info for this managed object   

        :return: The version_context of this FaultInstance.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this FaultInstance.
        The versioning info for this managed object   

        :param version_context: The version_context of this FaultInstance.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this FaultInstance.

        :return: The device_mo_id of this FaultInstance.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this FaultInstance.

        :param device_mo_id: The device_mo_id of this FaultInstance.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this FaultInstance.

        :return: The dn of this FaultInstance.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this FaultInstance.

        :param dn: The dn of this FaultInstance.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this FaultInstance.

        :return: The rn of this FaultInstance.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this FaultInstance.

        :param rn: The rn of this FaultInstance.
        :type: str
        """

        self._rn = rn

    @property
    def acknowledged(self):
        """
        Gets the acknowledged of this FaultInstance.

        :return: The acknowledged of this FaultInstance.
        :rtype: str
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, acknowledged):
        """
        Sets the acknowledged of this FaultInstance.

        :param acknowledged: The acknowledged of this FaultInstance.
        :type: str
        """

        self._acknowledged = acknowledged

    @property
    def affected_dn(self):
        """
        Gets the affected_dn of this FaultInstance.

        :return: The affected_dn of this FaultInstance.
        :rtype: str
        """
        return self._affected_dn

    @affected_dn.setter
    def affected_dn(self, affected_dn):
        """
        Sets the affected_dn of this FaultInstance.

        :param affected_dn: The affected_dn of this FaultInstance.
        :type: str
        """

        self._affected_dn = affected_dn

    @property
    def affected_mo_id(self):
        """
        Gets the affected_mo_id of this FaultInstance.

        :return: The affected_mo_id of this FaultInstance.
        :rtype: str
        """
        return self._affected_mo_id

    @affected_mo_id.setter
    def affected_mo_id(self, affected_mo_id):
        """
        Sets the affected_mo_id of this FaultInstance.

        :param affected_mo_id: The affected_mo_id of this FaultInstance.
        :type: str
        """

        self._affected_mo_id = affected_mo_id

    @property
    def affected_mo_type(self):
        """
        Gets the affected_mo_type of this FaultInstance.

        :return: The affected_mo_type of this FaultInstance.
        :rtype: str
        """
        return self._affected_mo_type

    @affected_mo_type.setter
    def affected_mo_type(self, affected_mo_type):
        """
        Sets the affected_mo_type of this FaultInstance.

        :param affected_mo_type: The affected_mo_type of this FaultInstance.
        :type: str
        """

        self._affected_mo_type = affected_mo_type

    @property
    def ancestor_mo_id(self):
        """
        Gets the ancestor_mo_id of this FaultInstance.

        :return: The ancestor_mo_id of this FaultInstance.
        :rtype: str
        """
        return self._ancestor_mo_id

    @ancestor_mo_id.setter
    def ancestor_mo_id(self, ancestor_mo_id):
        """
        Sets the ancestor_mo_id of this FaultInstance.

        :param ancestor_mo_id: The ancestor_mo_id of this FaultInstance.
        :type: str
        """

        self._ancestor_mo_id = ancestor_mo_id

    @property
    def ancestor_mo_type(self):
        """
        Gets the ancestor_mo_type of this FaultInstance.

        :return: The ancestor_mo_type of this FaultInstance.
        :rtype: str
        """
        return self._ancestor_mo_type

    @ancestor_mo_type.setter
    def ancestor_mo_type(self, ancestor_mo_type):
        """
        Sets the ancestor_mo_type of this FaultInstance.

        :param ancestor_mo_type: The ancestor_mo_type of this FaultInstance.
        :type: str
        """

        self._ancestor_mo_type = ancestor_mo_type

    @property
    def code(self):
        """
        Gets the code of this FaultInstance.

        :return: The code of this FaultInstance.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this FaultInstance.

        :param code: The code of this FaultInstance.
        :type: str
        """

        self._code = code

    @property
    def creation_time(self):
        """
        Gets the creation_time of this FaultInstance.

        :return: The creation_time of this FaultInstance.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this FaultInstance.

        :param creation_time: The creation_time of this FaultInstance.
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """
        Gets the description of this FaultInstance.

        :return: The description of this FaultInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FaultInstance.

        :param description: The description of this FaultInstance.
        :type: str
        """

        self._description = description

    @property
    def last_transition_time(self):
        """
        Gets the last_transition_time of this FaultInstance.

        :return: The last_transition_time of this FaultInstance.
        :rtype: str
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """
        Sets the last_transition_time of this FaultInstance.

        :param last_transition_time: The last_transition_time of this FaultInstance.
        :type: str
        """

        self._last_transition_time = last_transition_time

    @property
    def num_occurrences(self):
        """
        Gets the num_occurrences of this FaultInstance.

        :return: The num_occurrences of this FaultInstance.
        :rtype: int
        """
        return self._num_occurrences

    @num_occurrences.setter
    def num_occurrences(self, num_occurrences):
        """
        Sets the num_occurrences of this FaultInstance.

        :param num_occurrences: The num_occurrences of this FaultInstance.
        :type: int
        """

        self._num_occurrences = num_occurrences

    @property
    def original_severity(self):
        """
        Gets the original_severity of this FaultInstance.

        :return: The original_severity of this FaultInstance.
        :rtype: str
        """
        return self._original_severity

    @original_severity.setter
    def original_severity(self, original_severity):
        """
        Sets the original_severity of this FaultInstance.

        :param original_severity: The original_severity of this FaultInstance.
        :type: str
        """

        self._original_severity = original_severity

    @property
    def previous_severity(self):
        """
        Gets the previous_severity of this FaultInstance.

        :return: The previous_severity of this FaultInstance.
        :rtype: str
        """
        return self._previous_severity

    @previous_severity.setter
    def previous_severity(self, previous_severity):
        """
        Sets the previous_severity of this FaultInstance.

        :param previous_severity: The previous_severity of this FaultInstance.
        :type: str
        """

        self._previous_severity = previous_severity

    @property
    def registered_device(self):
        """
        Gets the registered_device of this FaultInstance.

        :return: The registered_device of this FaultInstance.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this FaultInstance.

        :param registered_device: The registered_device of this FaultInstance.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def rule(self):
        """
        Gets the rule of this FaultInstance.

        :return: The rule of this FaultInstance.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this FaultInstance.

        :param rule: The rule of this FaultInstance.
        :type: str
        """

        self._rule = rule

    @property
    def severity(self):
        """
        Gets the severity of this FaultInstance.

        :return: The severity of this FaultInstance.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this FaultInstance.

        :param severity: The severity of this FaultInstance.
        :type: str
        """

        self._severity = severity

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
        if not isinstance(other, FaultInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
