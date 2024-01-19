# ModelBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The embeddings model used. | 
**usage** | [**ModelUsage**](ModelUsage.md) |  | 

## Example

```python
from mixedbread_ai.models.model_base_response import ModelBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelBaseResponse from a JSON string
model_base_response_instance = ModelBaseResponse.from_json(json)
# print the JSON string representation of the object
print ModelBaseResponse.to_json()

# convert the object into a dict
model_base_response_dict = model_base_response_instance.to_dict()
# create an instance of ModelBaseResponse from a dict
model_base_response_form_dict = model_base_response.from_dict(model_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


