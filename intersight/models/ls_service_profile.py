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


class LsServiceProfile(object):
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
        'assign_state': 'str',
        'assoc_state': 'str',
        'associated_server': 'str',
        'config_state': 'str',
        'name': 'str',
        'oper_state': 'str',
        'registered_device': 'AssetDeviceRegistrationRef'
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
        'assign_state': 'AssignState',
        'assoc_state': 'AssocState',
        'associated_server': 'AssociatedServer',
        'config_state': 'ConfigState',
        'name': 'Name',
        'oper_state': 'OperState',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, assign_state=None, assoc_state=None, associated_server=None, config_state=None, name=None, oper_state=None, registered_device=None):
        """
        LsServiceProfile - a model defined in Swagger
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
        self._assign_state = None
        self._assoc_state = None
        self._associated_server = None
        self._config_state = None
        self._name = None
        self._oper_state = None
        self._registered_device = None

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
        if assign_state is not None:
          self.assign_state = assign_state
        if assoc_state is not None:
          self.assoc_state = assoc_state
        if associated_server is not None:
          self.associated_server = associated_server
        if config_state is not None:
          self.config_state = config_state
        if name is not None:
          self.name = name
        if oper_state is not None:
          self.oper_state = oper_state
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this LsServiceProfile.
        The Account ID for this managed object.  

        :return: The account_moid of this LsServiceProfile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this LsServiceProfile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this LsServiceProfile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this LsServiceProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this LsServiceProfile.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this LsServiceProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this LsServiceProfile.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this LsServiceProfile.
        The time when this managed object was created.  

        :return: The create_time of this LsServiceProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this LsServiceProfile.
        The time when this managed object was created.  

        :param create_time: The create_time of this LsServiceProfile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this LsServiceProfile.
        The time when this managed object was last modified.  

        :return: The mod_time of this LsServiceProfile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this LsServiceProfile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this LsServiceProfile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this LsServiceProfile.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this LsServiceProfile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this LsServiceProfile.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this LsServiceProfile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this LsServiceProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this LsServiceProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this LsServiceProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this LsServiceProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this LsServiceProfile.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this LsServiceProfile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this LsServiceProfile.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this LsServiceProfile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this LsServiceProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this LsServiceProfile.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this LsServiceProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this LsServiceProfile.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this LsServiceProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this LsServiceProfile.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this LsServiceProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this LsServiceProfile.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this LsServiceProfile.
        The versioning info for this managed object   

        :return: The version_context of this LsServiceProfile.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this LsServiceProfile.
        The versioning info for this managed object   

        :param version_context: The version_context of this LsServiceProfile.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this LsServiceProfile.

        :return: The device_mo_id of this LsServiceProfile.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this LsServiceProfile.

        :param device_mo_id: The device_mo_id of this LsServiceProfile.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this LsServiceProfile.

        :return: The dn of this LsServiceProfile.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this LsServiceProfile.

        :param dn: The dn of this LsServiceProfile.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this LsServiceProfile.

        :return: The rn of this LsServiceProfile.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this LsServiceProfile.

        :param rn: The rn of this LsServiceProfile.
        :type: str
        """

        self._rn = rn

    @property
    def assign_state(self):
        """
        Gets the assign_state of this LsServiceProfile.

        :return: The assign_state of this LsServiceProfile.
        :rtype: str
        """
        return self._assign_state

    @assign_state.setter
    def assign_state(self, assign_state):
        """
        Sets the assign_state of this LsServiceProfile.

        :param assign_state: The assign_state of this LsServiceProfile.
        :type: str
        """

        self._assign_state = assign_state

    @property
    def assoc_state(self):
        """
        Gets the assoc_state of this LsServiceProfile.

        :return: The assoc_state of this LsServiceProfile.
        :rtype: str
        """
        return self._assoc_state

    @assoc_state.setter
    def assoc_state(self, assoc_state):
        """
        Sets the assoc_state of this LsServiceProfile.

        :param assoc_state: The assoc_state of this LsServiceProfile.
        :type: str
        """

        self._assoc_state = assoc_state

    @property
    def associated_server(self):
        """
        Gets the associated_server of this LsServiceProfile.

        :return: The associated_server of this LsServiceProfile.
        :rtype: str
        """
        return self._associated_server

    @associated_server.setter
    def associated_server(self, associated_server):
        """
        Sets the associated_server of this LsServiceProfile.

        :param associated_server: The associated_server of this LsServiceProfile.
        :type: str
        """

        self._associated_server = associated_server

    @property
    def config_state(self):
        """
        Gets the config_state of this LsServiceProfile.

        :return: The config_state of this LsServiceProfile.
        :rtype: str
        """
        return self._config_state

    @config_state.setter
    def config_state(self, config_state):
        """
        Sets the config_state of this LsServiceProfile.

        :param config_state: The config_state of this LsServiceProfile.
        :type: str
        """

        self._config_state = config_state

    @property
    def name(self):
        """
        Gets the name of this LsServiceProfile.

        :return: The name of this LsServiceProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LsServiceProfile.

        :param name: The name of this LsServiceProfile.
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """
        Gets the oper_state of this LsServiceProfile.

        :return: The oper_state of this LsServiceProfile.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this LsServiceProfile.

        :param oper_state: The oper_state of this LsServiceProfile.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def registered_device(self):
        """
        Gets the registered_device of this LsServiceProfile.

        :return: The registered_device of this LsServiceProfile.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this LsServiceProfile.

        :param registered_device: The registered_device of this LsServiceProfile.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, LsServiceProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
