# TTSAudioConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_encoding** | [**AudioEncoding**](AudioEncoding.md) |  | 
**sample_rate_hertz** | **int** | Sample rate in Hertz of the audio data sent in all RecognitionAudio messages. Valid values are 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that is not possible, use the native sample rate of the audio source (instead of re-sampling). This field is required for all audio formats. In Text to Speech endpoint is the synthesis sample rate (in hertz) for audio and Optional. If this is different from the voice&#39;s natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality), unless the specified sample rate is not supported for the encoding chosen.  | [default to 16000]
**speaking_rate** | **float** | Optional speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values &lt; 0.25 or &gt; 4.0 will return an error.  | [optional] 
**pitch** | **float** | Optional speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch.  | [optional] 
**volume_gain_db** | **float** | Optional volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. Strongly recommend not to exceed +10 (dB) as there&#39;s usually no effective increase in loudness for any value greater than that.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


