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


class UcsdconnectorTelemetryMo(object):
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
        'field_queries': 'list[UcsdconnectorFieldQuery]',
        'mo_name': 'str',
        'object_query': 'UcsdconnectorSqlQuery'
    }

    attribute_map = {
        'field_queries': 'FieldQueries',
        'mo_name': 'MoName',
        'object_query': 'ObjectQuery'
    }

    def __init__(self, field_queries=None, mo_name=None, object_query=None):
        """
        UcsdconnectorTelemetryMo - a model defined in Swagger
        """

        self._field_queries = None
        self._mo_name = None
        self._object_query = None

        if field_queries is not None:
          self.field_queries = field_queries
        if mo_name is not None:
          self.mo_name = mo_name
        if object_query is not None:
          self.object_query = object_query

    @property
    def field_queries(self):
        """
        Gets the field_queries of this UcsdconnectorTelemetryMo.
        Its a collection of FieldQuery objects  

        :return: The field_queries of this UcsdconnectorTelemetryMo.
        :rtype: list[UcsdconnectorFieldQuery]
        """
        return self._field_queries

    @field_queries.setter
    def field_queries(self, field_queries):
        """
        Sets the field_queries of this UcsdconnectorTelemetryMo.
        Its a collection of FieldQuery objects  

        :param field_queries: The field_queries of this UcsdconnectorTelemetryMo.
        :type: list[UcsdconnectorFieldQuery]
        """

        self._field_queries = field_queries

    @property
    def mo_name(self):
        """
        Gets the mo_name of this UcsdconnectorTelemetryMo.
        MoName corresponds to Fanwood telemetry Mo  

        :return: The mo_name of this UcsdconnectorTelemetryMo.
        :rtype: str
        """
        return self._mo_name

    @mo_name.setter
    def mo_name(self, mo_name):
        """
        Sets the mo_name of this UcsdconnectorTelemetryMo.
        MoName corresponds to Fanwood telemetry Mo  

        :param mo_name: The mo_name of this UcsdconnectorTelemetryMo.
        :type: str
        """

        self._mo_name = mo_name

    @property
    def object_query(self):
        """
        Gets the object_query of this UcsdconnectorTelemetryMo.
        It contains a single SQL Query that collects all the properties of a Mo   

        :return: The object_query of this UcsdconnectorTelemetryMo.
        :rtype: UcsdconnectorSqlQuery
        """
        return self._object_query

    @object_query.setter
    def object_query(self, object_query):
        """
        Sets the object_query of this UcsdconnectorTelemetryMo.
        It contains a single SQL Query that collects all the properties of a Mo   

        :param object_query: The object_query of this UcsdconnectorTelemetryMo.
        :type: UcsdconnectorSqlQuery
        """

        self._object_query = object_query

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
        if not isinstance(other, UcsdconnectorTelemetryMo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
