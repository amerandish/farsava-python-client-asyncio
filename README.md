# aiofarsava
Farsava API. Speech Recognition and Text to Speech by applying powerful deep neural network models.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.5
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import aiofarsava 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import aiofarsava
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.farsava.ir/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LanguageModelApi* | [**get_language_model_by_id**](docs/LanguageModelApi.md#get_language_model_by_id) | **GET** /speech/languagemodels/{languageModelId} | GET /speech/languagemodels/{languageModelId}
*LanguageModelApi* | [**get_language_model_list**](docs/LanguageModelApi.md#get_language_model_list) | **GET** /speech/languagemodels | GET /speech/languagemodels
*LanguageModelApi* | [**train_language_model**](docs/LanguageModelApi.md#train_language_model) | **POST** /speech/languagemodels | POST /speech/languagemodels
*SpeechApi* | [**delete_transcription**](docs/SpeechApi.md#delete_transcription) | **DELETE** /speech/transcriptions/{transcriptionId} | DELETE /speech/transcriptions/{transcriptionId}
*SpeechApi* | [**get_transcription**](docs/SpeechApi.md#get_transcription) | **GET** /speech/transcriptions/{transcriptionId} | GET /speech/transcriptions/{transcriptionId}
*SpeechApi* | [**recognize**](docs/SpeechApi.md#recognize) | **POST** /speech/asr | POST /speech/asr
*SpeechApi* | [**recognize_live**](docs/SpeechApi.md#recognize_live) | **GET** /speech/asrlive | GET /speech/asrlive
*SpeechApi* | [**recognize_long_running**](docs/SpeechApi.md#recognize_long_running) | **POST** /speech/asrlongrunning | POST /speech/asrlongrunning
*SpeechApi* | [**speech_health_check**](docs/SpeechApi.md#speech_health_check) | **GET** /speech/healthcheck | GET /speech/healthcheck
*VoiceApi* | [**get_voices_list**](docs/VoiceApi.md#get_voices_list) | **GET** /voice/speakers | GET /voice/speakers
*VoiceApi* | [**synthesize**](docs/VoiceApi.md#synthesize) | **POST** /voice/tts | POST /voice/tts
*VoiceApi* | [**voice_health_check**](docs/VoiceApi.md#voice_health_check) | **GET** /voice/healthcheck | GET /voice/healthcheck


## Documentation For Models

 - [ASRRequestBodyData](docs/ASRRequestBodyData.md)
 - [ASRRequestBodyURI](docs/ASRRequestBodyURI.md)
 - [ASRResponseBody](docs/ASRResponseBody.md)
 - [ASRStatus](docs/ASRStatus.md)
 - [AudioEncoding](docs/AudioEncoding.md)
 - [Error](docs/Error.md)
 - [HealthCheckResponseBody](docs/HealthCheckResponseBody.md)
 - [LMStatus](docs/LMStatus.md)
 - [LanguageCode](docs/LanguageCode.md)
 - [LanguageModelResult](docs/LanguageModelResult.md)
 - [LanguageModelTrainRequestBody](docs/LanguageModelTrainRequestBody.md)
 - [RecognitionAudioData](docs/RecognitionAudioData.md)
 - [RecognitionAudioURI](docs/RecognitionAudioURI.md)
 - [RecognitionConfig](docs/RecognitionConfig.md)
 - [SpeechRecognitionModel](docs/SpeechRecognitionModel.md)
 - [SpeechRecognitionResult](docs/SpeechRecognitionResult.md)
 - [SynthesisInput](docs/SynthesisInput.md)
 - [TTSAudioConfig](docs/TTSAudioConfig.md)
 - [TTSRequestBody](docs/TTSRequestBody.md)
 - [TTSResponseBody](docs/TTSResponseBody.md)
 - [TTSVoiceGender](docs/TTSVoiceGender.md)
 - [VoiceSelectionParams](docs/VoiceSelectionParams.md)
 - [WordInfo](docs/WordInfo.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

amir@amerandish.com


