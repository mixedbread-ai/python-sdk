# Embeddings200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | **List[float]** | The generated embeddings. | [optional] 
**index** | **int** | Index of the request text the embedding corresponds to. | [optional] 
**was_truncated** | **bool** | Indicates if the text was truncated for the model. | [optional] 

## Example

```python
from mixedbread_ai.models.embeddings200_response_data_inner import Embeddings200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Embeddings200ResponseDataInner from a JSON string
embeddings200_response_data_inner_instance = Embeddings200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print Embeddings200ResponseDataInner.to_json()

# convert the object into a dict
embeddings200_response_data_inner_dict = embeddings200_response_data_inner_instance.to_dict()
# create an instance of Embeddings200ResponseDataInner from a dict
embeddings200_response_data_inner_form_dict = embeddings200_response_data_inner.from_dict(embeddings200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


