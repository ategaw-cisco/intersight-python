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


class PortSubGroup(object):
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
        'ethernet_ports': 'list[EtherPhysicalPortRef]',
        'port_group': 'PortGroupRef',
        'registered_device': 'AssetDeviceRegistrationRef',
        'transport': 'str'
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
        'ethernet_ports': 'EthernetPorts',
        'port_group': 'PortGroup',
        'registered_device': 'RegisteredDevice',
        'transport': 'Transport'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, ethernet_ports=None, port_group=None, registered_device=None, transport=None):
        """
        PortSubGroup - a model defined in Swagger
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
        self._ethernet_ports = None
        self._port_group = None
        self._registered_device = None
        self._transport = None

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
        if ethernet_ports is not None:
          self.ethernet_ports = ethernet_ports
        if port_group is not None:
          self.port_group = port_group
        if registered_device is not None:
          self.registered_device = registered_device
        if transport is not None:
          self.transport = transport

    @property
    def account_moid(self):
        """
        Gets the account_moid of this PortSubGroup.
        The Account ID for this managed object.  

        :return: The account_moid of this PortSubGroup.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this PortSubGroup.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this PortSubGroup.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this PortSubGroup.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this PortSubGroup.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this PortSubGroup.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this PortSubGroup.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this PortSubGroup.
        The time when this managed object was created.  

        :return: The create_time of this PortSubGroup.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this PortSubGroup.
        The time when this managed object was created.  

        :param create_time: The create_time of this PortSubGroup.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this PortSubGroup.
        The time when this managed object was last modified.  

        :return: The mod_time of this PortSubGroup.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this PortSubGroup.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this PortSubGroup.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this PortSubGroup.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this PortSubGroup.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this PortSubGroup.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this PortSubGroup.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this PortSubGroup.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this PortSubGroup.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this PortSubGroup.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this PortSubGroup.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this PortSubGroup.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this PortSubGroup.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this PortSubGroup.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this PortSubGroup.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this PortSubGroup.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this PortSubGroup.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this PortSubGroup.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this PortSubGroup.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this PortSubGroup.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this PortSubGroup.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this PortSubGroup.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this PortSubGroup.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this PortSubGroup.
        The versioning info for this managed object   

        :return: The version_context of this PortSubGroup.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this PortSubGroup.
        The versioning info for this managed object   

        :param version_context: The version_context of this PortSubGroup.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this PortSubGroup.

        :return: The device_mo_id of this PortSubGroup.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this PortSubGroup.

        :param device_mo_id: The device_mo_id of this PortSubGroup.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this PortSubGroup.

        :return: The dn of this PortSubGroup.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this PortSubGroup.

        :param dn: The dn of this PortSubGroup.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this PortSubGroup.

        :return: The rn of this PortSubGroup.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this PortSubGroup.

        :param rn: The rn of this PortSubGroup.
        :type: str
        """

        self._rn = rn

    @property
    def ethernet_ports(self):
        """
        Gets the ethernet_ports of this PortSubGroup.

        :return: The ethernet_ports of this PortSubGroup.
        :rtype: list[EtherPhysicalPortRef]
        """
        return self._ethernet_ports

    @ethernet_ports.setter
    def ethernet_ports(self, ethernet_ports):
        """
        Sets the ethernet_ports of this PortSubGroup.

        :param ethernet_ports: The ethernet_ports of this PortSubGroup.
        :type: list[EtherPhysicalPortRef]
        """

        self._ethernet_ports = ethernet_ports

    @property
    def port_group(self):
        """
        Gets the port_group of this PortSubGroup.

        :return: The port_group of this PortSubGroup.
        :rtype: PortGroupRef
        """
        return self._port_group

    @port_group.setter
    def port_group(self, port_group):
        """
        Sets the port_group of this PortSubGroup.

        :param port_group: The port_group of this PortSubGroup.
        :type: PortGroupRef
        """

        self._port_group = port_group

    @property
    def registered_device(self):
        """
        Gets the registered_device of this PortSubGroup.

        :return: The registered_device of this PortSubGroup.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this PortSubGroup.

        :param registered_device: The registered_device of this PortSubGroup.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def transport(self):
        """
        Gets the transport of this PortSubGroup.

        :return: The transport of this PortSubGroup.
        :rtype: str
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """
        Sets the transport of this PortSubGroup.

        :param transport: The transport of this PortSubGroup.
        :type: str
        """

        self._transport = transport

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
        if not isinstance(other, PortSubGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
