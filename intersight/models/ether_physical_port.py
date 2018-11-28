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


class EtherPhysicalPort(object):
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
        'oper_state': 'str',
        'role': 'str',
        'mac_address': 'str',
        'port_group': 'PortGroupRef',
        'port_sub_group': 'PortSubGroupRef',
        'registered_device': 'AssetDeviceRegistrationRef',
        'transceiver_type': 'str'
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
        'oper_state': 'OperState',
        'role': 'Role',
        'mac_address': 'MacAddress',
        'port_group': 'PortGroup',
        'port_sub_group': 'PortSubGroup',
        'registered_device': 'RegisteredDevice',
        'transceiver_type': 'TransceiverType'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, oper_state=None, role=None, mac_address=None, port_group=None, port_sub_group=None, registered_device=None, transceiver_type=None):
        """
        EtherPhysicalPort - a model defined in Swagger
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
        self._oper_state = None
        self._role = None
        self._mac_address = None
        self._port_group = None
        self._port_sub_group = None
        self._registered_device = None
        self._transceiver_type = None

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
        if oper_state is not None:
          self.oper_state = oper_state
        if role is not None:
          self.role = role
        if mac_address is not None:
          self.mac_address = mac_address
        if port_group is not None:
          self.port_group = port_group
        if port_sub_group is not None:
          self.port_sub_group = port_sub_group
        if registered_device is not None:
          self.registered_device = registered_device
        if transceiver_type is not None:
          self.transceiver_type = transceiver_type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this EtherPhysicalPort.
        The Account ID for this managed object.  

        :return: The account_moid of this EtherPhysicalPort.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this EtherPhysicalPort.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this EtherPhysicalPort.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this EtherPhysicalPort.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this EtherPhysicalPort.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this EtherPhysicalPort.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this EtherPhysicalPort.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this EtherPhysicalPort.
        The time when this managed object was created.  

        :return: The create_time of this EtherPhysicalPort.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this EtherPhysicalPort.
        The time when this managed object was created.  

        :param create_time: The create_time of this EtherPhysicalPort.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this EtherPhysicalPort.
        The time when this managed object was last modified.  

        :return: The mod_time of this EtherPhysicalPort.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this EtherPhysicalPort.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this EtherPhysicalPort.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this EtherPhysicalPort.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this EtherPhysicalPort.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this EtherPhysicalPort.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this EtherPhysicalPort.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this EtherPhysicalPort.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this EtherPhysicalPort.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this EtherPhysicalPort.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this EtherPhysicalPort.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this EtherPhysicalPort.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this EtherPhysicalPort.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this EtherPhysicalPort.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this EtherPhysicalPort.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this EtherPhysicalPort.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this EtherPhysicalPort.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this EtherPhysicalPort.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this EtherPhysicalPort.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this EtherPhysicalPort.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this EtherPhysicalPort.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EtherPhysicalPort.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this EtherPhysicalPort.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this EtherPhysicalPort.
        The versioning info for this managed object   

        :return: The version_context of this EtherPhysicalPort.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this EtherPhysicalPort.
        The versioning info for this managed object   

        :param version_context: The version_context of this EtherPhysicalPort.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this EtherPhysicalPort.

        :return: The device_mo_id of this EtherPhysicalPort.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this EtherPhysicalPort.

        :param device_mo_id: The device_mo_id of this EtherPhysicalPort.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this EtherPhysicalPort.

        :return: The dn of this EtherPhysicalPort.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this EtherPhysicalPort.

        :param dn: The dn of this EtherPhysicalPort.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this EtherPhysicalPort.

        :return: The rn of this EtherPhysicalPort.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this EtherPhysicalPort.

        :param rn: The rn of this EtherPhysicalPort.
        :type: str
        """

        self._rn = rn

    @property
    def oper_state(self):
        """
        Gets the oper_state of this EtherPhysicalPort.

        :return: The oper_state of this EtherPhysicalPort.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this EtherPhysicalPort.

        :param oper_state: The oper_state of this EtherPhysicalPort.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def role(self):
        """
        Gets the role of this EtherPhysicalPort.

        :return: The role of this EtherPhysicalPort.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this EtherPhysicalPort.

        :param role: The role of this EtherPhysicalPort.
        :type: str
        """

        self._role = role

    @property
    def mac_address(self):
        """
        Gets the mac_address of this EtherPhysicalPort.

        :return: The mac_address of this EtherPhysicalPort.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this EtherPhysicalPort.

        :param mac_address: The mac_address of this EtherPhysicalPort.
        :type: str
        """

        self._mac_address = mac_address

    @property
    def port_group(self):
        """
        Gets the port_group of this EtherPhysicalPort.

        :return: The port_group of this EtherPhysicalPort.
        :rtype: PortGroupRef
        """
        return self._port_group

    @port_group.setter
    def port_group(self, port_group):
        """
        Sets the port_group of this EtherPhysicalPort.

        :param port_group: The port_group of this EtherPhysicalPort.
        :type: PortGroupRef
        """

        self._port_group = port_group

    @property
    def port_sub_group(self):
        """
        Gets the port_sub_group of this EtherPhysicalPort.

        :return: The port_sub_group of this EtherPhysicalPort.
        :rtype: PortSubGroupRef
        """
        return self._port_sub_group

    @port_sub_group.setter
    def port_sub_group(self, port_sub_group):
        """
        Sets the port_sub_group of this EtherPhysicalPort.

        :param port_sub_group: The port_sub_group of this EtherPhysicalPort.
        :type: PortSubGroupRef
        """

        self._port_sub_group = port_sub_group

    @property
    def registered_device(self):
        """
        Gets the registered_device of this EtherPhysicalPort.

        :return: The registered_device of this EtherPhysicalPort.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this EtherPhysicalPort.

        :param registered_device: The registered_device of this EtherPhysicalPort.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def transceiver_type(self):
        """
        Gets the transceiver_type of this EtherPhysicalPort.

        :return: The transceiver_type of this EtherPhysicalPort.
        :rtype: str
        """
        return self._transceiver_type

    @transceiver_type.setter
    def transceiver_type(self, transceiver_type):
        """
        Sets the transceiver_type of this EtherPhysicalPort.

        :param transceiver_type: The transceiver_type of this EtherPhysicalPort.
        :type: str
        """

        self._transceiver_type = transceiver_type

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
        if not isinstance(other, EtherPhysicalPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
