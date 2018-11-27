# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-260
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectorStartStream(object):
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
        'stream_name': 'str',
        'batch_size': 'int',
        'force_rebuild': 'bool',
        'input': 'str',
        'plugin_name': 'str',
        'poll_interval': 'int',
        'priority': 'int',
        'response_topic': 'str'
    }

    attribute_map = {
        'stream_name': 'StreamName',
        'batch_size': 'BatchSize',
        'force_rebuild': 'ForceRebuild',
        'input': 'Input',
        'plugin_name': 'PluginName',
        'poll_interval': 'PollInterval',
        'priority': 'Priority',
        'response_topic': 'ResponseTopic'
    }

    def __init__(self, stream_name=None, batch_size=None, force_rebuild=None, input=None, plugin_name=None, poll_interval=None, priority=None, response_topic=None):
        """
        ConnectorStartStream - a model defined in Swagger
        """

        self._stream_name = None
        self._batch_size = None
        self._force_rebuild = None
        self._input = None
        self._plugin_name = None
        self._poll_interval = None
        self._priority = None
        self._response_topic = None

        if stream_name is not None:
          self.stream_name = stream_name
        if batch_size is not None:
          self.batch_size = batch_size
        if force_rebuild is not None:
          self.force_rebuild = force_rebuild
        if input is not None:
          self.input = input
        if plugin_name is not None:
          self.plugin_name = plugin_name
        if poll_interval is not None:
          self.poll_interval = poll_interval
        if priority is not None:
          self.priority = priority
        if response_topic is not None:
          self.response_topic = response_topic

    @property
    def stream_name(self):
        """
        Gets the stream_name of this ConnectorStartStream.
        The requested stream name. Stream names are unique per device endpoint.   

        :return: The stream_name of this ConnectorStartStream.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ConnectorStartStream.
        The requested stream name. Stream names are unique per device endpoint.   

        :param stream_name: The stream_name of this ConnectorStartStream.
        :type: str
        """

        self._stream_name = stream_name

    @property
    def batch_size(self):
        """
        Gets the batch_size of this ConnectorStartStream.
        The number of outputs from a plugin to collect into a single message. Applicable only to streams that involve polling plugins and plugins which support emitting batchable data. Default value of zero indicates no batching.  

        :return: The batch_size of this ConnectorStartStream.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """
        Sets the batch_size of this ConnectorStartStream.
        The number of outputs from a plugin to collect into a single message. Applicable only to streams that involve polling plugins and plugins which support emitting batchable data. Default value of zero indicates no batching.  

        :param batch_size: The batch_size of this ConnectorStartStream.
        :type: int
        """

        self._batch_size = batch_size

    @property
    def force_rebuild(self):
        """
        Gets the force_rebuild of this ConnectorStartStream.
        Flag to force a rebuild of an existing stream. To be used if a stream is unable to recover itself in response to dropped messages.  

        :return: The force_rebuild of this ConnectorStartStream.
        :rtype: bool
        """
        return self._force_rebuild

    @force_rebuild.setter
    def force_rebuild(self, force_rebuild):
        """
        Sets the force_rebuild of this ConnectorStartStream.
        Flag to force a rebuild of an existing stream. To be used if a stream is unable to recover itself in response to dropped messages.  

        :param force_rebuild: The force_rebuild of this ConnectorStartStream.
        :type: bool
        """

        self._force_rebuild = force_rebuild

    @property
    def input(self):
        """
        Gets the input of this ConnectorStartStream.
        Input to the plugin to start the start the stream or collect stream messages.  

        :return: The input of this ConnectorStartStream.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this ConnectorStartStream.
        Input to the plugin to start the start the stream or collect stream messages.  

        :param input: The input of this ConnectorStartStream.
        :type: str
        """

        self._input = input

    @property
    def plugin_name(self):
        """
        Gets the plugin_name of this ConnectorStartStream.
        The plugin to run the stream on  

        :return: The plugin_name of this ConnectorStartStream.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """
        Sets the plugin_name of this ConnectorStartStream.
        The plugin to run the stream on  

        :param plugin_name: The plugin_name of this ConnectorStartStream.
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def poll_interval(self):
        """
        Gets the poll_interval of this ConnectorStartStream.
        The desired interval to emit messages from this stream. The stream plugin will poll plugins at this interval to create a stream event.  

        :return: The poll_interval of this ConnectorStartStream.
        :rtype: int
        """
        return self._poll_interval

    @poll_interval.setter
    def poll_interval(self, poll_interval):
        """
        Sets the poll_interval of this ConnectorStartStream.
        The desired interval to emit messages from this stream. The stream plugin will poll plugins at this interval to create a stream event.  

        :param poll_interval: The poll_interval of this ConnectorStartStream.
        :type: int
        """

        self._poll_interval = poll_interval

    @property
    def priority(self):
        """
        Gets the priority of this ConnectorStartStream.
        The priority level to apply to messages emitted by this stream  

        :return: The priority of this ConnectorStartStream.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this ConnectorStartStream.
        The priority level to apply to messages emitted by this stream  

        :param priority: The priority of this ConnectorStartStream.
        :type: int
        """

        self._priority = priority

    @property
    def response_topic(self):
        """
        Gets the response_topic of this ConnectorStartStream.
        The topic for the device connector to publish messages to.   

        :return: The response_topic of this ConnectorStartStream.
        :rtype: str
        """
        return self._response_topic

    @response_topic.setter
    def response_topic(self, response_topic):
        """
        Sets the response_topic of this ConnectorStartStream.
        The topic for the device connector to publish messages to.   

        :param response_topic: The response_topic of this ConnectorStartStream.
        :type: str
        """

        self._response_topic = response_topic

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
        if not isinstance(other, ConnectorStartStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
