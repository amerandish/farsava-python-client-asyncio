# coding: utf-8

"""
    Farsava API

    Farsava API. Speech Recognition and Text to Speech by applying powerful deep neural network models.  # noqa: E501

    OpenAPI spec version: 1.0.5
    Contact: amir@amerandish.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aiofarsava.api_client import ApiClient
from aiofarsava.exceptions import (
    ApiTypeError,
    ApiValueError
)


class VoiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_voices_list(self, **kwargs):  # noqa: E501
        """GET /voice/speakers  # noqa: E501

        This endpoint retrieves the list of available speakers for speech synthesization. Each speaker has a unique *voiceId* which can be used to synthesize speech. The result aslo includes each speaker langauge, gender and name. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voices_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[VoiceSelectionParams]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_voices_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_voices_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_voices_list_with_http_info(self, **kwargs):  # noqa: E501
        """GET /voice/speakers  # noqa: E501

        This endpoint retrieves the list of available speakers for speech synthesization. Each speaker has a unique *voiceId* which can be used to synthesize speech. The result aslo includes each speaker langauge, gender and name. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_voices_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[VoiceSelectionParams]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_voices_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/voice/speakers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[VoiceSelectionParams]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def synthesize(self, tts_request_body, **kwargs):  # noqa: E501
        """POST /voice/tts  # noqa: E501

        ## Synthesizes speech synchronously  *** Receives text and data configs and synthesize speech in different voices and format using state-of-the-art deep neural networks. This service synthesizes speech synchronously and the results will be available after all text input has been processed.  *** Using *config* object you can can specify audio configs such as *audioEncoding* and *sampleRateHertz*. We will support different languages so you can choose the *languageCode*. using *voiceSelectionParams* you can choose between the supported voices with specifying voiceId. Voices differ in gender, tone and style.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.synthesize(tts_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TTSRequestBody tts_request_body: Receives a json including input text, voice parameteres and audio config.  (required)
        :return: TTSResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.synthesize_with_http_info(tts_request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.synthesize_with_http_info(tts_request_body, **kwargs)  # noqa: E501
            return data

    def synthesize_with_http_info(self, tts_request_body, **kwargs):  # noqa: E501
        """POST /voice/tts  # noqa: E501

        ## Synthesizes speech synchronously  *** Receives text and data configs and synthesize speech in different voices and format using state-of-the-art deep neural networks. This service synthesizes speech synchronously and the results will be available after all text input has been processed.  *** Using *config* object you can can specify audio configs such as *audioEncoding* and *sampleRateHertz*. We will support different languages so you can choose the *languageCode*. using *voiceSelectionParams* you can choose between the supported voices with specifying voiceId. Voices differ in gender, tone and style.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.synthesize_with_http_info(tts_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TTSRequestBody tts_request_body: Receives a json including input text, voice parameteres and audio config.  (required)
        :return: TTSResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tts_request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method synthesize" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tts_request_body' is set
        if ('tts_request_body' not in local_var_params or
                local_var_params['tts_request_body'] is None):
            raise ApiValueError("Missing the required parameter `tts_request_body` when calling `synthesize`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tts_request_body' in local_var_params:
            body_params = local_var_params['tts_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/voice/tts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TTSResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def voice_health_check(self, **kwargs):  # noqa: E501
        """GET /voice/healthcheck  # noqa: E501

        ## voice health check endpoint. *** This endpoint will return a simple json including **service status** and **API version**.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_health_check(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HealthCheckResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_health_check_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.voice_health_check_with_http_info(**kwargs)  # noqa: E501
            return data

    def voice_health_check_with_http_info(self, **kwargs):  # noqa: E501
        """GET /voice/healthcheck  # noqa: E501

        ## voice health check endpoint. *** This endpoint will return a simple json including **service status** and **API version**.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_health_check_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HealthCheckResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_health_check" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/voice/healthcheck', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HealthCheckResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)