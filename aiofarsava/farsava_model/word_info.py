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


class WordInfo(object):
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
        'start_time': 'float',
        'end_time': 'float',
        'word': 'str',
        'confidence': 'float'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'word': 'word',
        'confidence': 'confidence'
    }

    def __init__(self, start_time=None, end_time=None, word=None, confidence=None):  # noqa: E501
        """WordInfo - a model defined in OpenAPI"""  # noqa: E501

        self._start_time = None
        self._end_time = None
        self._word = None
        self._confidence = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if word is not None:
            self.word = word
        if confidence is not None:
            self.confidence = confidence

    @property
    def start_time(self):
        """Gets the start_time of this WordInfo.  # noqa: E501

        Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This is an experimental feature and the accuracy of the time offset can vary. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating confidence was not set.   # noqa: E501

        :return: The start_time of this WordInfo.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WordInfo.

        Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This is an experimental feature and the accuracy of the time offset can vary. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating confidence was not set.   # noqa: E501

        :param start_time: The start_time of this WordInfo.  # noqa: E501
        :type: float
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this WordInfo.  # noqa: E501

        Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This is an experimental feature and the accuracy of the time offset can vary. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating confidence was not set.   # noqa: E501

        :return: The end_time of this WordInfo.  # noqa: E501
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this WordInfo.

        Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This is an experimental feature and the accuracy of the time offset can vary. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating confidence was not set.   # noqa: E501

        :param end_time: The end_time of this WordInfo.  # noqa: E501
        :type: float
        """

        self._end_time = end_time

    @property
    def word(self):
        """Gets the word of this WordInfo.  # noqa: E501

        The word corresponding to this set of information.   # noqa: E501

        :return: The word of this WordInfo.  # noqa: E501
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this WordInfo.

        The word corresponding to this set of information.   # noqa: E501

        :param word: The word of this WordInfo.  # noqa: E501
        :type: str
        """

        self._word = word

    @property
    def confidence(self):
        """Gets the confidence of this WordInfo.  # noqa: E501

        The confidence of ASR engine for generated output. The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. It is the total confidence of recognition in transcript level and each word confidence in word info object. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating confidence was not set.   # noqa: E501

        :return: The confidence of this WordInfo.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this WordInfo.

        The confidence of ASR engine for generated output. The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. It is the total confidence of recognition in transcript level and each word confidence in word info object. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating confidence was not set.   # noqa: E501

        :param confidence: The confidence of this WordInfo.  # noqa: E501
        :type: float
        """
        if confidence is not None and confidence > 1:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `1`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

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
        if not isinstance(other, WordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
