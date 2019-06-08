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


class TTSAudioConfig(object):
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
        'audio_encoding': 'AudioEncoding',
        'sample_rate_hertz': 'int',
        'speaking_rate': 'float',
        'pitch': 'float',
        'volume_gain_db': 'float'
    }

    attribute_map = {
        'audio_encoding': 'audioEncoding',
        'sample_rate_hertz': 'sampleRateHertz',
        'speaking_rate': 'speakingRate',
        'pitch': 'pitch',
        'volume_gain_db': 'volumeGainDb'
    }

    def __init__(self, audio_encoding=None, sample_rate_hertz=16000, speaking_rate=None, pitch=None, volume_gain_db=None):  # noqa: E501
        """TTSAudioConfig - a model defined in OpenAPI"""  # noqa: E501

        self._audio_encoding = None
        self._sample_rate_hertz = None
        self._speaking_rate = None
        self._pitch = None
        self._volume_gain_db = None
        self.discriminator = None

        self.audio_encoding = audio_encoding
        self.sample_rate_hertz = sample_rate_hertz
        if speaking_rate is not None:
            self.speaking_rate = speaking_rate
        if pitch is not None:
            self.pitch = pitch
        if volume_gain_db is not None:
            self.volume_gain_db = volume_gain_db

    @property
    def audio_encoding(self):
        """Gets the audio_encoding of this TTSAudioConfig.  # noqa: E501


        :return: The audio_encoding of this TTSAudioConfig.  # noqa: E501
        :rtype: AudioEncoding
        """
        return self._audio_encoding

    @audio_encoding.setter
    def audio_encoding(self, audio_encoding):
        """Sets the audio_encoding of this TTSAudioConfig.


        :param audio_encoding: The audio_encoding of this TTSAudioConfig.  # noqa: E501
        :type: AudioEncoding
        """
        if audio_encoding is None:
            raise ValueError("Invalid value for `audio_encoding`, must not be `None`")  # noqa: E501

        self._audio_encoding = audio_encoding

    @property
    def sample_rate_hertz(self):
        """Gets the sample_rate_hertz of this TTSAudioConfig.  # noqa: E501

        Sample rate in Hertz of the audio data sent in all RecognitionAudio messages. Valid values are 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that is not possible, use the native sample rate of the audio source (instead of re-sampling). This field is required for all audio formats. In Text to Speech endpoint is the synthesis sample rate (in hertz) for audio and Optional. If this is different from the voice's natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality), unless the specified sample rate is not supported for the encoding chosen.   # noqa: E501

        :return: The sample_rate_hertz of this TTSAudioConfig.  # noqa: E501
        :rtype: int
        """
        return self._sample_rate_hertz

    @sample_rate_hertz.setter
    def sample_rate_hertz(self, sample_rate_hertz):
        """Sets the sample_rate_hertz of this TTSAudioConfig.

        Sample rate in Hertz of the audio data sent in all RecognitionAudio messages. Valid values are 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that is not possible, use the native sample rate of the audio source (instead of re-sampling). This field is required for all audio formats. In Text to Speech endpoint is the synthesis sample rate (in hertz) for audio and Optional. If this is different from the voice's natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality), unless the specified sample rate is not supported for the encoding chosen.   # noqa: E501

        :param sample_rate_hertz: The sample_rate_hertz of this TTSAudioConfig.  # noqa: E501
        :type: int
        """
        if sample_rate_hertz is None:
            raise ValueError("Invalid value for `sample_rate_hertz`, must not be `None`")  # noqa: E501

        self._sample_rate_hertz = sample_rate_hertz

    @property
    def speaking_rate(self):
        """Gets the speaking_rate of this TTSAudioConfig.  # noqa: E501

        Optional speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values < 0.25 or > 4.0 will return an error.   # noqa: E501

        :return: The speaking_rate of this TTSAudioConfig.  # noqa: E501
        :rtype: float
        """
        return self._speaking_rate

    @speaking_rate.setter
    def speaking_rate(self, speaking_rate):
        """Sets the speaking_rate of this TTSAudioConfig.

        Optional speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values < 0.25 or > 4.0 will return an error.   # noqa: E501

        :param speaking_rate: The speaking_rate of this TTSAudioConfig.  # noqa: E501
        :type: float
        """
        if speaking_rate is not None and speaking_rate > 4:  # noqa: E501
            raise ValueError("Invalid value for `speaking_rate`, must be a value less than or equal to `4`")  # noqa: E501
        if speaking_rate is not None and speaking_rate < 0.25:  # noqa: E501
            raise ValueError("Invalid value for `speaking_rate`, must be a value greater than or equal to `0.25`")  # noqa: E501

        self._speaking_rate = speaking_rate

    @property
    def pitch(self):
        """Gets the pitch of this TTSAudioConfig.  # noqa: E501

        Optional speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch.   # noqa: E501

        :return: The pitch of this TTSAudioConfig.  # noqa: E501
        :rtype: float
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this TTSAudioConfig.

        Optional speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch.   # noqa: E501

        :param pitch: The pitch of this TTSAudioConfig.  # noqa: E501
        :type: float
        """
        if pitch is not None and pitch > 20.0:  # noqa: E501
            raise ValueError("Invalid value for `pitch`, must be a value less than or equal to `20.0`")  # noqa: E501
        if pitch is not None and pitch < -20.0:  # noqa: E501
            raise ValueError("Invalid value for `pitch`, must be a value greater than or equal to `-20.0`")  # noqa: E501

        self._pitch = pitch

    @property
    def volume_gain_db(self):
        """Gets the volume_gain_db of this TTSAudioConfig.  # noqa: E501

        Optional volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. Strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.   # noqa: E501

        :return: The volume_gain_db of this TTSAudioConfig.  # noqa: E501
        :rtype: float
        """
        return self._volume_gain_db

    @volume_gain_db.setter
    def volume_gain_db(self, volume_gain_db):
        """Sets the volume_gain_db of this TTSAudioConfig.

        Optional volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. Strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.   # noqa: E501

        :param volume_gain_db: The volume_gain_db of this TTSAudioConfig.  # noqa: E501
        :type: float
        """
        if volume_gain_db is not None and volume_gain_db > 16.0:  # noqa: E501
            raise ValueError("Invalid value for `volume_gain_db`, must be a value less than or equal to `16.0`")  # noqa: E501
        if volume_gain_db is not None and volume_gain_db < -96.0:  # noqa: E501
            raise ValueError("Invalid value for `volume_gain_db`, must be a value greater than or equal to `-96.0`")  # noqa: E501

        self._volume_gain_db = volume_gain_db

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
        if not isinstance(other, TTSAudioConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other