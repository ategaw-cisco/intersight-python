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


class HyperflexCluster(object):
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
        'alarm': 'list[HyperflexAlarmRef]',
        'cluster_name': 'str',
        'cluster_type': 'int',
        'cluster_uuid': 'str',
        'compute_node_count': 'int',
        'converged_node_count': 'int',
        'device_id': 'str',
        'flt_aggr': 'int',
        'hx_version': 'str',
        'hypervisor_type': 'str',
        'hypervisor_version': 'str',
        'nodes': 'list[HyperflexNodeRef]',
        'registered_device': 'AssetDeviceRegistrationRef',
        'summary': 'HyperflexSummary',
        'vm_count': 'int'
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
        'alarm': 'Alarm',
        'cluster_name': 'ClusterName',
        'cluster_type': 'ClusterType',
        'cluster_uuid': 'ClusterUuid',
        'compute_node_count': 'ComputeNodeCount',
        'converged_node_count': 'ConvergedNodeCount',
        'device_id': 'DeviceId',
        'flt_aggr': 'FltAggr',
        'hx_version': 'HxVersion',
        'hypervisor_type': 'HypervisorType',
        'hypervisor_version': 'HypervisorVersion',
        'nodes': 'Nodes',
        'registered_device': 'RegisteredDevice',
        'summary': 'Summary',
        'vm_count': 'VmCount'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, alarm=None, cluster_name=None, cluster_type=None, cluster_uuid=None, compute_node_count=None, converged_node_count=None, device_id=None, flt_aggr=None, hx_version=None, hypervisor_type='Unknown', hypervisor_version=None, nodes=None, registered_device=None, summary=None, vm_count=None):
        """
        HyperflexCluster - a model defined in Swagger
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
        self._alarm = None
        self._cluster_name = None
        self._cluster_type = None
        self._cluster_uuid = None
        self._compute_node_count = None
        self._converged_node_count = None
        self._device_id = None
        self._flt_aggr = None
        self._hx_version = None
        self._hypervisor_type = None
        self._hypervisor_version = None
        self._nodes = None
        self._registered_device = None
        self._summary = None
        self._vm_count = None

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
        if alarm is not None:
          self.alarm = alarm
        if cluster_name is not None:
          self.cluster_name = cluster_name
        if cluster_type is not None:
          self.cluster_type = cluster_type
        if cluster_uuid is not None:
          self.cluster_uuid = cluster_uuid
        if compute_node_count is not None:
          self.compute_node_count = compute_node_count
        if converged_node_count is not None:
          self.converged_node_count = converged_node_count
        if device_id is not None:
          self.device_id = device_id
        if flt_aggr is not None:
          self.flt_aggr = flt_aggr
        if hx_version is not None:
          self.hx_version = hx_version
        if hypervisor_type is not None:
          self.hypervisor_type = hypervisor_type
        if hypervisor_version is not None:
          self.hypervisor_version = hypervisor_version
        if nodes is not None:
          self.nodes = nodes
        if registered_device is not None:
          self.registered_device = registered_device
        if summary is not None:
          self.summary = summary
        if vm_count is not None:
          self.vm_count = vm_count

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexCluster.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexCluster.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexCluster.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexCluster.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexCluster.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexCluster.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexCluster.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexCluster.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexCluster.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexCluster.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexCluster.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexCluster.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexCluster.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexCluster.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexCluster.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexCluster.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexCluster.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexCluster.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexCluster.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexCluster.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexCluster.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexCluster.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexCluster.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexCluster.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexCluster.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexCluster.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexCluster.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexCluster.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexCluster.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexCluster.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexCluster.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexCluster.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexCluster.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this HyperflexCluster.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexCluster.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this HyperflexCluster.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexCluster.
        The versioning info for this managed object   

        :return: The version_context of this HyperflexCluster.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexCluster.
        The versioning info for this managed object   

        :param version_context: The version_context of this HyperflexCluster.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def alarm(self):
        """
        Gets the alarm of this HyperflexCluster.

        :return: The alarm of this HyperflexCluster.
        :rtype: list[HyperflexAlarmRef]
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        """
        Sets the alarm of this HyperflexCluster.

        :param alarm: The alarm of this HyperflexCluster.
        :type: list[HyperflexAlarmRef]
        """

        self._alarm = alarm

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this HyperflexCluster.

        :return: The cluster_name of this HyperflexCluster.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this HyperflexCluster.

        :param cluster_name: The cluster_name of this HyperflexCluster.
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        """
        Gets the cluster_type of this HyperflexCluster.

        :return: The cluster_type of this HyperflexCluster.
        :rtype: int
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """
        Sets the cluster_type of this HyperflexCluster.

        :param cluster_type: The cluster_type of this HyperflexCluster.
        :type: int
        """

        self._cluster_type = cluster_type

    @property
    def cluster_uuid(self):
        """
        Gets the cluster_uuid of this HyperflexCluster.

        :return: The cluster_uuid of this HyperflexCluster.
        :rtype: str
        """
        return self._cluster_uuid

    @cluster_uuid.setter
    def cluster_uuid(self, cluster_uuid):
        """
        Sets the cluster_uuid of this HyperflexCluster.

        :param cluster_uuid: The cluster_uuid of this HyperflexCluster.
        :type: str
        """

        self._cluster_uuid = cluster_uuid

    @property
    def compute_node_count(self):
        """
        Gets the compute_node_count of this HyperflexCluster.

        :return: The compute_node_count of this HyperflexCluster.
        :rtype: int
        """
        return self._compute_node_count

    @compute_node_count.setter
    def compute_node_count(self, compute_node_count):
        """
        Sets the compute_node_count of this HyperflexCluster.

        :param compute_node_count: The compute_node_count of this HyperflexCluster.
        :type: int
        """

        self._compute_node_count = compute_node_count

    @property
    def converged_node_count(self):
        """
        Gets the converged_node_count of this HyperflexCluster.

        :return: The converged_node_count of this HyperflexCluster.
        :rtype: int
        """
        return self._converged_node_count

    @converged_node_count.setter
    def converged_node_count(self, converged_node_count):
        """
        Sets the converged_node_count of this HyperflexCluster.

        :param converged_node_count: The converged_node_count of this HyperflexCluster.
        :type: int
        """

        self._converged_node_count = converged_node_count

    @property
    def device_id(self):
        """
        Gets the device_id of this HyperflexCluster.

        :return: The device_id of this HyperflexCluster.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this HyperflexCluster.

        :param device_id: The device_id of this HyperflexCluster.
        :type: str
        """

        self._device_id = device_id

    @property
    def flt_aggr(self):
        """
        Gets the flt_aggr of this HyperflexCluster.

        :return: The flt_aggr of this HyperflexCluster.
        :rtype: int
        """
        return self._flt_aggr

    @flt_aggr.setter
    def flt_aggr(self, flt_aggr):
        """
        Sets the flt_aggr of this HyperflexCluster.

        :param flt_aggr: The flt_aggr of this HyperflexCluster.
        :type: int
        """

        self._flt_aggr = flt_aggr

    @property
    def hx_version(self):
        """
        Gets the hx_version of this HyperflexCluster.

        :return: The hx_version of this HyperflexCluster.
        :rtype: str
        """
        return self._hx_version

    @hx_version.setter
    def hx_version(self, hx_version):
        """
        Sets the hx_version of this HyperflexCluster.

        :param hx_version: The hx_version of this HyperflexCluster.
        :type: str
        """

        self._hx_version = hx_version

    @property
    def hypervisor_type(self):
        """
        Gets the hypervisor_type of this HyperflexCluster.

        :return: The hypervisor_type of this HyperflexCluster.
        :rtype: str
        """
        return self._hypervisor_type

    @hypervisor_type.setter
    def hypervisor_type(self, hypervisor_type):
        """
        Sets the hypervisor_type of this HyperflexCluster.

        :param hypervisor_type: The hypervisor_type of this HyperflexCluster.
        :type: str
        """
        allowed_values = ["Unknown", "HyperV", "ESXi"]
        if hypervisor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `hypervisor_type` ({0}), must be one of {1}"
                .format(hypervisor_type, allowed_values)
            )

        self._hypervisor_type = hypervisor_type

    @property
    def hypervisor_version(self):
        """
        Gets the hypervisor_version of this HyperflexCluster.

        :return: The hypervisor_version of this HyperflexCluster.
        :rtype: str
        """
        return self._hypervisor_version

    @hypervisor_version.setter
    def hypervisor_version(self, hypervisor_version):
        """
        Sets the hypervisor_version of this HyperflexCluster.

        :param hypervisor_version: The hypervisor_version of this HyperflexCluster.
        :type: str
        """

        self._hypervisor_version = hypervisor_version

    @property
    def nodes(self):
        """
        Gets the nodes of this HyperflexCluster.

        :return: The nodes of this HyperflexCluster.
        :rtype: list[HyperflexNodeRef]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this HyperflexCluster.

        :param nodes: The nodes of this HyperflexCluster.
        :type: list[HyperflexNodeRef]
        """

        self._nodes = nodes

    @property
    def registered_device(self):
        """
        Gets the registered_device of this HyperflexCluster.

        :return: The registered_device of this HyperflexCluster.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this HyperflexCluster.

        :param registered_device: The registered_device of this HyperflexCluster.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def summary(self):
        """
        Gets the summary of this HyperflexCluster.

        :return: The summary of this HyperflexCluster.
        :rtype: HyperflexSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this HyperflexCluster.

        :param summary: The summary of this HyperflexCluster.
        :type: HyperflexSummary
        """

        self._summary = summary

    @property
    def vm_count(self):
        """
        Gets the vm_count of this HyperflexCluster.

        :return: The vm_count of this HyperflexCluster.
        :rtype: int
        """
        return self._vm_count

    @vm_count.setter
    def vm_count(self, vm_count):
        """
        Sets the vm_count of this HyperflexCluster.

        :param vm_count: The vm_count of this HyperflexCluster.
        :type: int
        """

        self._vm_count = vm_count

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
        if not isinstance(other, HyperflexCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
