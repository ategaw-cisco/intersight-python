# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-300
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FirmwareUpgradeStatus(object):
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
        'download_error': 'str',
        'download_percentage': 'int',
        'download_stage': 'str',
        'download_status': 'str',
        'ep_power_status': 'str',
        'overall_error': 'str',
        'overall_percentage': 'int',
        'overallstatus': 'str',
        'pending_type': 'str',
        'upgrade': 'FirmwareUpgradeRef'
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
        'download_error': 'DownloadError',
        'download_percentage': 'DownloadPercentage',
        'download_stage': 'DownloadStage',
        'download_status': 'DownloadStatus',
        'ep_power_status': 'EpPowerStatus',
        'overall_error': 'OverallError',
        'overall_percentage': 'OverallPercentage',
        'overallstatus': 'Overallstatus',
        'pending_type': 'PendingType',
        'upgrade': 'Upgrade'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, download_error=None, download_percentage=None, download_stage=None, download_status=None, ep_power_status='none', overall_error=None, overall_percentage=None, overallstatus='none', pending_type='none', upgrade=None):
        """
        FirmwareUpgradeStatus - a model defined in Swagger
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
        self._download_error = None
        self._download_percentage = None
        self._download_stage = None
        self._download_status = None
        self._ep_power_status = None
        self._overall_error = None
        self._overall_percentage = None
        self._overallstatus = None
        self._pending_type = None
        self._upgrade = None

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
        if download_error is not None:
          self.download_error = download_error
        if download_percentage is not None:
          self.download_percentage = download_percentage
        if download_stage is not None:
          self.download_stage = download_stage
        if download_status is not None:
          self.download_status = download_status
        if ep_power_status is not None:
          self.ep_power_status = ep_power_status
        if overall_error is not None:
          self.overall_error = overall_error
        if overall_percentage is not None:
          self.overall_percentage = overall_percentage
        if overallstatus is not None:
          self.overallstatus = overallstatus
        if pending_type is not None:
          self.pending_type = pending_type
        if upgrade is not None:
          self.upgrade = upgrade

    @property
    def account_moid(self):
        """
        Gets the account_moid of this FirmwareUpgradeStatus.
        The Account ID for this managed object.  

        :return: The account_moid of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this FirmwareUpgradeStatus.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this FirmwareUpgradeStatus.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this FirmwareUpgradeStatus.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this FirmwareUpgradeStatus.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this FirmwareUpgradeStatus.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this FirmwareUpgradeStatus.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this FirmwareUpgradeStatus.
        The time when this managed object was created.  

        :return: The create_time of this FirmwareUpgradeStatus.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this FirmwareUpgradeStatus.
        The time when this managed object was created.  

        :param create_time: The create_time of this FirmwareUpgradeStatus.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this FirmwareUpgradeStatus.
        The time when this managed object was last modified.  

        :return: The mod_time of this FirmwareUpgradeStatus.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this FirmwareUpgradeStatus.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this FirmwareUpgradeStatus.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this FirmwareUpgradeStatus.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this FirmwareUpgradeStatus.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this FirmwareUpgradeStatus.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this FirmwareUpgradeStatus.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this FirmwareUpgradeStatus.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this FirmwareUpgradeStatus.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this FirmwareUpgradeStatus.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this FirmwareUpgradeStatus.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this FirmwareUpgradeStatus.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this FirmwareUpgradeStatus.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this FirmwareUpgradeStatus.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this FirmwareUpgradeStatus.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this FirmwareUpgradeStatus.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this FirmwareUpgradeStatus.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this FirmwareUpgradeStatus.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this FirmwareUpgradeStatus.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this FirmwareUpgradeStatus.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this FirmwareUpgradeStatus.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this FirmwareUpgradeStatus.
        The versioning info for this managed object.   

        :return: The version_context of this FirmwareUpgradeStatus.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this FirmwareUpgradeStatus.
        The versioning info for this managed object.   

        :param version_context: The version_context of this FirmwareUpgradeStatus.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def download_error(self):
        """
        Gets the download_error of this FirmwareUpgradeStatus.
        Provides the download failure message  

        :return: The download_error of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._download_error

    @download_error.setter
    def download_error(self, download_error):
        """
        Sets the download_error of this FirmwareUpgradeStatus.
        Provides the download failure message  

        :param download_error: The download_error of this FirmwareUpgradeStatus.
        :type: str
        """

        self._download_error = download_error

    @property
    def download_percentage(self):
        """
        Gets the download_percentage of this FirmwareUpgradeStatus.
        Provides the image downloaded percentage from image source  

        :return: The download_percentage of this FirmwareUpgradeStatus.
        :rtype: int
        """
        return self._download_percentage

    @download_percentage.setter
    def download_percentage(self, download_percentage):
        """
        Sets the download_percentage of this FirmwareUpgradeStatus.
        Provides the image downloaded percentage from image source  

        :param download_percentage: The download_percentage of this FirmwareUpgradeStatus.
        :type: int
        """

        self._download_percentage = download_percentage

    @property
    def download_stage(self):
        """
        Gets the download_stage of this FirmwareUpgradeStatus.
        Provides the latest download phase like downloading, flashing, downloaded  

        :return: The download_stage of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._download_stage

    @download_stage.setter
    def download_stage(self, download_stage):
        """
        Sets the download_stage of this FirmwareUpgradeStatus.
        Provides the latest download phase like downloading, flashing, downloaded  

        :param download_stage: The download_stage of this FirmwareUpgradeStatus.
        :type: str
        """

        self._download_stage = download_stage

    @property
    def download_status(self):
        """
        Gets the download_status of this FirmwareUpgradeStatus.
        Provides the download status like downloading, downloaded or failed  

        :return: The download_status of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._download_status

    @download_status.setter
    def download_status(self, download_status):
        """
        Sets the download_status of this FirmwareUpgradeStatus.
        Provides the download status like downloading, downloaded or failed  

        :param download_status: The download_status of this FirmwareUpgradeStatus.
        :type: str
        """

        self._download_status = download_status

    @property
    def ep_power_status(self):
        """
        Gets the ep_power_status of this FirmwareUpgradeStatus.
        Provides the server power status at the end of upgrade  

        :return: The ep_power_status of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._ep_power_status

    @ep_power_status.setter
    def ep_power_status(self, ep_power_status):
        """
        Sets the ep_power_status of this FirmwareUpgradeStatus.
        Provides the server power status at the end of upgrade  

        :param ep_power_status: The ep_power_status of this FirmwareUpgradeStatus.
        :type: str
        """
        allowed_values = ["none", "powered on", "powered off"]
        if ep_power_status not in allowed_values:
            raise ValueError(
                "Invalid value for `ep_power_status` ({0}), must be one of {1}"
                .format(ep_power_status, allowed_values)
            )

        self._ep_power_status = ep_power_status

    @property
    def overall_error(self):
        """
        Gets the overall_error of this FirmwareUpgradeStatus.
        Provides the failure message when download or upgrade fails  

        :return: The overall_error of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._overall_error

    @overall_error.setter
    def overall_error(self, overall_error):
        """
        Sets the overall_error of this FirmwareUpgradeStatus.
        Provides the failure message when download or upgrade fails  

        :param overall_error: The overall_error of this FirmwareUpgradeStatus.
        :type: str
        """

        self._overall_error = overall_error

    @property
    def overall_percentage(self):
        """
        Gets the overall_percentage of this FirmwareUpgradeStatus.
        Provides the overall percentage of the upgrade inclusive of download  

        :return: The overall_percentage of this FirmwareUpgradeStatus.
        :rtype: int
        """
        return self._overall_percentage

    @overall_percentage.setter
    def overall_percentage(self, overall_percentage):
        """
        Sets the overall_percentage of this FirmwareUpgradeStatus.
        Provides the overall percentage of the upgrade inclusive of download  

        :param overall_percentage: The overall_percentage of this FirmwareUpgradeStatus.
        :type: int
        """

        self._overall_percentage = overall_percentage

    @property
    def overallstatus(self):
        """
        Gets the overallstatus of this FirmwareUpgradeStatus.
        Provides the overall status, e.g., downloading, upgrading, successful, failure and pending-for-reboot  

        :return: The overallstatus of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._overallstatus

    @overallstatus.setter
    def overallstatus(self, overallstatus):
        """
        Sets the overallstatus of this FirmwareUpgradeStatus.
        Provides the overall status, e.g., downloading, upgrading, successful, failure and pending-for-reboot  

        :param overallstatus: The overallstatus of this FirmwareUpgradeStatus.
        :type: str
        """
        allowed_values = ["none", "started", "download initiating", "download initiated", "downloading", "downloaded", "upgrade initiating", "upgrade initiated", "upgrading", "upgraded", "success", "failed", "pending"]
        if overallstatus not in allowed_values:
            raise ValueError(
                "Invalid value for `overallstatus` ({0}), must be one of {1}"
                .format(overallstatus, allowed_values)
            )

        self._overallstatus = overallstatus

    @property
    def pending_type(self):
        """
        Gets the pending_type of this FirmwareUpgradeStatus.
        Provides the current pending upgrade status for the on-next boot based upgrades   

        :return: The pending_type of this FirmwareUpgradeStatus.
        :rtype: str
        """
        return self._pending_type

    @pending_type.setter
    def pending_type(self, pending_type):
        """
        Sets the pending_type of this FirmwareUpgradeStatus.
        Provides the current pending upgrade status for the on-next boot based upgrades   

        :param pending_type: The pending_type of this FirmwareUpgradeStatus.
        :type: str
        """
        allowed_values = ["none", "pending for next reboot"]
        if pending_type not in allowed_values:
            raise ValueError(
                "Invalid value for `pending_type` ({0}), must be one of {1}"
                .format(pending_type, allowed_values)
            )

        self._pending_type = pending_type

    @property
    def upgrade(self):
        """
        Gets the upgrade of this FirmwareUpgradeStatus.
        A collection of references to the [firmware.Upgrade](mo://firmware.Upgrade) Managed Object.  When this managed object is deleted, the referenced [firmware.Upgrade](mo://firmware.Upgrade) MO unsets its reference to this deleted MO. 

        :return: The upgrade of this FirmwareUpgradeStatus.
        :rtype: FirmwareUpgradeRef
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """
        Sets the upgrade of this FirmwareUpgradeStatus.
        A collection of references to the [firmware.Upgrade](mo://firmware.Upgrade) Managed Object.  When this managed object is deleted, the referenced [firmware.Upgrade](mo://firmware.Upgrade) MO unsets its reference to this deleted MO. 

        :param upgrade: The upgrade of this FirmwareUpgradeStatus.
        :type: FirmwareUpgradeRef
        """

        self._upgrade = upgrade

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
        if not isinstance(other, FirmwareUpgradeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
