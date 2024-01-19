import os
import importlib.metadata

from mixedbread_ai.api.mixedbread_ai_api import MixedbreadAiApi
from mixedbread_ai.configuration import Configuration
from mixedbread_ai.api_client import ApiClient
from mixedbread_ai.models import embeddings_request

version = importlib.metadata.version("mixedbread_ai")


class MixedbreadAi:
    def __init__(self,
                 api_key=os.environ.get("MIXEDBREADAI_API_KEY"),
                 basePath="https://api.mixedbread.ai",
                 retries=0,
                 headers={},
                 client_side_validation=True) -> None:
        config = Configuration.get_default()
        config.api_key = {
            "MIXEDBREADAI_API_KEY": api_key,
        }
        config.api_key_prefix = {
            "MIXEDBREADAI_API_KEY": "Bearer"
        }
        if not config.api_key["MIXEDBREADAI_API_KEY"]:
            raise Exception("Missing API key")

        config.host = basePath
        if not config.host:
            raise Exception("Missing basePath")

        config.retries = retries
        config.client_side_validation = client_side_validation

        api_client = ApiClient(config)
        api_client.default_headers = headers
        api_client.user_agent = """mixedbread-ai/python-sdk/{version}"""
        self.client = MixedbreadAiApi(api_client=api_client)

    async def embeddings(self, embeddings_request: embeddings_request, **kwargs):
        if isinstance(embeddings_request["input"], str):
            embeddings_request["input"] = [embeddings_request["input"]]
        return await self.client.embeddings(embeddings_request=embeddings_request, **kwargs)
