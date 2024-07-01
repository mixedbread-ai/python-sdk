# MixedbreadAi Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![pypi](https://img.shields.io/pypi/v/mixedbread-ai)](https://pypi.python.org/pypi/mixedbread-ai)

The MixedbreadAi Python library provides convenient access to the MixedbreadAi API from Python.

## Installation

```sh
pip install mixedbread-ai
```

## Usage

Instantiate and use the client with the following:

```python
from mixedbread-ai.client import MixedbreadAI

client = MixedbreadAI(api_key="YOUR_API_KEY", )
client.embeddings(model='mixedbread-ai/mxbai-embed-large-v1', input='This is a sample text input.', )
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
from mixedbread-ai.client import AsyncMixedbreadAI

client = AsyncMixedbreadAI(api_key="YOUR_API_KEY", )
await client.embeddings(model='mixedbread-ai/mxbai-embed-large-v1', input='This is a sample text input.', )
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
