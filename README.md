# mixedbread ai Python SDK

## Introduction to mixedbread ai
mixedbread ai is a cutting-edge research and development company specializing in Natural Language Processing (NLP). At our core, we focus on advancing the field of NLP through innovative research, offering powerful tools for embeddings, retrieval, and other NLP functionalities. Our mission is to make NLP accessible to everyone on every device. To learn more about mixedbread ai, visit our [website](https://mixedbread.ai/).

## Requirements.
Python 3.7+

## Installation & Usage
### Installation

If the python package is hosted on a repository, you can install directly using:

```sh
pip install mixedbread-ai
```

### Usage

```python
from mixedbread_ai import MixedbreadAi
import os
os.environ["MIXEDBREAD_API_KEY"] = "{YOUR_API_KEY}"

mxbai = MixedbreadAi()
embeddings = mxbai.embeddings(
    model="e5-large-v2",
    input=["I like to eat apples.", "I like to eat bananas."]
)

print(embeddings)
```

Alternatively, you can set the api key via configuration:
```python
from mixedbread_ai import MixedbreadAi

mxbai = MixedbreadAi(
    api_key="{YOUR_API_KEY}",
    base_url="https://api.mixedbread.ai",
    timeout=30,
    headers={"X-Custom-Header": "foobar"},
    ...
)
embeddings = mxbai.embeddings(
    model="e5-large-v2",
    input=["I like to eat apples.", "I like to eat bananas."],
    normalized=False
)

print(embeddings)
```

Don't forget to replace `"{YOUR_API_KEY}"` with your actual API key. If you don't have an API key, you can get one for free by signing up for an account at [mixedbread.ai](https://mixedbread.ai/).