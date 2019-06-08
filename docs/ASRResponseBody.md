# ASRResponseBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transcription_id** | **str** | A UUID string specifying a unique pair of audio and recognitionResult. It can be used to retrieve this recognitionResult using transcription endpoint. asrLongRunning recognitionResult will only be available using transcription endpoint and this transcriptionId.  | [optional] 
**duration** | **float** | File duration in seconds. | [optional] 
**inference_time** | **float** | Total inference time in seconds. | [optional] 
**status** | [**ASRStatus**](ASRStatus.md) |  | [optional] 
**results** | [**list[SpeechRecognitionResult]**](SpeechRecognitionResult.md) | Sequential list of transcription results corresponding to sequential portions of audio. May contain one or more recognition hypotheses (up to the maximum specified in maxAlternatives). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


