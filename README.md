# mixedbread ai Python SDK

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Embeddings](#embeddings)
  - [Reranking](#reranking)
- [Error Handling](#error-handling)
- [API Documentation](#api-documentation)

## Requirements
- Python 3.8+

## Installation
You can install directly using:
```sh
pip install mixedbread-ai
```

## Quick Start
Here's a minimal example to get started with the mixedbread ai SDK:
```python
from mixedbread_ai.client import MixedbreadAI

mxbai = MixedbreadAI(api_key="{YOUR_API_KEY}")

embeddings = mxbai.embeddings(
    model="mixedbread-ai/mxbai-embed-large-v1",
    input=["I like to eat apples."]
)

print(embeddings)
```

## Usage

### Embeddings

Here's an example of using the mixedbread ai SDK to create basic embeddings:
```python
from mixedbread_ai.client import MixedbreadAI

mxbai = MixedbreadAI(api_key="{YOUR_API_KEY}")

embeddings = mxbai.embeddings(
    model="mixedbread-ai/mxbai-embed-large-v1",
    input=["I like to eat apples.", "I like to eat bananas."]
)

print(embeddings)
```

By providing a prompt, you can guide the model to produce embeddings that are optimized for your specific use-case or downstream task.

```python
from mixedbread_ai.client import MixedbreadAI

mxbai = MixedbreadAI(api_key="{YOUR_API_KEY}")

embeddings = mxbai.embeddings(
    model="mixedbread-ai/mxbai-embed-large-v1",
    input=["I like to eat apples.", "I like to eat bananas."],
    prompt="Represent this sentence for searching relevant passages"
)

print(embeddings)
```

By specifying the encoding format, you can leverage f.e. binary embeddings.

```python
from mixedbread_ai.client import MixedbreadAI
from mixedbread_ai.types import EncodingFormat

mxbai = MixedbreadAI(api_key="{YOUR_API_KEY}")

embeddings = mxbai.embeddings(
    model="mixedbread-ai/mxbai-embed-large-v1",
    input=["I like to eat apples.", "I like to eat bananas."],
    encoding_format=[EncodingFormat.FLOAT, EncodingFormat.UBINARY]
)

print(embeddings.data[0].embedding.float_, embeddings.data[0].embedding.ubinary)
```

### Reranking (Asynchronous)
Here's an asynchronous example of using the mixedbread ai SDK to rerank documents:
```python
from mixedbread_ai.client import AsyncMixedbreadAI

mxbai_async = AsyncMixedbreadAI(api_key="{YOUR_API_KEY}")

model = "mixedbread-ai/mxbai-rerank-large-v1"
query = "Who wrote 'To Kill a Mockingbird'?"

documents = [
    "'To Kill a Mockingbird' is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature.",
    "The novel 'Moby-Dick' was written by Herman Melville and first published in 1851. It is considered a masterpiece of American literature and deals with complex themes of obsession, revenge, and the conflict between good and evil.",
    "Harper Lee, an American novelist widely known for her novel 'To Kill a Mockingbird', was born in 1926 in Monroeville, Alabama. She received the Pulitzer Prize for Fiction in 1961.",
    "Jane Austen was an English novelist known primarily for her six major novels, which interpret, critique and comment upon the British landed gentry at the end of the 18th century.",
    "The 'Harry Potter' series, which consists of seven fantasy novels written by British author J.K. Rowling, is among the most popular and critically acclaimed books of the modern era.",
    "'The Great Gatsby', a novel written by American author F. Scott Fitzgerald, was published in 1925. The story is set in the Jazz Age and follows the life of millionaire Jay Gatsby and his pursuit of Daisy Buchanan."
]

reranked_docs = await mxbai_async.reranking(
    model=model,
    query=query,
    input=documents
)

print(reranked_docs)
```

Don't forget to replace `"{YOUR_API_KEY}"` with your actual API key. If you don't have an API key, you can get one for free by signing up for an account at [mixedbread.ai](https://mixedbread.ai/).


## Error Handling and Retries
The SDK will raise errors if there is an issue with the API request, such as an invalid API key or a network error. Make sure to handle these exceptions in your code.

```python
from mixedbread_ai.client import MixedbreadAI, ApiError
from mixedbread_ai.types import EncodingFormat

mxbai = MixedbreadAI(api_key="{YOUR_API_KEY}")

try:
    embeddings = mxbai.embeddings(
        model="mixedbread-ai/mxbai-embed-large-v1",
        input=["I like to eat apples.", "I like to eat bananas."],
        encoding_format=[EncodingFormat.FLOAT, EncodingFormat.UBINARY],
        request_options={
            "max_retries": 3,
        }
    )
except ApiError as e:
    print(e.status_code)

print(embeddings.data[0].embedding.float_, embeddings.data[0].embedding.ubinary)
```


## API Documentation
For more information on the available methods and options in the mixedbread ai SDK, please refer to our [API documentation](https://mixedbread.ai/api-reference).