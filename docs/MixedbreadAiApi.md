# mixedbread_ai.MixedbreadAiApi

All URIs are relative to *https://api.mixedbread.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**embeddings**](MixedbreadAiApi.md#embeddings) | **POST** /v1/embeddings/ | Create embeddings


# **embeddings**
> EmbeddingsResponse embeddings(embeddings_request)

Create embeddings

This endpoint allows you to post text data and receive embeddings in response. The embeddings are generated using the model specified in the request body.

### Example

* Api Key Authentication (MIXEDBREADAI_API_KEY):

```python
import time
import os
import mixedbread_ai
from mixedbread_ai.models.embeddings_request import EmbeddingsRequest
from mixedbread_ai.models.embeddings_response import EmbeddingsResponse
from mixedbread_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixedbread.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = mixedbread_ai.Configuration(
    host = "https://api.mixedbread.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: MIXEDBREADAI_API_KEY
configuration.api_key['MIXEDBREADAI_API_KEY'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['MIXEDBREADAI_API_KEY'] = 'Bearer'

# Enter a context with an instance of the API client
async with mixedbread_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixedbread_ai.MixedbreadAiApi(api_client)
    embeddings_request = mixedbread_ai.EmbeddingsRequest() # EmbeddingsRequest | 

    try:
        # Create embeddings
        api_response = await api_instance.embeddings(embeddings_request)
        print("The response of MixedbreadAiApi->embeddings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MixedbreadAiApi->embeddings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embeddings_request** | [**EmbeddingsRequest**](EmbeddingsRequest.md)|  | 

### Return type

[**EmbeddingsResponse**](EmbeddingsResponse.md)

### Authorization

[MIXEDBREADAI_API_KEY](../README.md#MIXEDBREADAI_API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully generated embeddings. |  -  |
**400** | Bad Request. The request was not valid, indicating issues like missing parameters or incorrect data formats. |  -  |
**401** | Unauthorized. Authentication failed, or the user lacks the necessary permissions for the requested operation. |  -  |
**402** | Required Payment. The request is valid but cannot proceed without a balance top-up. |  -  |
**404** | Not Found. The requested resource is not available or does not exist. |  -  |
**429** | Too Many Requests. Too many requests have been sent in a given amount of time, exceeding the rate limit. |  -  |
**500** | Internal Server Error. An unexpected error occurred on the server side. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

