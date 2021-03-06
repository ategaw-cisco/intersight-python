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


class EquipmentTpm(object):
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
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'activation_status': 'str',
        'admin_state': 'str',
        'compute_board': 'ComputeBoardRef',
        'ownership': 'str',
        'presence': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'tpm_id': 'int',
        'version': 'str'
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
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'activation_status': 'ActivationStatus',
        'admin_state': 'AdminState',
        'compute_board': 'ComputeBoard',
        'ownership': 'Ownership',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice',
        'tpm_id': 'TpmId',
        'version': 'Version'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, activation_status=None, admin_state=None, compute_board=None, ownership=None, presence=None, registered_device=None, tpm_id=None, version=None):
        """
        EquipmentTpm - a model defined in Swagger
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
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._activation_status = None
        self._admin_state = None
        self._compute_board = None
        self._ownership = None
        self._presence = None
        self._registered_device = None
        self._tpm_id = None
        self._version = None

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
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if activation_status is not None:
          self.activation_status = activation_status
        if admin_state is not None:
          self.admin_state = admin_state
        if compute_board is not None:
          self.compute_board = compute_board
        if ownership is not None:
          self.ownership = ownership
        if presence is not None:
          self.presence = presence
        if registered_device is not None:
          self.registered_device = registered_device
        if tpm_id is not None:
          self.tpm_id = tpm_id
        if version is not None:
          self.version = version

    @property
    def account_moid(self):
        """
        Gets the account_moid of this EquipmentTpm.
        The Account ID for this managed object.  

        :return: The account_moid of this EquipmentTpm.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this EquipmentTpm.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this EquipmentTpm.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this EquipmentTpm.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this EquipmentTpm.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this EquipmentTpm.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this EquipmentTpm.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this EquipmentTpm.
        The time when this managed object was created.  

        :return: The create_time of this EquipmentTpm.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this EquipmentTpm.
        The time when this managed object was created.  

        :param create_time: The create_time of this EquipmentTpm.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this EquipmentTpm.
        The time when this managed object was last modified.  

        :return: The mod_time of this EquipmentTpm.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this EquipmentTpm.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this EquipmentTpm.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this EquipmentTpm.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this EquipmentTpm.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this EquipmentTpm.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this EquipmentTpm.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this EquipmentTpm.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this EquipmentTpm.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this EquipmentTpm.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this EquipmentTpm.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this EquipmentTpm.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this EquipmentTpm.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this EquipmentTpm.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this EquipmentTpm.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this EquipmentTpm.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this EquipmentTpm.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this EquipmentTpm.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this EquipmentTpm.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this EquipmentTpm.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this EquipmentTpm.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EquipmentTpm.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this EquipmentTpm.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this EquipmentTpm.
        The versioning info for this managed object   

        :return: The version_context of this EquipmentTpm.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this EquipmentTpm.
        The versioning info for this managed object   

        :param version_context: The version_context of this EquipmentTpm.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this EquipmentTpm.

        :return: The device_mo_id of this EquipmentTpm.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this EquipmentTpm.

        :param device_mo_id: The device_mo_id of this EquipmentTpm.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this EquipmentTpm.

        :return: The dn of this EquipmentTpm.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this EquipmentTpm.

        :param dn: The dn of this EquipmentTpm.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this EquipmentTpm.

        :return: The rn of this EquipmentTpm.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this EquipmentTpm.

        :param rn: The rn of this EquipmentTpm.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this EquipmentTpm.

        :return: The model of this EquipmentTpm.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this EquipmentTpm.

        :param model: The model of this EquipmentTpm.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this EquipmentTpm.

        :return: The revision of this EquipmentTpm.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this EquipmentTpm.

        :param revision: The revision of this EquipmentTpm.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this EquipmentTpm.

        :return: The serial of this EquipmentTpm.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this EquipmentTpm.

        :param serial: The serial of this EquipmentTpm.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this EquipmentTpm.

        :return: The vendor of this EquipmentTpm.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this EquipmentTpm.

        :param vendor: The vendor of this EquipmentTpm.
        :type: str
        """

        self._vendor = vendor

    @property
    def activation_status(self):
        """
        Gets the activation_status of this EquipmentTpm.

        :return: The activation_status of this EquipmentTpm.
        :rtype: str
        """
        return self._activation_status

    @activation_status.setter
    def activation_status(self, activation_status):
        """
        Sets the activation_status of this EquipmentTpm.

        :param activation_status: The activation_status of this EquipmentTpm.
        :type: str
        """

        self._activation_status = activation_status

    @property
    def admin_state(self):
        """
        Gets the admin_state of this EquipmentTpm.

        :return: The admin_state of this EquipmentTpm.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """
        Sets the admin_state of this EquipmentTpm.

        :param admin_state: The admin_state of this EquipmentTpm.
        :type: str
        """

        self._admin_state = admin_state

    @property
    def compute_board(self):
        """
        Gets the compute_board of this EquipmentTpm.

        :return: The compute_board of this EquipmentTpm.
        :rtype: ComputeBoardRef
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """
        Sets the compute_board of this EquipmentTpm.

        :param compute_board: The compute_board of this EquipmentTpm.
        :type: ComputeBoardRef
        """

        self._compute_board = compute_board

    @property
    def ownership(self):
        """
        Gets the ownership of this EquipmentTpm.

        :return: The ownership of this EquipmentTpm.
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """
        Sets the ownership of this EquipmentTpm.

        :param ownership: The ownership of this EquipmentTpm.
        :type: str
        """

        self._ownership = ownership

    @property
    def presence(self):
        """
        Gets the presence of this EquipmentTpm.

        :return: The presence of this EquipmentTpm.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this EquipmentTpm.

        :param presence: The presence of this EquipmentTpm.
        :type: str
        """

        self._presence = presence

    @property
    def registered_device(self):
        """
        Gets the registered_device of this EquipmentTpm.

        :return: The registered_device of this EquipmentTpm.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this EquipmentTpm.

        :param registered_device: The registered_device of this EquipmentTpm.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def tpm_id(self):
        """
        Gets the tpm_id of this EquipmentTpm.

        :return: The tpm_id of this EquipmentTpm.
        :rtype: int
        """
        return self._tpm_id

    @tpm_id.setter
    def tpm_id(self, tpm_id):
        """
        Sets the tpm_id of this EquipmentTpm.

        :param tpm_id: The tpm_id of this EquipmentTpm.
        :type: int
        """

        self._tpm_id = tpm_id

    @property
    def version(self):
        """
        Gets the version of this EquipmentTpm.

        :return: The version of this EquipmentTpm.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this EquipmentTpm.

        :param version: The version of this EquipmentTpm.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, EquipmentTpm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
