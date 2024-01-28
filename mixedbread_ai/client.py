import os
from typing import Optional, Union, Dict

from mixedbread_ai.mixedbread_ai_client.api.mixedbread_ai import embeddings
from mixedbread_ai.mixedbread_ai_client.client import AuthenticatedClient
from mixedbread_ai.mixedbread_ai_client.models import EmbeddingsRequest, EmbeddingsResponse, ErrorResponse


class MixedbreadAi:
    _client = None

    def __init__(self,
                 api_key: Optional[str] = None,
                 base_url: str = "https://api.mixedbread.ai",
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
                raise Exception(
                    "Missing API key. Please set MIXEDBREAD_API_KEY environment variable or pass it to the constructor.")

        if base_url is None:
            raise Exception("Missing base_url.")

        self._client = AuthenticatedClient(
            base_url=base_url,
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
        self._raise_for_status = raise_for_status

    def _handle_response(self, response):
        if isinstance(response, ErrorResponse) and self._raise_for_status:
            raise RuntimeError(f"mixedbread ai client error - {response.code}: {response.message} \n {response.data}")
        if response is None:
            raise RuntimeError("mixedbread ai client error - no response")
        return response

    def embeddings(self,
                   model: str,
                   input: Union[str, list[str]],
                   instruction: Optional[str] = None,
                   normalized: Optional[bool] = None) -> Optional[Union[ErrorResponse, EmbeddingsResponse]]:
        return self._handle_response(embeddings.sync(client=self._client, body=EmbeddingsRequest(
            model=model,
            input_=input,
            instruction=instruction,
            normalized=normalized,
        )))

    async def async_embeddings(self,
                               model: str,
                               input: Union[str, list[str]],
                               instruction: Optional[str] = None,
                               normalized: Optional[bool] = None) -> Optional[Union[ErrorResponse, EmbeddingsResponse]]:
        return self._handle_response(await embeddings.asyncio(client=self._client, body=EmbeddingsRequest(
            model=model,
            input_=input,
            instruction=instruction,
            normalized=normalized,
        )))
