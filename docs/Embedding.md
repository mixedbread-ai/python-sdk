# Embedding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | **List[float]** | The generated embeddings. | 
**index** | **int** | Index of the request text the embedding corresponds to. | 
**truncated** | **bool** | Indicates if the text was truncated for the model. | [optional] 

## Example

```python
from mixedbread_ai.models.embedding import Embedding

# TODO update the JSON string below
json = "{}"
# create an instance of Embedding from a JSON string
embedding_instance = Embedding.from_json(json)
# print the JSON string representation of the object
print Embedding.to_json()

# convert the object into a dict
embedding_dict = embedding_instance.to_dict()
# create an instance of Embedding from a dict
embedding_form_dict = embedding.from_dict(embedding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


