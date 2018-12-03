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


class DevopsNotificationTrigger(object):
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
        'account': 'str',
        'domain_group': 'str',
        'mo_type': 'str',
        'modification_type': 'str',
        'moid': 'str',
        'security_context_subject': 'str',
        'security_context_type': 'str'
    }

    attribute_map = {
        'account': 'Account',
        'domain_group': 'DomainGroup',
        'mo_type': 'MoType',
        'modification_type': 'ModificationType',
        'moid': 'Moid',
        'security_context_subject': 'SecurityContextSubject',
        'security_context_type': 'SecurityContextType'
    }

    def __init__(self, account=None, domain_group=None, mo_type=None, modification_type='Update', moid=None, security_context_subject=None, security_context_type='AccountContext'):
        """
        DevopsNotificationTrigger - a model defined in Swagger
        """

        self._account = None
        self._domain_group = None
        self._mo_type = None
        self._modification_type = None
        self._moid = None
        self._security_context_subject = None
        self._security_context_type = None

        if account is not None:
          self.account = account
        if domain_group is not None:
          self.domain_group = domain_group
        if mo_type is not None:
          self.mo_type = mo_type
        if modification_type is not None:
          self.modification_type = modification_type
        if moid is not None:
          self.moid = moid
        if security_context_subject is not None:
          self.security_context_subject = security_context_subject
        if security_context_type is not None:
          self.security_context_type = security_context_type

    @property
    def account(self):
        """
        Gets the account of this DevopsNotificationTrigger.
        The Moid of the Account to which the MO identified by the 'moid' field belonged. This field is mandatory when modificationType is Delete and is ignored for other values of modificationType. 

        :return: The account of this DevopsNotificationTrigger.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this DevopsNotificationTrigger.
        The Moid of the Account to which the MO identified by the 'moid' field belonged. This field is mandatory when modificationType is Delete and is ignored for other values of modificationType. 

        :param account: The account of this DevopsNotificationTrigger.
        :type: str
        """

        self._account = account

    @property
    def domain_group(self):
        """
        Gets the domain_group of this DevopsNotificationTrigger.
        The Moid of the DomainGroup to which the MO identified by the 'moid' field belonged. This field is mandatory when modificationType is Delete and is ignored for other values of modificationType. 

        :return: The domain_group of this DevopsNotificationTrigger.
        :rtype: str
        """
        return self._domain_group

    @domain_group.setter
    def domain_group(self, domain_group):
        """
        Sets the domain_group of this DevopsNotificationTrigger.
        The Moid of the DomainGroup to which the MO identified by the 'moid' field belonged. This field is mandatory when modificationType is Delete and is ignored for other values of modificationType. 

        :param domain_group: The domain_group of this DevopsNotificationTrigger.
        :type: str
        """

        self._domain_group = domain_group

    @property
    def mo_type(self):
        """
        Gets the mo_type of this DevopsNotificationTrigger.
        The type of the MO such as iam.Account.  

        :return: The mo_type of this DevopsNotificationTrigger.
        :rtype: str
        """
        return self._mo_type

    @mo_type.setter
    def mo_type(self, mo_type):
        """
        Sets the mo_type of this DevopsNotificationTrigger.
        The type of the MO such as iam.Account.  

        :param mo_type: The mo_type of this DevopsNotificationTrigger.
        :type: str
        """

        self._mo_type = mo_type

    @property
    def modification_type(self):
        """
        Gets the modification_type of this DevopsNotificationTrigger.
        Indicates the type of change notification.  

        :return: The modification_type of this DevopsNotificationTrigger.
        :rtype: str
        """
        return self._modification_type

    @modification_type.setter
    def modification_type(self, modification_type):
        """
        Sets the modification_type of this DevopsNotificationTrigger.
        Indicates the type of change notification.  

        :param modification_type: The modification_type of this DevopsNotificationTrigger.
        :type: str
        """
        allowed_values = ["Update", "Create", "Read", "Delete"]
        if modification_type not in allowed_values:
            raise ValueError(
                "Invalid value for `modification_type` ({0}), must be one of {1}"
                .format(modification_type, allowed_values)
            )

        self._modification_type = modification_type

    @property
    def moid(self):
        """
        Gets the moid of this DevopsNotificationTrigger.
        The Moid of the MO.  

        :return: The moid of this DevopsNotificationTrigger.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this DevopsNotificationTrigger.
        The Moid of the MO.  

        :param moid: The moid of this DevopsNotificationTrigger.
        :type: str
        """

        self._moid = moid

    @property
    def security_context_subject(self):
        """
        Gets the security_context_subject of this DevopsNotificationTrigger.
        A securityContextSubject must be specified when the securityContextType is AccountContext or DeviceContext. The field is the Moid of the respective iam.Account of asset.DeviceRegistration. 

        :return: The security_context_subject of this DevopsNotificationTrigger.
        :rtype: str
        """
        return self._security_context_subject

    @security_context_subject.setter
    def security_context_subject(self, security_context_subject):
        """
        Sets the security_context_subject of this DevopsNotificationTrigger.
        A securityContextSubject must be specified when the securityContextType is AccountContext or DeviceContext. The field is the Moid of the respective iam.Account of asset.DeviceRegistration. 

        :param security_context_subject: The security_context_subject of this DevopsNotificationTrigger.
        :type: str
        """

        self._security_context_subject = security_context_subject

    @property
    def security_context_type(self):
        """
        Gets the security_context_type of this DevopsNotificationTrigger.
        In some scenarios it is necessary for change notifications to be processed in SystemContext. For example, when a device is claimed or unclaimed the notification must execute in SystemContext in order to move MOs related to the device between accounts. 

        :return: The security_context_type of this DevopsNotificationTrigger.
        :rtype: str
        """
        return self._security_context_type

    @security_context_type.setter
    def security_context_type(self, security_context_type):
        """
        Sets the security_context_type of this DevopsNotificationTrigger.
        In some scenarios it is necessary for change notifications to be processed in SystemContext. For example, when a device is claimed or unclaimed the notification must execute in SystemContext in order to move MOs related to the device between accounts. 

        :param security_context_type: The security_context_type of this DevopsNotificationTrigger.
        :type: str
        """
        allowed_values = ["AccountContext", "SystemContext", "DeviceContext"]
        if security_context_type not in allowed_values:
            raise ValueError(
                "Invalid value for `security_context_type` ({0}), must be one of {1}"
                .format(security_context_type, allowed_values)
            )

        self._security_context_type = security_context_type

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
        if not isinstance(other, DevopsNotificationTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
