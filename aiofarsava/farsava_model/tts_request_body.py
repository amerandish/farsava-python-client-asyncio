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


class TTSRequestBody(object):
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
        'synthesis_input': 'SynthesisInput',
        'voice_config': 'VoiceSelectionParams',
        'audio_config': 'TTSAudioConfig'
    }

    attribute_map = {
        'synthesis_input': 'synthesisInput',
        'voice_config': 'voiceConfig',
        'audio_config': 'audioConfig'
    }

    def __init__(self, synthesis_input=None, voice_config=None, audio_config=None):  # noqa: E501
        """TTSRequestBody - a model defined in OpenAPI"""  # noqa: E501

        self._synthesis_input = None
        self._voice_config = None
        self._audio_config = None
        self.discriminator = None

        self.synthesis_input = synthesis_input
        self.voice_config = voice_config
        self.audio_config = audio_config

    @property
    def synthesis_input(self):
        """Gets the synthesis_input of this TTSRequestBody.  # noqa: E501


        :return: The synthesis_input of this TTSRequestBody.  # noqa: E501
        :rtype: SynthesisInput
        """
        return self._synthesis_input

    @synthesis_input.setter
    def synthesis_input(self, synthesis_input):
        """Sets the synthesis_input of this TTSRequestBody.


        :param synthesis_input: The synthesis_input of this TTSRequestBody.  # noqa: E501
        :type: SynthesisInput
        """
        if synthesis_input is None:
            raise ValueError("Invalid value for `synthesis_input`, must not be `None`")  # noqa: E501

        self._synthesis_input = synthesis_input

    @property
    def voice_config(self):
        """Gets the voice_config of this TTSRequestBody.  # noqa: E501


        :return: The voice_config of this TTSRequestBody.  # noqa: E501
        :rtype: VoiceSelectionParams
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this TTSRequestBody.


        :param voice_config: The voice_config of this TTSRequestBody.  # noqa: E501
        :type: VoiceSelectionParams
        """
        if voice_config is None:
            raise ValueError("Invalid value for `voice_config`, must not be `None`")  # noqa: E501

        self._voice_config = voice_config

    @property
    def audio_config(self):
        """Gets the audio_config of this TTSRequestBody.  # noqa: E501


        :return: The audio_config of this TTSRequestBody.  # noqa: E501
        :rtype: TTSAudioConfig
        """
        return self._audio_config

    @audio_config.setter
    def audio_config(self, audio_config):
        """Sets the audio_config of this TTSRequestBody.


        :param audio_config: The audio_config of this TTSRequestBody.  # noqa: E501
        :type: TTSAudioConfig
        """
        if audio_config is None:
            raise ValueError("Invalid value for `audio_config`, must not be `None`")  # noqa: E501

        self._audio_config = audio_config

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
        if not isinstance(other, TTSRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
