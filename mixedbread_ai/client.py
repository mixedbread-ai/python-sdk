import os
from typing import Any, Optional, Union, Dict

from mixedbread_ai.mixedbread_ai_client.client import AuthenticatedClient
from mixedbread_ai.mixedbread_ai_client.models import EmbeddingsRequest, EmbeddingsResponse
from mixedbread_ai.mixedbread_ai_client.api.mixedbread_ai import embeddings

class MixedbreadAi:
    _client = None

    def __init__(self,
                 api_key: Optional[str] = None,
                 base_path: str = "https://api.mixedbread.ai",
                 headers: Optional[Dict[str, str]] = None,
                 cookies: Optional[Dict[str, str]] = None,
                 timeout: Optional[float] = None,
                 verify_ssl: bool = True,
                 raise_for_status: bool = False
                 ) -> None:
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        if api_key is None:
            api_key = os.environ.get("MIXEDBREAD_API_KEY", os.environ.get("MIXEDBREADAI_API_KEY", None))
            if api_key is None:
                raise Exception("Missing API key. Please set MIXEDBREAD_API_KEY environment variable or pass it to the constructor.")

        if base_path is None:
            raise Exception("Missing basePath")

        self._client = AuthenticatedClient(
            base_url=base_path,
            token=api_key,
            headers={
                "User-Agent": "@mixedbread-ai/python-sdk",
                **headers,
            },
            cookies=cookies,
            timeout=timeout,
            raise_on_unexpected_status=raise_for_status,
            verify_ssl=verify_ssl,
        )

    def embeddings(self,
                   model: str,
                   input: Union[str, list[str]],
                   instruction: Optional[str] = None,
                   normalized: Optional[bool] = None,
                   **kwargs) -> Optional[Union[Any, EmbeddingsResponse]]:
        return embeddings.sync(client=self._client, json_body=EmbeddingsRequest(
            model=model,
            input_=input,
            instruction=instruction,
            normalized=normalized,
            **kwargs)
        )

    async def async_embeddings(self,
                               model: str,
                               input: Union[str, list[str]],
                               instruction: Optional[str] = None,
                               normalized: Optional[bool] = None,
                               **kwargs) -> Optional[Union[Any, EmbeddingsResponse]]:
        return await embeddings.asyncio(client=self._client, json_body=EmbeddingsRequest(
            model=model,
            input_=input,
            instruction=instruction,
            normalized=normalized,
            **kwargs)
        )