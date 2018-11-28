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


class AssetClusterMember(object):
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
        'api_version': 'int',
        'app_partition_number': 'int',
        'connection_id': 'str',
        'connection_reason': 'str',
        'connection_status': 'str',
        'connection_status_last_change_time': 'datetime',
        'connector_version': 'str',
        'device_external_ip_address': 'str',
        'proxy_app': 'str',
        'device': 'AssetDeviceRegistrationRef',
        'leadership': 'str',
        'member_identity': 'str'
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
        'api_version': 'ApiVersion',
        'app_partition_number': 'AppPartitionNumber',
        'connection_id': 'ConnectionId',
        'connection_reason': 'ConnectionReason',
        'connection_status': 'ConnectionStatus',
        'connection_status_last_change_time': 'ConnectionStatusLastChangeTime',
        'connector_version': 'ConnectorVersion',
        'device_external_ip_address': 'DeviceExternalIpAddress',
        'proxy_app': 'ProxyApp',
        'device': 'Device',
        'leadership': 'Leadership',
        'member_identity': 'MemberIdentity'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, api_version=None, app_partition_number=None, connection_id=None, connection_reason=None, connection_status='null', connection_status_last_change_time=None, connector_version=None, device_external_ip_address=None, proxy_app=None, device=None, leadership='Unknown', member_identity=None):
        """
        AssetClusterMember - a model defined in Swagger
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
        self._api_version = None
        self._app_partition_number = None
        self._connection_id = None
        self._connection_reason = None
        self._connection_status = None
        self._connection_status_last_change_time = None
        self._connector_version = None
        self._device_external_ip_address = None
        self._proxy_app = None
        self._device = None
        self._leadership = None
        self._member_identity = None

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
        if api_version is not None:
          self.api_version = api_version
        if app_partition_number is not None:
          self.app_partition_number = app_partition_number
        if connection_id is not None:
          self.connection_id = connection_id
        if connection_reason is not None:
          self.connection_reason = connection_reason
        if connection_status is not None:
          self.connection_status = connection_status
        if connection_status_last_change_time is not None:
          self.connection_status_last_change_time = connection_status_last_change_time
        if connector_version is not None:
          self.connector_version = connector_version
        if device_external_ip_address is not None:
          self.device_external_ip_address = device_external_ip_address
        if proxy_app is not None:
          self.proxy_app = proxy_app
        if device is not None:
          self.device = device
        if leadership is not None:
          self.leadership = leadership
        if member_identity is not None:
          self.member_identity = member_identity

    @property
    def account_moid(self):
        """
        Gets the account_moid of this AssetClusterMember.
        The Account ID for this managed object.  

        :return: The account_moid of this AssetClusterMember.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this AssetClusterMember.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this AssetClusterMember.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this AssetClusterMember.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this AssetClusterMember.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this AssetClusterMember.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this AssetClusterMember.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this AssetClusterMember.
        The time when this managed object was created.  

        :return: The create_time of this AssetClusterMember.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this AssetClusterMember.
        The time when this managed object was created.  

        :param create_time: The create_time of this AssetClusterMember.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this AssetClusterMember.
        The time when this managed object was last modified.  

        :return: The mod_time of this AssetClusterMember.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this AssetClusterMember.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this AssetClusterMember.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this AssetClusterMember.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this AssetClusterMember.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this AssetClusterMember.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this AssetClusterMember.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this AssetClusterMember.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this AssetClusterMember.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AssetClusterMember.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this AssetClusterMember.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this AssetClusterMember.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this AssetClusterMember.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this AssetClusterMember.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this AssetClusterMember.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this AssetClusterMember.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this AssetClusterMember.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AssetClusterMember.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this AssetClusterMember.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this AssetClusterMember.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this AssetClusterMember.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AssetClusterMember.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this AssetClusterMember.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this AssetClusterMember.
        The versioning info for this managed object   

        :return: The version_context of this AssetClusterMember.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this AssetClusterMember.
        The versioning info for this managed object   

        :param version_context: The version_context of this AssetClusterMember.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def api_version(self):
        """
        Gets the api_version of this AssetClusterMember.
        The version of the connector api. Describes the capability of the connector's framework. If the version is lower than the current minimum supported version defined in the service managing the connection, the device connector will be connected with limited capabilities until the device connector is upgraded to a fully supported version. For example if a device connector that was released without delta inventory capabilities registers and connects to Intersight, inventory collection may be disabled until it has been upgraded. 

        :return: The api_version of this AssetClusterMember.
        :rtype: int
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this AssetClusterMember.
        The version of the connector api. Describes the capability of the connector's framework. If the version is lower than the current minimum supported version defined in the service managing the connection, the device connector will be connected with limited capabilities until the device connector is upgraded to a fully supported version. For example if a device connector that was released without delta inventory capabilities registers and connects to Intersight, inventory collection may be disabled until it has been upgraded. 

        :param api_version: The api_version of this AssetClusterMember.
        :type: int
        """

        self._api_version = api_version

    @property
    def app_partition_number(self):
        """
        Gets the app_partition_number of this AssetClusterMember.
        The partition number corresponding to the instance of the Proxy App which is managing the web-socket to the device connector.  

        :return: The app_partition_number of this AssetClusterMember.
        :rtype: int
        """
        return self._app_partition_number

    @app_partition_number.setter
    def app_partition_number(self, app_partition_number):
        """
        Sets the app_partition_number of this AssetClusterMember.
        The partition number corresponding to the instance of the Proxy App which is managing the web-socket to the device connector.  

        :param app_partition_number: The app_partition_number of this AssetClusterMember.
        :type: int
        """

        self._app_partition_number = app_partition_number

    @property
    def connection_id(self):
        """
        Gets the connection_id of this AssetClusterMember.
        The unique identifier for the current connection. The identifier persists across network connectivity loss and is reset on device connector process restart or platform administrator toggle of the Intersight connectivity. The connectionId can be used by services that need to interact with stateful plugins running in the device connector process. For example if a service schedules an inventory in a devices job scheduler plugin at registration it is not necessary to reschedule the job if the device loses network connectivity due to an Intersight service upgrade or intermittent network issues in the devices datacenter.  

        :return: The connection_id of this AssetClusterMember.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this AssetClusterMember.
        The unique identifier for the current connection. The identifier persists across network connectivity loss and is reset on device connector process restart or platform administrator toggle of the Intersight connectivity. The connectionId can be used by services that need to interact with stateful plugins running in the device connector process. For example if a service schedules an inventory in a devices job scheduler plugin at registration it is not necessary to reschedule the job if the device loses network connectivity due to an Intersight service upgrade or intermittent network issues in the devices datacenter.  

        :param connection_id: The connection_id of this AssetClusterMember.
        :type: str
        """

        self._connection_id = connection_id

    @property
    def connection_reason(self):
        """
        Gets the connection_reason of this AssetClusterMember.
        If 'connectionStatus' is not equal to Connected, connectionReason provides further details about why the device is not connected with the cloud.  

        :return: The connection_reason of this AssetClusterMember.
        :rtype: str
        """
        return self._connection_reason

    @connection_reason.setter
    def connection_reason(self, connection_reason):
        """
        Sets the connection_reason of this AssetClusterMember.
        If 'connectionStatus' is not equal to Connected, connectionReason provides further details about why the device is not connected with the cloud.  

        :param connection_reason: The connection_reason of this AssetClusterMember.
        :type: str
        """

        self._connection_reason = connection_reason

    @property
    def connection_status(self):
        """
        Gets the connection_status of this AssetClusterMember.
        The status of the persistent connection between the device connector and Intersight.  

        :return: The connection_status of this AssetClusterMember.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this AssetClusterMember.
        The status of the persistent connection between the device connector and Intersight.  

        :param connection_status: The connection_status of this AssetClusterMember.
        :type: str
        """
        allowed_values = ["", "Connected", "NotConnected"]
        if connection_status not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_status` ({0}), must be one of {1}"
                .format(connection_status, allowed_values)
            )

        self._connection_status = connection_status

    @property
    def connection_status_last_change_time(self):
        """
        Gets the connection_status_last_change_time of this AssetClusterMember.
        The last time at which the 'connectionStatus' property value changed. If connectionStatus is Connected, this time can be interpreted as the starting time since which a persistent connection has been maintained between the cloud and device connector. If connectionStatus is NotConnected, this time can be interpreted as the last time the device connector was connected with the cloud.  

        :return: The connection_status_last_change_time of this AssetClusterMember.
        :rtype: datetime
        """
        return self._connection_status_last_change_time

    @connection_status_last_change_time.setter
    def connection_status_last_change_time(self, connection_status_last_change_time):
        """
        Sets the connection_status_last_change_time of this AssetClusterMember.
        The last time at which the 'connectionStatus' property value changed. If connectionStatus is Connected, this time can be interpreted as the starting time since which a persistent connection has been maintained between the cloud and device connector. If connectionStatus is NotConnected, this time can be interpreted as the last time the device connector was connected with the cloud.  

        :param connection_status_last_change_time: The connection_status_last_change_time of this AssetClusterMember.
        :type: datetime
        """

        self._connection_status_last_change_time = connection_status_last_change_time

    @property
    def connector_version(self):
        """
        Gets the connector_version of this AssetClusterMember.
        The version of the device connector running on the managed device.  

        :return: The connector_version of this AssetClusterMember.
        :rtype: str
        """
        return self._connector_version

    @connector_version.setter
    def connector_version(self, connector_version):
        """
        Sets the connector_version of this AssetClusterMember.
        The version of the device connector running on the managed device.  

        :param connector_version: The connector_version of this AssetClusterMember.
        :type: str
        """

        self._connector_version = connector_version

    @property
    def device_external_ip_address(self):
        """
        Gets the device_external_ip_address of this AssetClusterMember.
        The IP Address of the managed device as seen from the cloud at the time of registration. Eg this could be the IP of the managed device's interface which has a route to the internet or a NAT IP when the managed device is deployed in a private network.  

        :return: The device_external_ip_address of this AssetClusterMember.
        :rtype: str
        """
        return self._device_external_ip_address

    @device_external_ip_address.setter
    def device_external_ip_address(self, device_external_ip_address):
        """
        Sets the device_external_ip_address of this AssetClusterMember.
        The IP Address of the managed device as seen from the cloud at the time of registration. Eg this could be the IP of the managed device's interface which has a route to the internet or a NAT IP when the managed device is deployed in a private network.  

        :param device_external_ip_address: The device_external_ip_address of this AssetClusterMember.
        :type: str
        """

        self._device_external_ip_address = device_external_ip_address

    @property
    def proxy_app(self):
        """
        Gets the proxy_app of this AssetClusterMember.
        The name of the app which will proxy the messages to the device connector.   

        :return: The proxy_app of this AssetClusterMember.
        :rtype: str
        """
        return self._proxy_app

    @proxy_app.setter
    def proxy_app(self, proxy_app):
        """
        Sets the proxy_app of this AssetClusterMember.
        The name of the app which will proxy the messages to the device connector.   

        :param proxy_app: The proxy_app of this AssetClusterMember.
        :type: str
        """

        self._proxy_app = proxy_app

    @property
    def device(self):
        """
        Gets the device of this AssetClusterMember.

        :return: The device of this AssetClusterMember.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this AssetClusterMember.

        :param device: The device of this AssetClusterMember.
        :type: AssetDeviceRegistrationRef
        """

        self._device = device

    @property
    def leadership(self):
        """
        Gets the leadership of this AssetClusterMember.
        The current leadershipstate of this member. Updated by the device connector on failover or leadership change. If a member is elected as Primary within the cluster this connection will be the same as the DeviceRegistration connection. E.g a message addressed to the DeviceRegistration will be forwarded to the ClusterMember connection.  

        :return: The leadership of this AssetClusterMember.
        :rtype: str
        """
        return self._leadership

    @leadership.setter
    def leadership(self, leadership):
        """
        Sets the leadership of this AssetClusterMember.
        The current leadershipstate of this member. Updated by the device connector on failover or leadership change. If a member is elected as Primary within the cluster this connection will be the same as the DeviceRegistration connection. E.g a message addressed to the DeviceRegistration will be forwarded to the ClusterMember connection.  

        :param leadership: The leadership of this AssetClusterMember.
        :type: str
        """
        allowed_values = ["Unknown", "Primary", "Secondary"]
        if leadership not in allowed_values:
            raise ValueError(
                "Invalid value for `leadership` ({0}), must be one of {1}"
                .format(leadership, allowed_values)
            )

        self._leadership = leadership

    @property
    def member_identity(self):
        """
        Gets the member_identity of this AssetClusterMember.
        The unique identity of the member within the cluster. The identity is retrieved from the platform and reported by the device connector at connection time.   

        :return: The member_identity of this AssetClusterMember.
        :rtype: str
        """
        return self._member_identity

    @member_identity.setter
    def member_identity(self, member_identity):
        """
        Sets the member_identity of this AssetClusterMember.
        The unique identity of the member within the cluster. The identity is retrieved from the platform and reported by the device connector at connection time.   

        :param member_identity: The member_identity of this AssetClusterMember.
        :type: str
        """

        self._member_identity = member_identity

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
        if not isinstance(other, AssetClusterMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
