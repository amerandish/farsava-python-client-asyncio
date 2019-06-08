# LanguageModelResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_model_id** | **str** | This is the language model id of a customized trained language model. You can train your own language models and then use them to recognize speech. Refer to [languagemodel/train](#languagemodel/train) for more info.    There are some pretrained language models which you can use.    Model | Description   ------------ | -------------   general | Best for audio content that is not one of the specific language models. This is the default language model and if you are not sure which one to use, simply use &#39;general&#39;.   numbers | Best for audio content that contains only spoken numbers. For examble this language model can be used for speech enabled number input fileds.   yesno | Best for audio content that contains yes or no. For examble this language model can be used to receive confirmation from user.   country | Best for audio content that contains only spoken country. For examble this language model can be used for speech enabled input fileds.   city | Best for audio content that contains only spoken city. For examble this language model      can be used for speech enabled input fileds.   career | Best for audio content that contains only spoken career names. For examble this language model can be used for speech enabled input fileds.  | [optional] 
**name** | **str** | The name of the custom language model. | [optional] 
**status** | [**LMStatus**](LMStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


