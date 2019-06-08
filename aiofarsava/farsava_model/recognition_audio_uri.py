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


class RecognitionAudioURI(object):
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
        'uri': 'str'
    }

    attribute_map = {
        'uri': 'uri'
    }

    def __init__(self, uri=None):  # noqa: E501
        """RecognitionAudioURI - a model defined in OpenAPI"""  # noqa: E501

        self._uri = None
        self.discriminator = None

        self.uri = uri

    @property
    def uri(self):
        """Gets the uri of this RecognitionAudioURI.  # noqa: E501

        URI that points to a file that contains audio data bytes as specified in RecognitionConfig. The file must not be compressed (for example, gzip).   # noqa: E501

        :return: The uri of this RecognitionAudioURI.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RecognitionAudioURI.

        URI that points to a file that contains audio data bytes as specified in RecognitionConfig. The file must not be compressed (for example, gzip).   # noqa: E501

        :param uri: The uri of this RecognitionAudioURI.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

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
        if not isinstance(other, RecognitionAudioURI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
