# aiofarsava.LanguageModelApi

All URIs are relative to *https://api.farsava.ir/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_language_model_by_id**](LanguageModelApi.md#get_language_model_by_id) | **GET** /speech/languagemodels/{languageModelId} | GET /speech/languagemodels/{languageModelId}
[**get_language_model_list**](LanguageModelApi.md#get_language_model_list) | **GET** /speech/languagemodels | GET /speech/languagemodels
[**train_language_model**](LanguageModelApi.md#train_language_model) | **POST** /speech/languagemodels | POST /speech/languagemodels


# **get_language_model_by_id**
> LanguageModelResult get_language_model_by_id(language_model_id)

GET /speech/languagemodels/{languageModelId}

Retrieving the status of a language model with specified languageModelId. A language model is ready to use when its status is *trained*. *** 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import aiofarsava
from aiofarsava.rest import ApiException
from pprint import pprint
configuration = aiofarsava.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = aiofarsava.LanguageModelApi(aiofarsava.ApiClient(configuration))
language_model_id = 'language_model_id_example' # str | Id of the language model.

try:
    # GET /speech/languagemodels/{languageModelId}
    api_response = api_instance.get_language_model_by_id(language_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageModelApi->get_language_model_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_model_id** | **str**| Id of the language model. | 

### Return type

[**LanguageModelResult**](LanguageModelResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_language_model_list**
> list[LanguageModelResult] get_language_model_list()

GET /speech/languagemodels

Returns list of user available language models. Each user can access *general* language models plus their own *custom* trained language models. *** 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import aiofarsava
from aiofarsava.rest import ApiException
from pprint import pprint
configuration = aiofarsava.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = aiofarsava.LanguageModelApi(aiofarsava.ApiClient(configuration))

try:
    # GET /speech/languagemodels
    api_response = api_instance.get_language_model_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageModelApi->get_language_model_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LanguageModelResult]**](LanguageModelResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **train_language_model**
> LanguageModelResult train_language_model(language_model_train_request_body)

POST /speech/languagemodels

Train a custom language model using pharases provided by user. Returning a languageModelId for accessing the language model later and using this custom language model to transcribe audios. Using custom language models will boost accuracy for specific keywords/phrases and can be used for a domain-specific speech recognition. *** 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import aiofarsava
from aiofarsava.rest import ApiException
from pprint import pprint
configuration = aiofarsava.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = aiofarsava.LanguageModelApi(aiofarsava.ApiClient(configuration))
language_model_train_request_body = aiofarsava.LanguageModelTrainRequestBody() # LanguageModelTrainRequestBody | A json object including a name and a corpora. Corpora is a array of text data to train a custom model. This text data can be keywords/phrases. All values in the array must be a string. Name is an arbitary string you set for the custom language model name.

try:
    # POST /speech/languagemodels
    api_response = api_instance.train_language_model(language_model_train_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageModelApi->train_language_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_model_train_request_body** | [**LanguageModelTrainRequestBody**](LanguageModelTrainRequestBody.md)| A json object including a name and a corpora. Corpora is a array of text data to train a custom model. This text data can be keywords/phrases. All values in the array must be a string. Name is an arbitary string you set for the custom language model name. | 

### Return type

[**LanguageModelResult**](LanguageModelResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

