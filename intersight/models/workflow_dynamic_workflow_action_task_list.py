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


class WorkflowDynamicWorkflowActionTaskList(object):
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
        'action': 'str',
        'tasks': 'object'
    }

    attribute_map = {
        'action': 'Action',
        'tasks': 'Tasks'
    }

    def __init__(self, action=None, tasks=None):
        """
        WorkflowDynamicWorkflowActionTaskList - a model defined in Swagger
        """

        self._action = None
        self._tasks = None

        if action is not None:
          self.action = action
        if tasks is not None:
          self.tasks = tasks

    @property
    def action(self):
        """
        Gets the action of this WorkflowDynamicWorkflowActionTaskList.
        The action of the Dynamic Workflow  

        :return: The action of this WorkflowDynamicWorkflowActionTaskList.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this WorkflowDynamicWorkflowActionTaskList.
        The action of the Dynamic Workflow  

        :param action: The action of this WorkflowDynamicWorkflowActionTaskList.
        :type: str
        """

        self._action = action

    @property
    def tasks(self):
        """
        Gets the tasks of this WorkflowDynamicWorkflowActionTaskList.
        The task list that has precedences as well.   

        :return: The tasks of this WorkflowDynamicWorkflowActionTaskList.
        :rtype: object
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this WorkflowDynamicWorkflowActionTaskList.
        The task list that has precedences as well.   

        :param tasks: The tasks of this WorkflowDynamicWorkflowActionTaskList.
        :type: object
        """

        self._tasks = tasks

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
        if not isinstance(other, WorkflowDynamicWorkflowActionTaskList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
