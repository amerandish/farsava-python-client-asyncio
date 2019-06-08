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


class LanguageModelApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_language_model_by_id(self, language_model_id, **kwargs):  # noqa: E501
        """GET /speech/languagemodels/{languageModelId}  # noqa: E501

        Retrieving the status of a language model with specified languageModelId. A language model is ready to use when its status is *trained*. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_model_by_id(language_model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str language_model_id: Id of the language model. (required)
        :return: LanguageModelResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_language_model_by_id_with_http_info(language_model_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_language_model_by_id_with_http_info(language_model_id, **kwargs)  # noqa: E501
            return data

    def get_language_model_by_id_with_http_info(self, language_model_id, **kwargs):  # noqa: E501
        """GET /speech/languagemodels/{languageModelId}  # noqa: E501

        Retrieving the status of a language model with specified languageModelId. A language model is ready to use when its status is *trained*. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_model_by_id_with_http_info(language_model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str language_model_id: Id of the language model. (required)
        :return: LanguageModelResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['language_model_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_language_model_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'language_model_id' is set
        if ('language_model_id' not in local_var_params or
                local_var_params['language_model_id'] is None):
            raise ApiValueError("Missing the required parameter `language_model_id` when calling `get_language_model_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'language_model_id' in local_var_params:
            path_params['languageModelId'] = local_var_params['language_model_id']  # noqa: E501

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
            '/speech/languagemodels/{languageModelId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LanguageModelResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_language_model_list(self, **kwargs):  # noqa: E501
        """GET /speech/languagemodels  # noqa: E501

        Returns list of user available language models. Each user can access *general* language models plus their own *custom* trained language models. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_model_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[LanguageModelResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_language_model_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_language_model_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_language_model_list_with_http_info(self, **kwargs):  # noqa: E501
        """GET /speech/languagemodels  # noqa: E501

        Returns list of user available language models. Each user can access *general* language models plus their own *custom* trained language models. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_language_model_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[LanguageModelResult]
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
                    " to method get_language_model_list" % key
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
            '/speech/languagemodels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LanguageModelResult]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def train_language_model(self, language_model_train_request_body, **kwargs):  # noqa: E501
        """POST /speech/languagemodels  # noqa: E501

        Train a custom language model using pharases provided by user. Returning a languageModelId for accessing the language model later and using this custom language model to transcribe audios. Using custom language models will boost accuracy for specific keywords/phrases and can be used for a domain-specific speech recognition. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.train_language_model(language_model_train_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LanguageModelTrainRequestBody language_model_train_request_body: A json object including a name and a corpora. Corpora is a array of text data to train a custom model. This text data can be keywords/phrases. All values in the array must be a string. Name is an arbitary string you set for the custom language model name. (required)
        :return: LanguageModelResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.train_language_model_with_http_info(language_model_train_request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.train_language_model_with_http_info(language_model_train_request_body, **kwargs)  # noqa: E501
            return data

    def train_language_model_with_http_info(self, language_model_train_request_body, **kwargs):  # noqa: E501
        """POST /speech/languagemodels  # noqa: E501

        Train a custom language model using pharases provided by user. Returning a languageModelId for accessing the language model later and using this custom language model to transcribe audios. Using custom language models will boost accuracy for specific keywords/phrases and can be used for a domain-specific speech recognition. ***   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.train_language_model_with_http_info(language_model_train_request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LanguageModelTrainRequestBody language_model_train_request_body: A json object including a name and a corpora. Corpora is a array of text data to train a custom model. This text data can be keywords/phrases. All values in the array must be a string. Name is an arbitary string you set for the custom language model name. (required)
        :return: LanguageModelResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['language_model_train_request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method train_language_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'language_model_train_request_body' is set
        if ('language_model_train_request_body' not in local_var_params or
                local_var_params['language_model_train_request_body'] is None):
            raise ApiValueError("Missing the required parameter `language_model_train_request_body` when calling `train_language_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'language_model_train_request_body' in local_var_params:
            body_params = local_var_params['language_model_train_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/speech/languagemodels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LanguageModelResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)