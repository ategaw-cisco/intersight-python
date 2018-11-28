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


class LicenseAccountLicenseData(object):
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
        'account': 'IamAccountRef',
        'account_id': 'str',
        'agent_data': 'str',
        'auth_expire_time': 'str',
        'auth_initial_time': 'str',
        'auth_next_time': 'str',
        'category': 'str',
        'customer_op': 'LicenseCustomerOpRef',
        'group': 'str',
        'last_sync': 'datetime',
        'last_updated_time': 'datetime',
        'license_state': 'str',
        'license_tech_support_info': 'str',
        'licenseinfos': 'list[LicenseLicenseInfoRef]',
        'register_expire_time': 'str',
        'register_initial_time': 'str',
        'register_next_time': 'str',
        'registration_status': 'str',
        'renew_failure_string': 'str',
        'smart_account': 'str',
        'smartlicense_token': 'LicenseSmartlicenseTokenRef',
        'sync_status': 'str',
        'virtual_account': 'str'
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
        'account': 'Account',
        'account_id': 'AccountId',
        'agent_data': 'AgentData',
        'auth_expire_time': 'AuthExpireTime',
        'auth_initial_time': 'AuthInitialTime',
        'auth_next_time': 'AuthNextTime',
        'category': 'Category',
        'customer_op': 'CustomerOp',
        'group': 'Group',
        'last_sync': 'LastSync',
        'last_updated_time': 'LastUpdatedTime',
        'license_state': 'LicenseState',
        'license_tech_support_info': 'LicenseTechSupportInfo',
        'licenseinfos': 'Licenseinfos',
        'register_expire_time': 'RegisterExpireTime',
        'register_initial_time': 'RegisterInitialTime',
        'register_next_time': 'RegisterNextTime',
        'registration_status': 'RegistrationStatus',
        'renew_failure_string': 'RenewFailureString',
        'smart_account': 'SmartAccount',
        'smartlicense_token': 'SmartlicenseToken',
        'sync_status': 'SyncStatus',
        'virtual_account': 'VirtualAccount'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, account=None, account_id=None, agent_data=None, auth_expire_time=None, auth_initial_time=None, auth_next_time=None, category=None, customer_op=None, group=None, last_sync=None, last_updated_time=None, license_state=None, license_tech_support_info=None, licenseinfos=None, register_expire_time=None, register_initial_time=None, register_next_time=None, registration_status=None, renew_failure_string=None, smart_account=None, smartlicense_token=None, sync_status=None, virtual_account=None):
        """
        LicenseAccountLicenseData - a model defined in Swagger
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
        self._account = None
        self._account_id = None
        self._agent_data = None
        self._auth_expire_time = None
        self._auth_initial_time = None
        self._auth_next_time = None
        self._category = None
        self._customer_op = None
        self._group = None
        self._last_sync = None
        self._last_updated_time = None
        self._license_state = None
        self._license_tech_support_info = None
        self._licenseinfos = None
        self._register_expire_time = None
        self._register_initial_time = None
        self._register_next_time = None
        self._registration_status = None
        self._renew_failure_string = None
        self._smart_account = None
        self._smartlicense_token = None
        self._sync_status = None
        self._virtual_account = None

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
        if account is not None:
          self.account = account
        if account_id is not None:
          self.account_id = account_id
        if agent_data is not None:
          self.agent_data = agent_data
        if auth_expire_time is not None:
          self.auth_expire_time = auth_expire_time
        if auth_initial_time is not None:
          self.auth_initial_time = auth_initial_time
        if auth_next_time is not None:
          self.auth_next_time = auth_next_time
        if category is not None:
          self.category = category
        if customer_op is not None:
          self.customer_op = customer_op
        if group is not None:
          self.group = group
        if last_sync is not None:
          self.last_sync = last_sync
        if last_updated_time is not None:
          self.last_updated_time = last_updated_time
        if license_state is not None:
          self.license_state = license_state
        if license_tech_support_info is not None:
          self.license_tech_support_info = license_tech_support_info
        if licenseinfos is not None:
          self.licenseinfos = licenseinfos
        if register_expire_time is not None:
          self.register_expire_time = register_expire_time
        if register_initial_time is not None:
          self.register_initial_time = register_initial_time
        if register_next_time is not None:
          self.register_next_time = register_next_time
        if registration_status is not None:
          self.registration_status = registration_status
        if renew_failure_string is not None:
          self.renew_failure_string = renew_failure_string
        if smart_account is not None:
          self.smart_account = smart_account
        if smartlicense_token is not None:
          self.smartlicense_token = smartlicense_token
        if sync_status is not None:
          self.sync_status = sync_status
        if virtual_account is not None:
          self.virtual_account = virtual_account

    @property
    def account_moid(self):
        """
        Gets the account_moid of this LicenseAccountLicenseData.
        The Account ID for this managed object.  

        :return: The account_moid of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this LicenseAccountLicenseData.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this LicenseAccountLicenseData.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this LicenseAccountLicenseData.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this LicenseAccountLicenseData.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this LicenseAccountLicenseData.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this LicenseAccountLicenseData.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this LicenseAccountLicenseData.
        The time when this managed object was created.  

        :return: The create_time of this LicenseAccountLicenseData.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this LicenseAccountLicenseData.
        The time when this managed object was created.  

        :param create_time: The create_time of this LicenseAccountLicenseData.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this LicenseAccountLicenseData.
        The time when this managed object was last modified.  

        :return: The mod_time of this LicenseAccountLicenseData.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this LicenseAccountLicenseData.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this LicenseAccountLicenseData.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this LicenseAccountLicenseData.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this LicenseAccountLicenseData.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this LicenseAccountLicenseData.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this LicenseAccountLicenseData.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this LicenseAccountLicenseData.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this LicenseAccountLicenseData.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this LicenseAccountLicenseData.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this LicenseAccountLicenseData.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this LicenseAccountLicenseData.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this LicenseAccountLicenseData.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this LicenseAccountLicenseData.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this LicenseAccountLicenseData.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this LicenseAccountLicenseData.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this LicenseAccountLicenseData.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this LicenseAccountLicenseData.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this LicenseAccountLicenseData.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this LicenseAccountLicenseData.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this LicenseAccountLicenseData.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this LicenseAccountLicenseData.
        The versioning info for this managed object   

        :return: The version_context of this LicenseAccountLicenseData.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this LicenseAccountLicenseData.
        The versioning info for this managed object   

        :param version_context: The version_context of this LicenseAccountLicenseData.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def account(self):
        """
        Gets the account of this LicenseAccountLicenseData.

        :return: The account of this LicenseAccountLicenseData.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this LicenseAccountLicenseData.

        :param account: The account of this LicenseAccountLicenseData.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def account_id(self):
        """
        Gets the account_id of this LicenseAccountLicenseData.
        Root user's ID of the account  

        :return: The account_id of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this LicenseAccountLicenseData.
        Root user's ID of the account  

        :param account_id: The account_id of this LicenseAccountLicenseData.
        :type: str
        """

        self._account_id = account_id

    @property
    def agent_data(self):
        """
        Gets the agent_data of this LicenseAccountLicenseData.
        Agent trusted store data  

        :return: The agent_data of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._agent_data

    @agent_data.setter
    def agent_data(self, agent_data):
        """
        Sets the agent_data of this LicenseAccountLicenseData.
        Agent trusted store data  

        :param agent_data: The agent_data of this LicenseAccountLicenseData.
        :type: str
        """

        self._agent_data = agent_data

    @property
    def auth_expire_time(self):
        """
        Gets the auth_expire_time of this LicenseAccountLicenseData.
        Authorization expiration time  

        :return: The auth_expire_time of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._auth_expire_time

    @auth_expire_time.setter
    def auth_expire_time(self, auth_expire_time):
        """
        Sets the auth_expire_time of this LicenseAccountLicenseData.
        Authorization expiration time  

        :param auth_expire_time: The auth_expire_time of this LicenseAccountLicenseData.
        :type: str
        """

        self._auth_expire_time = auth_expire_time

    @property
    def auth_initial_time(self):
        """
        Gets the auth_initial_time of this LicenseAccountLicenseData.
        Intial Authorization time  

        :return: The auth_initial_time of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._auth_initial_time

    @auth_initial_time.setter
    def auth_initial_time(self, auth_initial_time):
        """
        Sets the auth_initial_time of this LicenseAccountLicenseData.
        Intial Authorization time  

        :param auth_initial_time: The auth_initial_time of this LicenseAccountLicenseData.
        :type: str
        """

        self._auth_initial_time = auth_initial_time

    @property
    def auth_next_time(self):
        """
        Gets the auth_next_time of this LicenseAccountLicenseData.
        Next time for Authorization  

        :return: The auth_next_time of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._auth_next_time

    @auth_next_time.setter
    def auth_next_time(self, auth_next_time):
        """
        Sets the auth_next_time of this LicenseAccountLicenseData.
        Next time for Authorization  

        :param auth_next_time: The auth_next_time of this LicenseAccountLicenseData.
        :type: str
        """

        self._auth_next_time = auth_next_time

    @property
    def category(self):
        """
        Gets the category of this LicenseAccountLicenseData.
        License category  

        :return: The category of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this LicenseAccountLicenseData.
        License category  

        :param category: The category of this LicenseAccountLicenseData.
        :type: str
        """

        self._category = category

    @property
    def customer_op(self):
        """
        Gets the customer_op of this LicenseAccountLicenseData.

        :return: The customer_op of this LicenseAccountLicenseData.
        :rtype: LicenseCustomerOpRef
        """
        return self._customer_op

    @customer_op.setter
    def customer_op(self, customer_op):
        """
        Sets the customer_op of this LicenseAccountLicenseData.

        :param customer_op: The customer_op of this LicenseAccountLicenseData.
        :type: LicenseCustomerOpRef
        """

        self._customer_op = customer_op

    @property
    def group(self):
        """
        Gets the group of this LicenseAccountLicenseData.
        Group  

        :return: The group of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this LicenseAccountLicenseData.
        Group  

        :param group: The group of this LicenseAccountLicenseData.
        :type: str
        """

        self._group = group

    @property
    def last_sync(self):
        """
        Gets the last_sync of this LicenseAccountLicenseData.
        Specifies last sync time with SA  

        :return: The last_sync of this LicenseAccountLicenseData.
        :rtype: datetime
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """
        Sets the last_sync of this LicenseAccountLicenseData.
        Specifies last sync time with SA  

        :param last_sync: The last_sync of this LicenseAccountLicenseData.
        :type: datetime
        """

        self._last_sync = last_sync

    @property
    def last_updated_time(self):
        """
        Gets the last_updated_time of this LicenseAccountLicenseData.
        Last updated  

        :return: The last_updated_time of this LicenseAccountLicenseData.
        :rtype: datetime
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """
        Sets the last_updated_time of this LicenseAccountLicenseData.
        Last updated  

        :param last_updated_time: The last_updated_time of this LicenseAccountLicenseData.
        :type: datetime
        """

        self._last_updated_time = last_updated_time

    @property
    def license_state(self):
        """
        Gets the license_state of this LicenseAccountLicenseData.
        Aggregrated mode for the agent  

        :return: The license_state of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._license_state

    @license_state.setter
    def license_state(self, license_state):
        """
        Sets the license_state of this LicenseAccountLicenseData.
        Aggregrated mode for the agent  

        :param license_state: The license_state of this LicenseAccountLicenseData.
        :type: str
        """

        self._license_state = license_state

    @property
    def license_tech_support_info(self):
        """
        Gets the license_tech_support_info of this LicenseAccountLicenseData.
        Tech-support info for a smart-agent  

        :return: The license_tech_support_info of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._license_tech_support_info

    @license_tech_support_info.setter
    def license_tech_support_info(self, license_tech_support_info):
        """
        Sets the license_tech_support_info of this LicenseAccountLicenseData.
        Tech-support info for a smart-agent  

        :param license_tech_support_info: The license_tech_support_info of this LicenseAccountLicenseData.
        :type: str
        """

        self._license_tech_support_info = license_tech_support_info

    @property
    def licenseinfos(self):
        """
        Gets the licenseinfos of this LicenseAccountLicenseData.

        :return: The licenseinfos of this LicenseAccountLicenseData.
        :rtype: list[LicenseLicenseInfoRef]
        """
        return self._licenseinfos

    @licenseinfos.setter
    def licenseinfos(self, licenseinfos):
        """
        Sets the licenseinfos of this LicenseAccountLicenseData.

        :param licenseinfos: The licenseinfos of this LicenseAccountLicenseData.
        :type: list[LicenseLicenseInfoRef]
        """

        self._licenseinfos = licenseinfos

    @property
    def register_expire_time(self):
        """
        Gets the register_expire_time of this LicenseAccountLicenseData.
        Registration exipiration time  

        :return: The register_expire_time of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._register_expire_time

    @register_expire_time.setter
    def register_expire_time(self, register_expire_time):
        """
        Sets the register_expire_time of this LicenseAccountLicenseData.
        Registration exipiration time  

        :param register_expire_time: The register_expire_time of this LicenseAccountLicenseData.
        :type: str
        """

        self._register_expire_time = register_expire_time

    @property
    def register_initial_time(self):
        """
        Gets the register_initial_time of this LicenseAccountLicenseData.
        Initial time of registration  

        :return: The register_initial_time of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._register_initial_time

    @register_initial_time.setter
    def register_initial_time(self, register_initial_time):
        """
        Sets the register_initial_time of this LicenseAccountLicenseData.
        Initial time of registration  

        :param register_initial_time: The register_initial_time of this LicenseAccountLicenseData.
        :type: str
        """

        self._register_initial_time = register_initial_time

    @property
    def register_next_time(self):
        """
        Gets the register_next_time of this LicenseAccountLicenseData.
        Next time for registration  

        :return: The register_next_time of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._register_next_time

    @register_next_time.setter
    def register_next_time(self, register_next_time):
        """
        Sets the register_next_time of this LicenseAccountLicenseData.
        Next time for registration  

        :param register_next_time: The register_next_time of this LicenseAccountLicenseData.
        :type: str
        """

        self._register_next_time = register_next_time

    @property
    def registration_status(self):
        """
        Gets the registration_status of this LicenseAccountLicenseData.
        Registration status  

        :return: The registration_status of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._registration_status

    @registration_status.setter
    def registration_status(self, registration_status):
        """
        Sets the registration_status of this LicenseAccountLicenseData.
        Registration status  

        :param registration_status: The registration_status of this LicenseAccountLicenseData.
        :type: str
        """

        self._registration_status = registration_status

    @property
    def renew_failure_string(self):
        """
        Gets the renew_failure_string of this LicenseAccountLicenseData.
        Renew failure message  

        :return: The renew_failure_string of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._renew_failure_string

    @renew_failure_string.setter
    def renew_failure_string(self, renew_failure_string):
        """
        Sets the renew_failure_string of this LicenseAccountLicenseData.
        Renew failure message  

        :param renew_failure_string: The renew_failure_string of this LicenseAccountLicenseData.
        :type: str
        """

        self._renew_failure_string = renew_failure_string

    @property
    def smart_account(self):
        """
        Gets the smart_account of this LicenseAccountLicenseData.
        Name of smart account  

        :return: The smart_account of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._smart_account

    @smart_account.setter
    def smart_account(self, smart_account):
        """
        Sets the smart_account of this LicenseAccountLicenseData.
        Name of smart account  

        :param smart_account: The smart_account of this LicenseAccountLicenseData.
        :type: str
        """

        self._smart_account = smart_account

    @property
    def smartlicense_token(self):
        """
        Gets the smartlicense_token of this LicenseAccountLicenseData.

        :return: The smartlicense_token of this LicenseAccountLicenseData.
        :rtype: LicenseSmartlicenseTokenRef
        """
        return self._smartlicense_token

    @smartlicense_token.setter
    def smartlicense_token(self, smartlicense_token):
        """
        Sets the smartlicense_token of this LicenseAccountLicenseData.

        :param smartlicense_token: The smartlicense_token of this LicenseAccountLicenseData.
        :type: LicenseSmartlicenseTokenRef
        """

        self._smartlicense_token = smartlicense_token

    @property
    def sync_status(self):
        """
        Gets the sync_status of this LicenseAccountLicenseData.
        Current sync status for the account  

        :return: The sync_status of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """
        Sets the sync_status of this LicenseAccountLicenseData.
        Current sync status for the account  

        :param sync_status: The sync_status of this LicenseAccountLicenseData.
        :type: str
        """

        self._sync_status = sync_status

    @property
    def virtual_account(self):
        """
        Gets the virtual_account of this LicenseAccountLicenseData.
        Name of virtual account   

        :return: The virtual_account of this LicenseAccountLicenseData.
        :rtype: str
        """
        return self._virtual_account

    @virtual_account.setter
    def virtual_account(self, virtual_account):
        """
        Sets the virtual_account of this LicenseAccountLicenseData.
        Name of virtual account   

        :param virtual_account: The virtual_account of this LicenseAccountLicenseData.
        :type: str
        """

        self._virtual_account = virtual_account

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
        if not isinstance(other, LicenseAccountLicenseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
