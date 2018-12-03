# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-265
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HyperflexServerFirmwareVersion(object):
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
        'app_catalog': 'HyperflexAppCatalogRef',
        'server_firmware_version_entries': 'list[HyperflexServerFirmwareVersionEntry]'
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
        'app_catalog': 'AppCatalog',
        'server_firmware_version_entries': 'ServerFirmwareVersionEntries'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, app_catalog=None, server_firmware_version_entries=None):
        """
        HyperflexServerFirmwareVersion - a model defined in Swagger
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
        self._app_catalog = None
        self._server_firmware_version_entries = None

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
        if app_catalog is not None:
          self.app_catalog = app_catalog
        if server_firmware_version_entries is not None:
          self.server_firmware_version_entries = server_firmware_version_entries

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexServerFirmwareVersion.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexServerFirmwareVersion.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexServerFirmwareVersion.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexServerFirmwareVersion.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexServerFirmwareVersion.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexServerFirmwareVersion.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexServerFirmwareVersion.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexServerFirmwareVersion.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexServerFirmwareVersion.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexServerFirmwareVersion.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexServerFirmwareVersion.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexServerFirmwareVersion.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexServerFirmwareVersion.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexServerFirmwareVersion.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexServerFirmwareVersion.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexServerFirmwareVersion.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexServerFirmwareVersion.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexServerFirmwareVersion.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexServerFirmwareVersion.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexServerFirmwareVersion.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexServerFirmwareVersion.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexServerFirmwareVersion.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexServerFirmwareVersion.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexServerFirmwareVersion.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexServerFirmwareVersion.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexServerFirmwareVersion.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexServerFirmwareVersion.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexServerFirmwareVersion.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexServerFirmwareVersion.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexServerFirmwareVersion.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexServerFirmwareVersion.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexServerFirmwareVersion.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexServerFirmwareVersion.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexServerFirmwareVersion.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexServerFirmwareVersion.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexServerFirmwareVersion.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexServerFirmwareVersion.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexServerFirmwareVersion.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexServerFirmwareVersion.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexServerFirmwareVersion.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def app_catalog(self):
        """
        Gets the app_catalog of this HyperflexServerFirmwareVersion.

        :return: The app_catalog of this HyperflexServerFirmwareVersion.
        :rtype: HyperflexAppCatalogRef
        """
        return self._app_catalog

    @app_catalog.setter
    def app_catalog(self, app_catalog):
        """
        Sets the app_catalog of this HyperflexServerFirmwareVersion.

        :param app_catalog: The app_catalog of this HyperflexServerFirmwareVersion.
        :type: HyperflexAppCatalogRef
        """

        self._app_catalog = app_catalog

    @property
    def server_firmware_version_entries(self):
        """
        Gets the server_firmware_version_entries of this HyperflexServerFirmwareVersion.
        Specifies server firmware bundle versions used for server components such as CIMC, adapters, BIOS, etc.   

        :return: The server_firmware_version_entries of this HyperflexServerFirmwareVersion.
        :rtype: list[HyperflexServerFirmwareVersionEntry]
        """
        return self._server_firmware_version_entries

    @server_firmware_version_entries.setter
    def server_firmware_version_entries(self, server_firmware_version_entries):
        """
        Sets the server_firmware_version_entries of this HyperflexServerFirmwareVersion.
        Specifies server firmware bundle versions used for server components such as CIMC, adapters, BIOS, etc.   

        :param server_firmware_version_entries: The server_firmware_version_entries of this HyperflexServerFirmwareVersion.
        :type: list[HyperflexServerFirmwareVersionEntry]
        """

        self._server_firmware_version_entries = server_firmware_version_entries

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
        if not isinstance(other, HyperflexServerFirmwareVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
