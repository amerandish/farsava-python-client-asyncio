# coding: utf-8

# flake8: noqa

"""
    Farsava API

    Farsava API. Speech Recognition and Text to Speech by applying powerful deep neural network models.  # noqa: E501

    OpenAPI spec version: 1.0.5
    Contact: amir@amerandish.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from farsava_api.language_model_api import LanguageModelApi
from farsava_api.speech_api import SpeechApi
from farsava_api.voice_api import VoiceApi

# import ApiClient
from aiofarsava.api_client import ApiClient
from aiofarsava.configuration import Configuration
from aiofarsava.exceptions import OpenApiException
from aiofarsava.exceptions import ApiTypeError
from aiofarsava.exceptions import ApiValueError
from aiofarsava.exceptions import ApiKeyError
from aiofarsava.exceptions import ApiException
# import models into sdk package
from aiofarsava.farsava_model.asr_request_body_data import ASRRequestBodyData
from aiofarsava.farsava_model.asr_request_body_uri import ASRRequestBodyURI
from aiofarsava.farsava_model.asr_response_body import ASRResponseBody
from aiofarsava.farsava_model.asr_status import ASRStatus
from aiofarsava.farsava_model.audio_encoding import AudioEncoding
from aiofarsava.farsava_model.error import Error
from aiofarsava.farsava_model.health_check_response_body import HealthCheckResponseBody
from aiofarsava.farsava_model.lm_status import LMStatus
from aiofarsava.farsava_model.language_code import LanguageCode
from aiofarsava.farsava_model.language_model_result import LanguageModelResult
from aiofarsava.farsava_model.language_model_train_request_body import LanguageModelTrainRequestBody
from aiofarsava.farsava_model.recognition_audio_data import RecognitionAudioData
from aiofarsava.farsava_model.recognition_audio_uri import RecognitionAudioURI
from aiofarsava.farsava_model.recognition_config import RecognitionConfig
from aiofarsava.farsava_model.speech_recognition_model import SpeechRecognitionModel
from aiofarsava.farsava_model.speech_recognition_result import SpeechRecognitionResult
from aiofarsava.farsava_model.synthesis_input import SynthesisInput
from aiofarsava.farsava_model.tts_audio_config import TTSAudioConfig
from aiofarsava.farsava_model.tts_request_body import TTSRequestBody
from aiofarsava.farsava_model.tts_response_body import TTSResponseBody
from aiofarsava.farsava_model.tts_voice_gender import TTSVoiceGender
from aiofarsava.farsava_model.voice_selection_params import VoiceSelectionParams
from aiofarsava.farsava_model.word_info import WordInfo

