# V1EnvFromSource

EnvFromSource represents the source of a set of ConfigMaps or Secrets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_ref** | [**V1ConfigMapEnvSource**](V1ConfigMapEnvSource.md) |  | [optional] 
**prefix** | **str** | Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER. | [optional] 
**secret_ref** | [**V1SecretEnvSource**](V1SecretEnvSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


