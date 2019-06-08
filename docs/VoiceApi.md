# aiofarsava.VoiceApi

All URIs are relative to *https://api.farsava.ir/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_voices_list**](VoiceApi.md#get_voices_list) | **GET** /voice/speakers | GET /voice/speakers
[**synthesize**](VoiceApi.md#synthesize) | **POST** /voice/tts | POST /voice/tts
[**voice_health_check**](VoiceApi.md#voice_health_check) | **GET** /voice/healthcheck | GET /voice/healthcheck


# **get_voices_list**
> list[VoiceSelectionParams] get_voices_list()

GET /voice/speakers

This endpoint retrieves the list of available speakers for speech synthesization. Each speaker has a unique *voiceId* which can be used to synthesize speech. The result aslo includes each speaker langauge, gender and name. *** 

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
api_instance = aiofarsava.VoiceApi(aiofarsava.ApiClient(configuration))

try:
    # GET /voice/speakers
    api_response = api_instance.get_voices_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voices_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VoiceSelectionParams]**](VoiceSelectionParams.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synthesize**
> TTSResponseBody synthesize(tts_request_body)

POST /voice/tts

## Synthesizes speech synchronously  *** Receives text and data configs and synthesize speech in different voices and format using state-of-the-art deep neural networks. This service synthesizes speech synchronously and the results will be available after all text input has been processed.  *** Using *config* object you can can specify audio configs such as *audioEncoding* and *sampleRateHertz*. We will support different languages so you can choose the *languageCode*. using *voiceSelectionParams* you can choose between the supported voices with specifying voiceId. Voices differ in gender, tone and style.  

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
api_instance = aiofarsava.VoiceApi(aiofarsava.ApiClient(configuration))
tts_request_body = {"synthesisInput":{"text":"Speak This."},"voiceConfig":{"languageCode":"fa","voiceId":"b2d8dfca-7d78-47f8-b976-c85b15bbc134","name":"speaker-2","gender":"female"},"audioConfig":{"audioEncoding":"MP3","speakingRate":1.2,"pitch":0.0,"volumeGainDb":-2,"sampleRateHertz":16000}} # TTSRequestBody | Receives a json including input text, voice parameteres and audio config. 

try:
    # POST /voice/tts
    api_response = api_instance.synthesize(tts_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->synthesize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tts_request_body** | [**TTSRequestBody**](TTSRequestBody.md)| Receives a json including input text, voice parameteres and audio config.  | 

### Return type

[**TTSResponseBody**](TTSResponseBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_health_check**
> HealthCheckResponseBody voice_health_check()

GET /voice/healthcheck

## voice health check endpoint. *** This endpoint will return a simple json including **service status** and **API version**. 

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
api_instance = aiofarsava.VoiceApi(aiofarsava.ApiClient(configuration))

try:
    # GET /voice/healthcheck
    api_response = api_instance.voice_health_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->voice_health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheckResponseBody**](HealthCheckResponseBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

