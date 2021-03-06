# coding: utf-8

"""
    Farsava API

    Farsava API. Speech Recognition and Text to Speech by applying powerful deep neural network models.  # noqa: E501

    OpenAPI spec version: 1.0.5
    Contact: amir@amerandish.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ASRResponseBody(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'transcription_id': 'str',
        'duration': 'float',
        'inference_time': 'float',
        'status': 'ASRStatus',
        'results': 'list[SpeechRecognitionResult]'
    }

    attribute_map = {
        'transcription_id': 'transcriptionId',
        'duration': 'duration',
        'inference_time': 'inferenceTime',
        'status': 'status',
        'results': 'results'
    }

    def __init__(self, transcription_id=None, duration=None, inference_time=None, status=None, results=None):  # noqa: E501
        """ASRResponseBody - a model defined in OpenAPI"""  # noqa: E501

        self._transcription_id = None
        self._duration = None
        self._inference_time = None
        self._status = None
        self._results = None
        self.discriminator = None

        if transcription_id is not None:
            self.transcription_id = transcription_id
        if duration is not None:
            self.duration = duration
        if inference_time is not None:
            self.inference_time = inference_time
        if status is not None:
            self.status = status
        if results is not None:
            self.results = results

    @property
    def transcription_id(self):
        """Gets the transcription_id of this ASRResponseBody.  # noqa: E501

        A UUID string specifying a unique pair of audio and recognitionResult. It can be used to retrieve this recognitionResult using transcription endpoint. asrLongRunning recognitionResult will only be available using transcription endpoint and this transcriptionId.   # noqa: E501

        :return: The transcription_id of this ASRResponseBody.  # noqa: E501
        :rtype: str
        """
        return self._transcription_id

    @transcription_id.setter
    def transcription_id(self, transcription_id):
        """Sets the transcription_id of this ASRResponseBody.

        A UUID string specifying a unique pair of audio and recognitionResult. It can be used to retrieve this recognitionResult using transcription endpoint. asrLongRunning recognitionResult will only be available using transcription endpoint and this transcriptionId.   # noqa: E501

        :param transcription_id: The transcription_id of this ASRResponseBody.  # noqa: E501
        :type: str
        """

        self._transcription_id = transcription_id

    @property
    def duration(self):
        """Gets the duration of this ASRResponseBody.  # noqa: E501

        File duration in seconds.  # noqa: E501

        :return: The duration of this ASRResponseBody.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ASRResponseBody.

        File duration in seconds.  # noqa: E501

        :param duration: The duration of this ASRResponseBody.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def inference_time(self):
        """Gets the inference_time of this ASRResponseBody.  # noqa: E501

        Total inference time in seconds.  # noqa: E501

        :return: The inference_time of this ASRResponseBody.  # noqa: E501
        :rtype: float
        """
        return self._inference_time

    @inference_time.setter
    def inference_time(self, inference_time):
        """Sets the inference_time of this ASRResponseBody.

        Total inference time in seconds.  # noqa: E501

        :param inference_time: The inference_time of this ASRResponseBody.  # noqa: E501
        :type: float
        """

        self._inference_time = inference_time

    @property
    def status(self):
        """Gets the status of this ASRResponseBody.  # noqa: E501


        :return: The status of this ASRResponseBody.  # noqa: E501
        :rtype: ASRStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ASRResponseBody.


        :param status: The status of this ASRResponseBody.  # noqa: E501
        :type: ASRStatus
        """

        self._status = status

    @property
    def results(self):
        """Gets the results of this ASRResponseBody.  # noqa: E501

        Sequential list of transcription results corresponding to sequential portions of audio. May contain one or more recognition hypotheses (up to the maximum specified in maxAlternatives). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.   # noqa: E501

        :return: The results of this ASRResponseBody.  # noqa: E501
        :rtype: list[SpeechRecognitionResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ASRResponseBody.

        Sequential list of transcription results corresponding to sequential portions of audio. May contain one or more recognition hypotheses (up to the maximum specified in maxAlternatives). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.   # noqa: E501

        :param results: The results of this ASRResponseBody.  # noqa: E501
        :type: list[SpeechRecognitionResult]
        """

        self._results = results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ASRResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
