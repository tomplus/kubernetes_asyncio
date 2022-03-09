# FlowcontrolV1beta1Subject

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**V1beta1GroupSubject**](V1beta1GroupSubject.md) |  | [optional] 
**kind** | **str** | Required | 
**service_account** | [**V1beta1ServiceAccountSubject**](V1beta1ServiceAccountSubject.md) |  | [optional] 
**user** | [**V1beta1UserSubject**](V1beta1UserSubject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


