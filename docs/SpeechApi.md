# aiofarsava.SpeechApi

All URIs are relative to *https://api.farsava.ir/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transcription**](SpeechApi.md#delete_transcription) | **DELETE** /speech/transcriptions/{transcriptionId} | DELETE /speech/transcriptions/{transcriptionId}
[**get_transcription**](SpeechApi.md#get_transcription) | **GET** /speech/transcriptions/{transcriptionId} | GET /speech/transcriptions/{transcriptionId}
[**recognize**](SpeechApi.md#recognize) | **POST** /speech/asr | POST /speech/asr
[**recognize_live**](SpeechApi.md#recognize_live) | **GET** /speech/asrlive | GET /speech/asrlive
[**recognize_long_running**](SpeechApi.md#recognize_long_running) | **POST** /speech/asrlongrunning | POST /speech/asrlongrunning
[**speech_health_check**](SpeechApi.md#speech_health_check) | **GET** /speech/healthcheck | GET /speech/healthcheck


# **delete_transcription**
> delete_transcription(transcription_id)

DELETE /speech/transcriptions/{transcriptionId}

Deletes a transcription for a previous file using transcriptionId. *** 

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
api_instance = aiofarsava.SpeechApi(aiofarsava.ApiClient(configuration))
transcription_id = 'transcription_id_example' # str | Id of the transcribed audio. It is a UUID string provided in the speech recognition result. 

try:
    # DELETE /speech/transcriptions/{transcriptionId}
    api_instance.delete_transcription(transcription_id)
except ApiException as e:
    print("Exception when calling SpeechApi->delete_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription_id** | [**str**](.md)| Id of the transcribed audio. It is a UUID string provided in the speech recognition result.  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcription**
> ASRResponseBody get_transcription(transcription_id)

GET /speech/transcriptions/{transcriptionId}

Transcription endpoint enable us to retrieve a previous speech recognition result or inform us on a long running speech recognition status. To access a speech recognition result transcriptionId should be provided.    ***    

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
api_instance = aiofarsava.SpeechApi(aiofarsava.ApiClient(configuration))
transcription_id = 'transcription_id_example' # str | Id of the transcribed audio. It is a UUID string provided in the speech recognition result. 

try:
    # GET /speech/transcriptions/{transcriptionId}
    api_response = api_instance.get_transcription(transcription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechApi->get_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription_id** | [**str**](.md)| Id of the transcribed audio. It is a UUID string provided in the speech recognition result.  | 

### Return type

[**ASRResponseBody**](ASRResponseBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize**
> ASRResponseBody recognize(asr_request_body_data)

POST /speech/asr

## Performs synchronous speech recognition  *** This resource receives audio data in different formats and transcribes the audio using state-of-the-art deep neural networks. It performs synchronous speech recognition and the result will be availble after all audio has been sent and processed. This endpoint is designed for transcription of short audio files upto 1 minute. *** Using *config* object you can can specify audio configs such as *audioEncoding* and *sampleRateHertz*. We will support different languages so you can choose the *languageCode*. Using *asrModel* and *languageModel* in config you can use customized models. Refer to *asrLongRunning* and *WebSocket API* for longer audio transcriptions. 

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
api_instance = aiofarsava.SpeechApi(aiofarsava.ApiClient(configuration))
asr_request_body_data = {"config":{"audioEncoding":"LINEAR16","sampleRateHertz":16000,"languageCode":"fa","maxAlternatives":1,"profanityFilter":true,"asrModel":"default","languageModel":"8ac4b75e-d3f8-48f2-80f2-d910fbeb02f4"},"audio":{"data":"UklGRiSFAgBXQVZFZm10IBAAAAABAAEAgD4AAAB9..."}} # ASRRequestBodyData | ## Audio *data* along with the customized *config* is posted to this service for speech recognition. 

try:
    # POST /speech/asr
    api_response = api_instance.recognize(asr_request_body_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechApi->recognize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asr_request_body_data** | [**ASRRequestBodyData**](ASRRequestBodyData.md)| ## Audio *data* along with the customized *config* is posted to this service for speech recognition.  | 

### Return type

[**ASRResponseBody**](ASRResponseBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_live**
> ASRResponseBody recognize_live()

GET /speech/asrlive

## Performs asynchronous live speech recognition using websocket *** This resource establish a websocket with client and receives audio data using websocket. It will start transcribing the audio using state-of-the-art deep neural networks and returns the partial results on the websocket. This endpoint is designed for transcription of stream audio data upto 15 minute. It will send back partial (status=partial) result everytime it transcribes an endpoint. After client sends the close signal, it will receive a ASRResponseBody with status=done. *** Using *config* object you can can specify audio configs such as *audioEncoding* and *sampleRateHertz*. We will support different languages so you can choose the *languageCode*. Using *asrModel* and *languageModel* in config you can use customized models. Refer to *ASRLongRuning API* for long audio speech recognition. Refer to *ASR API* for fast recognition for short audio files. 

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
api_instance = aiofarsava.SpeechApi(aiofarsava.ApiClient(configuration))

try:
    # GET /speech/asrlive
    api_response = api_instance.recognize_live()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechApi->recognize_live: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ASRResponseBody**](ASRResponseBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_long_running**
> ASRResponseBody recognize_long_running(asr_request_body_uri)

POST /speech/asrlongrunning

## Performs asynchronous speech recognition  *** This resource receives a uri containing the audio resource, download it and transcribes the audio using state-of-the-art deep neural networks. It performs asynchronous speech recognition and the result will be availble using transcription endpoint. This endpoint is designed for transcription of long audio files upto 240 minute. *** Using *config* object you can can specify audio configs such as *audioEncoding* and *sampleRateHertz*. We will support different languages so you can choose the *languageCode*. Using *asrModel* and *languageModel* in config you can use customized models. Refer to *WebSocket API* for speech recognition with streams. Refer to *ASR API* for fast recognition for short audio files. 

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
api_instance = aiofarsava.SpeechApi(aiofarsava.ApiClient(configuration))
asr_request_body_uri = {"config":{"audioEncoding":"LINEAR16","sampleRateHertz":16000,"languageCode":"fa","maxAlternatives":1,"profanityFilter":true,"asrModel":"default","languageModel":"8ac4b75e-d3f8-48f2-80f2-d910fbeb02f4"},"audio":{"uri":"http://files.examplecdn.com/data/example.wav"}} # ASRRequestBodyURI | post uri and configs to this service for asr. 

try:
    # POST /speech/asrlongrunning
    api_response = api_instance.recognize_long_running(asr_request_body_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechApi->recognize_long_running: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asr_request_body_uri** | [**ASRRequestBodyURI**](ASRRequestBodyURI.md)| post uri and configs to this service for asr.  | 

### Return type

[**ASRResponseBody**](ASRResponseBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **speech_health_check**
> HealthCheckResponseBody speech_health_check()

GET /speech/healthcheck

## speech health check endpoint. *** This endpoint will return a simple json including **service status** and **API version**. 

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
api_instance = aiofarsava.SpeechApi(aiofarsava.ApiClient(configuration))

try:
    # GET /speech/healthcheck
    api_response = api_instance.speech_health_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechApi->speech_health_check: %s\n" % e)
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

