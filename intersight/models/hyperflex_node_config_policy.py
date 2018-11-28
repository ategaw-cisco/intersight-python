# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-261
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HyperflexNodeConfigPolicy(object):
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
        'cluster_profiles': 'list[HyperflexClusterProfileRef]',
        'data_ip_range': 'HyperflexIpAddrRange',
        'hxdp_ip_range': 'HyperflexIpAddrRange',
        'mgmt_ip_range': 'HyperflexIpAddrRange',
        'node_name_prefix': 'str',
        'organization': 'IamAccountRef'
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
        'cluster_profiles': 'ClusterProfiles',
        'data_ip_range': 'DataIpRange',
        'hxdp_ip_range': 'HxdpIpRange',
        'mgmt_ip_range': 'MgmtIpRange',
        'node_name_prefix': 'NodeNamePrefix',
        'organization': 'Organization'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, cluster_profiles=None, data_ip_range=None, hxdp_ip_range=None, mgmt_ip_range=None, node_name_prefix=None, organization=None):
        """
        HyperflexNodeConfigPolicy - a model defined in Swagger
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
        self._cluster_profiles = None
        self._data_ip_range = None
        self._hxdp_ip_range = None
        self._mgmt_ip_range = None
        self._node_name_prefix = None
        self._organization = None

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
        if cluster_profiles is not None:
          self.cluster_profiles = cluster_profiles
        if data_ip_range is not None:
          self.data_ip_range = data_ip_range
        if hxdp_ip_range is not None:
          self.hxdp_ip_range = hxdp_ip_range
        if mgmt_ip_range is not None:
          self.mgmt_ip_range = mgmt_ip_range
        if node_name_prefix is not None:
          self.node_name_prefix = node_name_prefix
        if organization is not None:
          self.organization = organization

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexNodeConfigPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexNodeConfigPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexNodeConfigPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexNodeConfigPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexNodeConfigPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexNodeConfigPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexNodeConfigPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexNodeConfigPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexNodeConfigPolicy.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexNodeConfigPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexNodeConfigPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexNodeConfigPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexNodeConfigPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexNodeConfigPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexNodeConfigPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexNodeConfigPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexNodeConfigPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexNodeConfigPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexNodeConfigPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexNodeConfigPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexNodeConfigPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexNodeConfigPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexNodeConfigPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexNodeConfigPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexNodeConfigPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexNodeConfigPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexNodeConfigPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexNodeConfigPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexNodeConfigPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexNodeConfigPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexNodeConfigPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexNodeConfigPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexNodeConfigPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexNodeConfigPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexNodeConfigPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexNodeConfigPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexNodeConfigPolicy.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexNodeConfigPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexNodeConfigPolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexNodeConfigPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this HyperflexNodeConfigPolicy.
        Description of the policy.  

        :return: The description of this HyperflexNodeConfigPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexNodeConfigPolicy.
        Description of the policy.  

        :param description: The description of this HyperflexNodeConfigPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexNodeConfigPolicy.
        Name of the policy.   

        :return: The name of this HyperflexNodeConfigPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexNodeConfigPolicy.
        Name of the policy.   

        :param name: The name of this HyperflexNodeConfigPolicy.
        :type: str
        """

        self._name = name

    @property
    def cluster_profiles(self):
        """
        Gets the cluster_profiles of this HyperflexNodeConfigPolicy.
        List of cluster profiles using this policy 

        :return: The cluster_profiles of this HyperflexNodeConfigPolicy.
        :rtype: list[HyperflexClusterProfileRef]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """
        Sets the cluster_profiles of this HyperflexNodeConfigPolicy.
        List of cluster profiles using this policy 

        :param cluster_profiles: The cluster_profiles of this HyperflexNodeConfigPolicy.
        :type: list[HyperflexClusterProfileRef]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def data_ip_range(self):
        """
        Gets the data_ip_range of this HyperflexNodeConfigPolicy.
        Storage data IP range  

        :return: The data_ip_range of this HyperflexNodeConfigPolicy.
        :rtype: HyperflexIpAddrRange
        """
        return self._data_ip_range

    @data_ip_range.setter
    def data_ip_range(self, data_ip_range):
        """
        Sets the data_ip_range of this HyperflexNodeConfigPolicy.
        Storage data IP range  

        :param data_ip_range: The data_ip_range of this HyperflexNodeConfigPolicy.
        :type: HyperflexIpAddrRange
        """

        self._data_ip_range = data_ip_range

    @property
    def hxdp_ip_range(self):
        """
        Gets the hxdp_ip_range of this HyperflexNodeConfigPolicy.
        HyperFlex storage management IP range  

        :return: The hxdp_ip_range of this HyperflexNodeConfigPolicy.
        :rtype: HyperflexIpAddrRange
        """
        return self._hxdp_ip_range

    @hxdp_ip_range.setter
    def hxdp_ip_range(self, hxdp_ip_range):
        """
        Sets the hxdp_ip_range of this HyperflexNodeConfigPolicy.
        HyperFlex storage management IP range  

        :param hxdp_ip_range: The hxdp_ip_range of this HyperflexNodeConfigPolicy.
        :type: HyperflexIpAddrRange
        """

        self._hxdp_ip_range = hxdp_ip_range

    @property
    def mgmt_ip_range(self):
        """
        Gets the mgmt_ip_range of this HyperflexNodeConfigPolicy.
        Management IP range  

        :return: The mgmt_ip_range of this HyperflexNodeConfigPolicy.
        :rtype: HyperflexIpAddrRange
        """
        return self._mgmt_ip_range

    @mgmt_ip_range.setter
    def mgmt_ip_range(self, mgmt_ip_range):
        """
        Sets the mgmt_ip_range of this HyperflexNodeConfigPolicy.
        Management IP range  

        :param mgmt_ip_range: The mgmt_ip_range of this HyperflexNodeConfigPolicy.
        :type: HyperflexIpAddrRange
        """

        self._mgmt_ip_range = mgmt_ip_range

    @property
    def node_name_prefix(self):
        """
        Gets the node_name_prefix of this HyperflexNodeConfigPolicy.
        Specifies a node name prefix that is used to automatically generate the default hostname for each server. A dash (-) will be appended to the prefix followed by the node number to form a hostname. This default naming scheme can be manually overridden in the node configuration. The maximum length of a prefix is 60 and must only contain alphanumeric characters or dash (-).   

        :return: The node_name_prefix of this HyperflexNodeConfigPolicy.
        :rtype: str
        """
        return self._node_name_prefix

    @node_name_prefix.setter
    def node_name_prefix(self, node_name_prefix):
        """
        Sets the node_name_prefix of this HyperflexNodeConfigPolicy.
        Specifies a node name prefix that is used to automatically generate the default hostname for each server. A dash (-) will be appended to the prefix followed by the node number to form a hostname. This default naming scheme can be manually overridden in the node configuration. The maximum length of a prefix is 60 and must only contain alphanumeric characters or dash (-).   

        :param node_name_prefix: The node_name_prefix of this HyperflexNodeConfigPolicy.
        :type: str
        """

        self._node_name_prefix = node_name_prefix

    @property
    def organization(self):
        """
        Gets the organization of this HyperflexNodeConfigPolicy.
        Organization 

        :return: The organization of this HyperflexNodeConfigPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this HyperflexNodeConfigPolicy.
        Organization 

        :param organization: The organization of this HyperflexNodeConfigPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

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
        if not isinstance(other, HyperflexNodeConfigPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
