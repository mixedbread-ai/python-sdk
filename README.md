# mixedbread ai Python SDK

## Introduction to mixedbread ai
mixedbread ai is a cutting-edge research and development company specializing in Natural Language Processing (NLP). At our core, we focus on advancing the field of NLP through innovative research, offering powerful tools for embeddings, retrieval, and other NLP functionalities. Our mission is to make NLP accessible to everyone on every device. To learn more about mixedbread ai, visit our [website](https://mixedbread.ai/).


## Requirements.

Python 3.7+

## Installation & Usage
### Installation

If the python package is hosted on a repository, you can install directly using:

```sh
pip install mixedbread_ai
```

### Usage

```python
from mixedbread_ai import MixedbreadAiApi
import os
os.environ["MIXEDBREADAI_API_KEY"] = "{YOUR_API_KEY}"

client = mixedbread_ai.MixedbreadAiApi()
embeddings = client.embeddings({
    "texts": ["Hello world!"],
    "model": "e5-large-v2"
})

print(embeddings)
```

Alternatively, you can set the api key via configuration:
```python
from mixedbread_ai import Configuration, MixedbreadAiApi, ApiClient
client = MixedbreadAiApi(ApiClient(Configuration(api_key="{YOUR_API_KEY}")))
```

Don't forget to replace `"{YOUR_API_KEY}"` with your actual API key. If you don't have an API key, you can get one for free by signing up for an account at [mixedbread.ai](https://mixedbread.ai/).

## Documentation for API Endpoints

All URIs are relative to *https://api.mixedbread.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MixedbreadAiApi* | [**embeddings**](docs/MixedbreadAiApi.md#embeddings) | **POST** /v1/embeddings/ | Create embeddings


## Documentation For Models

 - [Embeddings200Response](docs/Embeddings200Response.md)
 - [Embeddings200ResponseDataInner](docs/Embeddings200ResponseDataInner.md)
 - [Embeddings200ResponseUsage](docs/Embeddings200ResponseUsage.md)
 - [EmbeddingsRequest](docs/EmbeddingsRequest.md)
 - [ErrorResponse](docs/ErrorResponse.md)


