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


class FeedbackFeedbackData(object):
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
        'comment': 'str',
        'email': 'str',
        'evaluation': 'str',
        'follow_up': 'bool',
        'trace_ids': 'object',
        'type': 'str'
    }

    attribute_map = {
        'comment': 'Comment',
        'email': 'Email',
        'evaluation': 'Evaluation',
        'follow_up': 'FollowUp',
        'trace_ids': 'TraceIds',
        'type': 'Type'
    }

    def __init__(self, comment=None, email=None, evaluation='Excellent', follow_up=None, trace_ids=None, type='Evaluation'):
        """
        FeedbackFeedbackData - a model defined in Swagger
        """

        self._comment = None
        self._email = None
        self._evaluation = None
        self._follow_up = None
        self._trace_ids = None
        self._type = None

        if comment is not None:
          self.comment = comment
        if email is not None:
          self.email = email
        if evaluation is not None:
          self.evaluation = evaluation
        if follow_up is not None:
          self.follow_up = follow_up
        if trace_ids is not None:
          self.trace_ids = trace_ids
        if type is not None:
          self.type = type

    @property
    def comment(self):
        """
        Gets the comment of this FeedbackFeedbackData.
        Text of the feedback  

        :return: The comment of this FeedbackFeedbackData.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this FeedbackFeedbackData.
        Text of the feedback  

        :param comment: The comment of this FeedbackFeedbackData.
        :type: str
        """

        self._comment = comment

    @property
    def email(self):
        """
        Gets the email of this FeedbackFeedbackData.
        user email  

        :return: The email of this FeedbackFeedbackData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this FeedbackFeedbackData.
        user email  

        :param email: The email of this FeedbackFeedbackData.
        :type: str
        """

        self._email = email

    @property
    def evaluation(self):
        """
        Gets the evaluation of this FeedbackFeedbackData.
        evaluation type  

        :return: The evaluation of this FeedbackFeedbackData.
        :rtype: str
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        """
        Sets the evaluation of this FeedbackFeedbackData.
        evaluation type  

        :param evaluation: The evaluation of this FeedbackFeedbackData.
        :type: str
        """
        allowed_values = ["Excellent", "Poor", "Fair", "Good"]
        if evaluation not in allowed_values:
            raise ValueError(
                "Invalid value for `evaluation` ({0}), must be one of {1}"
                .format(evaluation, allowed_values)
            )

        self._evaluation = evaluation

    @property
    def follow_up(self):
        """
        Gets the follow_up of this FeedbackFeedbackData.
        if user open for follow-up or not  

        :return: The follow_up of this FeedbackFeedbackData.
        :rtype: bool
        """
        return self._follow_up

    @follow_up.setter
    def follow_up(self, follow_up):
        """
        Sets the follow_up of this FeedbackFeedbackData.
        if user open for follow-up or not  

        :param follow_up: The follow_up of this FeedbackFeedbackData.
        :type: bool
        """

        self._follow_up = follow_up

    @property
    def trace_ids(self):
        """
        Gets the trace_ids of this FeedbackFeedbackData.
        Bunch of last traceId for reproducing user last activity  

        :return: The trace_ids of this FeedbackFeedbackData.
        :rtype: object
        """
        return self._trace_ids

    @trace_ids.setter
    def trace_ids(self, trace_ids):
        """
        Sets the trace_ids of this FeedbackFeedbackData.
        Bunch of last traceId for reproducing user last activity  

        :param trace_ids: The trace_ids of this FeedbackFeedbackData.
        :type: object
        """

        self._trace_ids = trace_ids

    @property
    def type(self):
        """
        Gets the type of this FeedbackFeedbackData.
        Type from user   

        :return: The type of this FeedbackFeedbackData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FeedbackFeedbackData.
        Type from user   

        :param type: The type of this FeedbackFeedbackData.
        :type: str
        """
        allowed_values = ["Evaluation", "Bug"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, FeedbackFeedbackData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
