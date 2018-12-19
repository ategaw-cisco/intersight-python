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


class WorkflowTaskRetryInfo(object):
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
        'status': 'str',
        'task_inst_id': 'str'
    }

    attribute_map = {
        'status': 'Status',
        'task_inst_id': 'TaskInstId'
    }

    def __init__(self, status=None, task_inst_id=None):
        """
        WorkflowTaskRetryInfo - a model defined in Swagger
        """

        self._status = None
        self._task_inst_id = None

        if status is not None:
          self.status = status
        if task_inst_id is not None:
          self.task_inst_id = task_inst_id

    @property
    def status(self):
        """
        Gets the status of this WorkflowTaskRetryInfo.
        Retried task status  

        :return: The status of this WorkflowTaskRetryInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkflowTaskRetryInfo.
        Retried task status  

        :param status: The status of this WorkflowTaskRetryInfo.
        :type: str
        """

        self._status = status

    @property
    def task_inst_id(self):
        """
        Gets the task_inst_id of this WorkflowTaskRetryInfo.
        Retried task instance Id   

        :return: The task_inst_id of this WorkflowTaskRetryInfo.
        :rtype: str
        """
        return self._task_inst_id

    @task_inst_id.setter
    def task_inst_id(self, task_inst_id):
        """
        Sets the task_inst_id of this WorkflowTaskRetryInfo.
        Retried task instance Id   

        :param task_inst_id: The task_inst_id of this WorkflowTaskRetryInfo.
        :type: str
        """

        self._task_inst_id = task_inst_id

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
        if not isinstance(other, WorkflowTaskRetryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
