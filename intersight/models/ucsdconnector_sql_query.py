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


class UcsdconnectorSqlQuery(object):
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
        'params': 'object',
        'query': 'str'
    }

    attribute_map = {
        'params': 'Params',
        'query': 'Query'
    }

    def __init__(self, params=None, query=None):
        """
        UcsdconnectorSqlQuery - a model defined in Swagger
        """

        self._params = None
        self._query = None

        if params is not None:
          self.params = params
        if query is not None:
          self.query = query

    @property
    def params(self):
        """
        Gets the params of this UcsdconnectorSqlQuery.
        Parameters in query string  

        :return: The params of this UcsdconnectorSqlQuery.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this UcsdconnectorSqlQuery.
        Parameters in query string  

        :param params: The params of this UcsdconnectorSqlQuery.
        :type: object
        """

        self._params = params

    @property
    def query(self):
        """
        Gets the query of this UcsdconnectorSqlQuery.
        query string   

        :return: The query of this UcsdconnectorSqlQuery.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this UcsdconnectorSqlQuery.
        query string   

        :param query: The query of this UcsdconnectorSqlQuery.
        :type: str
        """

        self._query = query

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
        if not isinstance(other, UcsdconnectorSqlQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
