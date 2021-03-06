# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-262
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class EquipmentLocatorLedApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def equipment_locator_leds_get(self, **kwargs):
        """
        Get a list of 'equipmentLocatorLed' instances
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool count: The $count query option allows clients to request a count of the matching resources.
        :param str inlinecount: The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response
        :param int top: The max number of records to return
        :param int skip: The number of records to skip
        :param str filter: Filter criteria for records to return. A URI with a $filter System Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in $filter operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. Query examples: $filter=Name eq 'Bob' $filter=Tags/any(t: t/Key eq 'Site') $filter=Tags/any(t: t/Key eq 'Site' and t/Value eq 'London') 
        :param str select: Specifies a subset of properties to return
        :param str orderby: Determines what values are used to order a collection of records
        :param str expand: Specify additional attributes or related records to return. Supports only 'DisplayNames' attribute now. Query examples: $expand=DisplayNames 
        :param str apply: Specify one or more transformation operations to perform aggregation on records. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. Query examples: $apply=groupby((Model), aggregate($count as Total)) $apply=groupby((Model), aggregate(AvailableMemory with average as AverageAvailableMemory)) 
        :param str at: Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for records to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. Query examples: at=VersionType eq 'Configured' at=InterestedMos.Moid eq '5b5877e56c6730367acf46cd' 
        :return: EquipmentLocatorLedList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.equipment_locator_leds_get_with_http_info(**kwargs)
        else:
            (data) = self.equipment_locator_leds_get_with_http_info(**kwargs)
            return data

    def equipment_locator_leds_get_with_http_info(self, **kwargs):
        """
        Get a list of 'equipmentLocatorLed' instances
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool count: The $count query option allows clients to request a count of the matching resources.
        :param str inlinecount: The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response
        :param int top: The max number of records to return
        :param int skip: The number of records to skip
        :param str filter: Filter criteria for records to return. A URI with a $filter System Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in $filter operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. Query examples: $filter=Name eq 'Bob' $filter=Tags/any(t: t/Key eq 'Site') $filter=Tags/any(t: t/Key eq 'Site' and t/Value eq 'London') 
        :param str select: Specifies a subset of properties to return
        :param str orderby: Determines what values are used to order a collection of records
        :param str expand: Specify additional attributes or related records to return. Supports only 'DisplayNames' attribute now. Query examples: $expand=DisplayNames 
        :param str apply: Specify one or more transformation operations to perform aggregation on records. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. Query examples: $apply=groupby((Model), aggregate($count as Total)) $apply=groupby((Model), aggregate(AvailableMemory with average as AverageAvailableMemory)) 
        :param str at: Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for records to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. Query examples: at=VersionType eq 'Configured' at=InterestedMos.Moid eq '5b5877e56c6730367acf46cd' 
        :return: EquipmentLocatorLedList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'inlinecount', 'top', 'skip', 'filter', 'select', 'orderby', 'expand', 'apply', 'at']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method equipment_locator_leds_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('$count', params['count']))
        if 'inlinecount' in params:
            query_params.append(('$inlinecount', params['inlinecount']))
        if 'top' in params:
            query_params.append(('$top', params['top']))
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))
        if 'filter' in params:
            query_params.append(('$filter', params['filter']))
        if 'select' in params:
            query_params.append(('$select', params['select']))
        if 'orderby' in params:
            query_params.append(('$orderby', params['orderby']))
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))
        if 'apply' in params:
            query_params.append(('$apply', params['apply']))
        if 'at' in params:
            query_params.append(('at', params['at']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/equipment/LocatorLeds', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EquipmentLocatorLedList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def equipment_locator_leds_moid_get(self, moid, **kwargs):
        """
        Get a specific instance of 'equipmentLocatorLed'
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_moid_get(moid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str moid: The moid of the equipmentLocatorLed instance. (required)
        :return: EquipmentLocatorLed
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.equipment_locator_leds_moid_get_with_http_info(moid, **kwargs)
        else:
            (data) = self.equipment_locator_leds_moid_get_with_http_info(moid, **kwargs)
            return data

    def equipment_locator_leds_moid_get_with_http_info(self, moid, **kwargs):
        """
        Get a specific instance of 'equipmentLocatorLed'
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_moid_get_with_http_info(moid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str moid: The moid of the equipmentLocatorLed instance. (required)
        :return: EquipmentLocatorLed
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['moid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method equipment_locator_leds_moid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'moid' is set
        if ('moid' not in params) or (params['moid'] is None):
            raise ValueError("Missing the required parameter `moid` when calling `equipment_locator_leds_moid_get`")


        collection_formats = {}

        path_params = {}
        if 'moid' in params:
            path_params['moid'] = params['moid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/equipment/LocatorLeds/{moid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EquipmentLocatorLed',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def equipment_locator_leds_moid_patch(self, moid, body, **kwargs):
        """
        Update an instance of 'equipmentLocatorLed'
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_moid_patch(moid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str moid: The moid of the equipmentLocatorLed instance. (required)
        :param EquipmentLocatorLed body: equipmentLocatorLed to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.equipment_locator_leds_moid_patch_with_http_info(moid, body, **kwargs)
        else:
            (data) = self.equipment_locator_leds_moid_patch_with_http_info(moid, body, **kwargs)
            return data

    def equipment_locator_leds_moid_patch_with_http_info(self, moid, body, **kwargs):
        """
        Update an instance of 'equipmentLocatorLed'
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_moid_patch_with_http_info(moid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str moid: The moid of the equipmentLocatorLed instance. (required)
        :param EquipmentLocatorLed body: equipmentLocatorLed to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['moid', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method equipment_locator_leds_moid_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'moid' is set
        if ('moid' not in params) or (params['moid'] is None):
            raise ValueError("Missing the required parameter `moid` when calling `equipment_locator_leds_moid_patch`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `equipment_locator_leds_moid_patch`")


        collection_formats = {}

        path_params = {}
        if 'moid' in params:
            path_params['moid'] = params['moid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/equipment/LocatorLeds/{moid}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def equipment_locator_leds_moid_post(self, moid, body, **kwargs):
        """
        Update an instance of 'equipmentLocatorLed'
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_moid_post(moid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str moid: The moid of the equipmentLocatorLed instance. (required)
        :param EquipmentLocatorLed body: equipmentLocatorLed to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.equipment_locator_leds_moid_post_with_http_info(moid, body, **kwargs)
        else:
            (data) = self.equipment_locator_leds_moid_post_with_http_info(moid, body, **kwargs)
            return data

    def equipment_locator_leds_moid_post_with_http_info(self, moid, body, **kwargs):
        """
        Update an instance of 'equipmentLocatorLed'
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.equipment_locator_leds_moid_post_with_http_info(moid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str moid: The moid of the equipmentLocatorLed instance. (required)
        :param EquipmentLocatorLed body: equipmentLocatorLed to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['moid', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method equipment_locator_leds_moid_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'moid' is set
        if ('moid' not in params) or (params['moid'] is None):
            raise ValueError("Missing the required parameter `moid` when calling `equipment_locator_leds_moid_post`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `equipment_locator_leds_moid_post`")


        collection_formats = {}

        path_params = {}
        if 'moid' in params:
            path_params['moid'] = params['moid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/equipment/LocatorLeds/{moid}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
