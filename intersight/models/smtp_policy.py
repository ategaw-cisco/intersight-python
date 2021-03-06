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


class SmtpPolicy(object):
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
        'enabled': 'bool',
        'min_severity': 'str',
        'organization': 'IamAccountRef',
        'profiles': 'list[PolicyAbstractConfigProfileRef]',
        'sender_email': 'str',
        'smtp_port': 'int',
        'smtp_recipients': 'list[str]',
        'smtp_server': 'str'
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
        'enabled': 'Enabled',
        'min_severity': 'MinSeverity',
        'organization': 'Organization',
        'profiles': 'Profiles',
        'sender_email': 'SenderEmail',
        'smtp_port': 'SmtpPort',
        'smtp_recipients': 'SmtpRecipients',
        'smtp_server': 'SmtpServer'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, description=None, name=None, enabled=None, min_severity='critical', organization=None, profiles=None, sender_email=None, smtp_port=None, smtp_recipients=None, smtp_server=None):
        """
        SmtpPolicy - a model defined in Swagger
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
        self._enabled = None
        self._min_severity = None
        self._organization = None
        self._profiles = None
        self._sender_email = None
        self._smtp_port = None
        self._smtp_recipients = None
        self._smtp_server = None

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
        if enabled is not None:
          self.enabled = enabled
        if min_severity is not None:
          self.min_severity = min_severity
        if organization is not None:
          self.organization = organization
        if profiles is not None:
          self.profiles = profiles
        if sender_email is not None:
          self.sender_email = sender_email
        if smtp_port is not None:
          self.smtp_port = smtp_port
        if smtp_recipients is not None:
          self.smtp_recipients = smtp_recipients
        if smtp_server is not None:
          self.smtp_server = smtp_server

    @property
    def account_moid(self):
        """
        Gets the account_moid of this SmtpPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this SmtpPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this SmtpPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this SmtpPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this SmtpPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this SmtpPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this SmtpPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this SmtpPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this SmtpPolicy.
        The time when this managed object was created.  

        :return: The create_time of this SmtpPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this SmtpPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this SmtpPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this SmtpPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this SmtpPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this SmtpPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this SmtpPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this SmtpPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this SmtpPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this SmtpPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this SmtpPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this SmtpPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this SmtpPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SmtpPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this SmtpPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this SmtpPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this SmtpPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this SmtpPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this SmtpPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this SmtpPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this SmtpPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SmtpPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this SmtpPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this SmtpPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this SmtpPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SmtpPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this SmtpPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this SmtpPolicy.
        The versioning info for this managed object   

        :return: The version_context of this SmtpPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this SmtpPolicy.
        The versioning info for this managed object   

        :param version_context: The version_context of this SmtpPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this SmtpPolicy.
        Description of the policy.  

        :return: The description of this SmtpPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SmtpPolicy.
        Description of the policy.  

        :param description: The description of this SmtpPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this SmtpPolicy.
        Name of the policy.   

        :return: The name of this SmtpPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SmtpPolicy.
        Name of the policy.   

        :param name: The name of this SmtpPolicy.
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """
        Gets the enabled of this SmtpPolicy.
        If enabled, controls the state of the SMTP client service on the managed device  

        :return: The enabled of this SmtpPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SmtpPolicy.
        If enabled, controls the state of the SMTP client service on the managed device  

        :param enabled: The enabled of this SmtpPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def min_severity(self):
        """
        Gets the min_severity of this SmtpPolicy.
        Minimum fault severity level to receive email notifications. Email notifications are sent for all faults whose severity is equal to or greater than the chosen level.  

        :return: The min_severity of this SmtpPolicy.
        :rtype: str
        """
        return self._min_severity

    @min_severity.setter
    def min_severity(self, min_severity):
        """
        Sets the min_severity of this SmtpPolicy.
        Minimum fault severity level to receive email notifications. Email notifications are sent for all faults whose severity is equal to or greater than the chosen level.  

        :param min_severity: The min_severity of this SmtpPolicy.
        :type: str
        """
        allowed_values = ["critical", "condition", "warning", "minor", "major"]
        if min_severity not in allowed_values:
            raise ValueError(
                "Invalid value for `min_severity` ({0}), must be one of {1}"
                .format(min_severity, allowed_values)
            )

        self._min_severity = min_severity

    @property
    def organization(self):
        """
        Gets the organization of this SmtpPolicy.
        Organization 

        :return: The organization of this SmtpPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this SmtpPolicy.
        Organization 

        :param organization: The organization of this SmtpPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def profiles(self):
        """
        Gets the profiles of this SmtpPolicy.
        Relationship to the profile object 

        :return: The profiles of this SmtpPolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this SmtpPolicy.
        Relationship to the profile object 

        :param profiles: The profiles of this SmtpPolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

    @property
    def sender_email(self):
        """
        Gets the sender_email of this SmtpPolicy.
        The email address entered here will be displayed as the from address(mail received from address) of all the SMTP mail alerts that are received. If not configured, the hostname of the server is used in the from address field.  

        :return: The sender_email of this SmtpPolicy.
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """
        Sets the sender_email of this SmtpPolicy.
        The email address entered here will be displayed as the from address(mail received from address) of all the SMTP mail alerts that are received. If not configured, the hostname of the server is used in the from address field.  

        :param sender_email: The sender_email of this SmtpPolicy.
        :type: str
        """

        self._sender_email = sender_email

    @property
    def smtp_port(self):
        """
        Gets the smtp_port of this SmtpPolicy.
        Port number used by the SMTP server for outgoing SMTP communication  

        :return: The smtp_port of this SmtpPolicy.
        :rtype: int
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        """
        Sets the smtp_port of this SmtpPolicy.
        Port number used by the SMTP server for outgoing SMTP communication  

        :param smtp_port: The smtp_port of this SmtpPolicy.
        :type: int
        """

        self._smtp_port = smtp_port

    @property
    def smtp_recipients(self):
        """
        Gets the smtp_recipients of this SmtpPolicy.
        List of email addresses that will receive notifications for faults  

        :return: The smtp_recipients of this SmtpPolicy.
        :rtype: list[str]
        """
        return self._smtp_recipients

    @smtp_recipients.setter
    def smtp_recipients(self, smtp_recipients):
        """
        Sets the smtp_recipients of this SmtpPolicy.
        List of email addresses that will receive notifications for faults  

        :param smtp_recipients: The smtp_recipients of this SmtpPolicy.
        :type: list[str]
        """

        self._smtp_recipients = smtp_recipients

    @property
    def smtp_server(self):
        """
        Gets the smtp_server of this SmtpPolicy.
        IP address or hostname of the SMTP server. The SMTP server is used by the managed device to send email notifications.   

        :return: The smtp_server of this SmtpPolicy.
        :rtype: str
        """
        return self._smtp_server

    @smtp_server.setter
    def smtp_server(self, smtp_server):
        """
        Sets the smtp_server of this SmtpPolicy.
        IP address or hostname of the SMTP server. The SMTP server is used by the managed device to send email notifications.   

        :param smtp_server: The smtp_server of this SmtpPolicy.
        :type: str
        """

        self._smtp_server = smtp_server

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
        if not isinstance(other, SmtpPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
