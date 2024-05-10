# coding: utf-8

"""
    Vorboss Product Availability API

    This API is provided by Vorboss to allow customers to check which products are available at a given postcode.  # noqa: E501

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ProductAvailability.api_client import ApiClient


class ProductAvailabilityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def confirm_postcode(self, postcode, **kwargs):  # noqa: E501
        """Check a postcode  # noqa: E501

        Check which products are available at the given postcode.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm_postcode(postcode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str postcode: UK Postcode to check availability for. (required)
        :return: Postcode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.confirm_postcode_with_http_info(postcode, **kwargs)  # noqa: E501
        else:
            (data) = self.confirm_postcode_with_http_info(postcode, **kwargs)  # noqa: E501
            return data

    def confirm_postcode_with_http_info(self, postcode, **kwargs):  # noqa: E501
        """Check a postcode  # noqa: E501

        Check which products are available at the given postcode.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm_postcode_with_http_info(postcode, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str postcode: UK Postcode to check availability for. (required)
        :return: Postcode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['postcode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method confirm_postcode" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'postcode' is set
        if ('postcode' not in params or
                params['postcode'] is None):
            raise ValueError("Missing the required parameter `postcode` when calling `confirm_postcode`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'postcode' in params:
            path_params['postcode'] = params['postcode']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/product-availability/postcode/{postcode}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Postcode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)