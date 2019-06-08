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


class LanguageModelResult(object):
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
        'language_model_id': 'str',
        'name': 'str',
        'status': 'LMStatus'
    }

    attribute_map = {
        'language_model_id': 'languageModelId',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, language_model_id=None, name=None, status=None):  # noqa: E501
        """LanguageModelResult - a model defined in OpenAPI"""  # noqa: E501

        self._language_model_id = None
        self._name = None
        self._status = None
        self.discriminator = None

        if language_model_id is not None:
            self.language_model_id = language_model_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def language_model_id(self):
        """Gets the language_model_id of this LanguageModelResult.  # noqa: E501

        This is the language model id of a customized trained language model. You can train your own language models and then use them to recognize speech. Refer to [languagemodel/train](#languagemodel/train) for more info.    There are some pretrained language models which you can use.    Model | Description   ------------ | -------------   general | Best for audio content that is not one of the specific language models. This is the default language model and if you are not sure which one to use, simply use 'general'.   numbers | Best for audio content that contains only spoken numbers. For examble this language model can be used for speech enabled number input fileds.   yesno | Best for audio content that contains yes or no. For examble this language model can be used to receive confirmation from user.   country | Best for audio content that contains only spoken country. For examble this language model can be used for speech enabled input fileds.   city | Best for audio content that contains only spoken city. For examble this language model      can be used for speech enabled input fileds.   career | Best for audio content that contains only spoken career names. For examble this language model can be used for speech enabled input fileds.   # noqa: E501

        :return: The language_model_id of this LanguageModelResult.  # noqa: E501
        :rtype: str
        """
        return self._language_model_id

    @language_model_id.setter
    def language_model_id(self, language_model_id):
        """Sets the language_model_id of this LanguageModelResult.

        This is the language model id of a customized trained language model. You can train your own language models and then use them to recognize speech. Refer to [languagemodel/train](#languagemodel/train) for more info.    There are some pretrained language models which you can use.    Model | Description   ------------ | -------------   general | Best for audio content that is not one of the specific language models. This is the default language model and if you are not sure which one to use, simply use 'general'.   numbers | Best for audio content that contains only spoken numbers. For examble this language model can be used for speech enabled number input fileds.   yesno | Best for audio content that contains yes or no. For examble this language model can be used to receive confirmation from user.   country | Best for audio content that contains only spoken country. For examble this language model can be used for speech enabled input fileds.   city | Best for audio content that contains only spoken city. For examble this language model      can be used for speech enabled input fileds.   career | Best for audio content that contains only spoken career names. For examble this language model can be used for speech enabled input fileds.   # noqa: E501

        :param language_model_id: The language_model_id of this LanguageModelResult.  # noqa: E501
        :type: str
        """

        self._language_model_id = language_model_id

    @property
    def name(self):
        """Gets the name of this LanguageModelResult.  # noqa: E501

        The name of the custom language model.  # noqa: E501

        :return: The name of this LanguageModelResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LanguageModelResult.

        The name of the custom language model.  # noqa: E501

        :param name: The name of this LanguageModelResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this LanguageModelResult.  # noqa: E501


        :return: The status of this LanguageModelResult.  # noqa: E501
        :rtype: LMStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LanguageModelResult.


        :param status: The status of this LanguageModelResult.  # noqa: E501
        :type: LMStatus
        """

        self._status = status

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
        if not isinstance(other, LanguageModelResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
