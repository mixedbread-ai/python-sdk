# EmbeddingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Specifies the model to be used for generating embeddings. | 
**input** | **List[str]** | A list of text strings for which the embeddings should be generated. | 
**instruction** | **str** | Required only for instruction based models. Specifies the instruction for generating embeddings. | [optional] 
**normalized** | **bool** | Specifies whether the embeddings should be normalized. | [optional] 

## Example

```python
from mixedbread_ai.models.embeddings_request import EmbeddingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsRequest from a JSON string
embeddings_request_instance = EmbeddingsRequest.from_json(json)
# print the JSON string representation of the object
print EmbeddingsRequest.to_json()

# convert the object into a dict
embeddings_request_dict = embeddings_request_instance.to_dict()
# create an instance of EmbeddingsRequest from a dict
embeddings_request_form_dict = embeddings_request.from_dict(embeddings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


