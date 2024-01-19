# mixedbread.ai Python SDK

## Introduction to mixedbread.ai
mixedbread.ai is a cutting-edge research and development company specializing in Natural Language Processing (NLP). At our core, we focus on advancing the field of NLP through innovative research, offering powerful tools for embeddings, retrieval, and other NLP functionalities. Our mission is to make NLP accessible to everyone on every device. To learn more about mixedbread.ai, visit our [website](https://mixedbread.ai/).

## Requirements.
Please note that for now this SDK does not support synchronous requests. All requests are asynchronous and require Python 3.7+. If you need support for synchronous requests, please open an issue on GitHub.

Python 3.7+

asyncio
## Installation & Usage
### Installation

If the python package is hosted on a repository, you can install directly using:

```sh
pip install mixedbread_ai
```

### Usage

```python
from mixedbread_ai import MixedbreadAi
import os
os.environ["MIXEDBREADAI_API_KEY"] = "{YOUR_API_KEY}"

client = MixedbreadAi()
embeddings = await client.embeddings({
    "texts": ["Hello world!", "How are you?"],
    "model": "e5-large-v2"
})

print(embeddings)
```

Alternatively, you can set the api key via configuration:
```python
from mixedbread_ai import MixedbreadAi
client = MixedbreadAi(
    api_key="{YOUR_API_KEY}",
    retries=3,
    headers={"User-Agent": "mixedbread-ai-python-sdk"},
    client_side_validation=False, # Speed up requests by disabling client side validation
)

embeddings = await client.embeddings({
    "texts": "Hello world!",
    "model": "e5-large-v2"
})

print(embeddings)
```

Don't forget to replace `"{YOUR_API_KEY}"` with your actual API key. If you don't have an API key, you can get one for free by signing up for an account at [mixedbread.ai](https://mixedbread.ai/).