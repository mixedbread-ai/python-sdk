import os
from typing import Optional, Union, Dict, List

from mixedbread_ai.mixedbread_ai_client.api.mixedbread_ai import embeddings
from mixedbread_ai.mixedbread_ai_client.client import AuthenticatedClient
from mixedbread_ai.mixedbread_ai_client.models import EmbeddingsRequest, EmbeddingsResponse, ErrorResponse


class MixedbreadAi:
    """
    A client class for interacting with the Mixedbread AI API.

    This class provides methods for authenticating and making requests to the Mixedbread AI API,
    specifically for generating embeddings based on provided input.

    Attributes:
        _client (AuthenticatedClient): An authenticated client for making API requests.
        _raise_for_status (bool): Whether to raise an exception for HTTP error responses.

    Args:
        api_key (Optional[str]): The API key for authentication. If not provided, it will look for
                                 'MIXEDBREAD_API_KEY' or 'MIXEDBREADAI_API_KEY' in environment variables.
        base_url (str): The base URL of the Mixedbread AI API.
        headers (Optional[Dict[str, str]]): Additional headers to include in requests.
        cookies (Optional[Dict[str, str]]): Cookies to include in requests.
        timeout (Optional[float]): Timeout for API requests.
        verify_ssl (bool): Whether to verify SSL certificates.
        raise_for_status (bool): Whether to raise an exception for HTTP error responses.

    Raises:
        Exception: If the API key is not provided and not found in environment variables.
        Exception: If the base_url is not provided.

    Example:
        ```python
        # Instantiate the client
        mxbai = MixedbreadAi(api_key="{MIXEDBREAD_API_KEY}")

        # Get embeddings for a single string
        response = mxbai.embeddings(model="UAE_Large_V1", input="Hello, world!")

        # Check if the response is an error
        if MixedbreadAi.is_error_response(response):
            print("Error:", response.message)
        else:
            # Process the embeddings
            embeddings = response.embeddings
            print("Embeddings:", embeddings)
        ```

    Note: Replace "your_api_key_here" and "model_name" with your actual API key and the name of the model you intend to use.
    """
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

    @staticmethod
    def is_error_response(response):
        return isinstance(response, ErrorResponse)

    def _handle_response(self, response):
        if self.is_error_response(response) and self._raise_for_status:
            raise RuntimeError(f"mixedbread ai client error - {response.code}: {response.message} \n {response.data}")
        if response is None:
            raise RuntimeError("mixedbread ai client error - no response")
        return response

    def embeddings(self,
                   model: str,
                   input: Union[str, List[str]],
                   instruction: Optional[str] = None,
                   normalized: Optional[bool] = None) -> Optional[Union[ErrorResponse, EmbeddingsResponse]]:
        """
        Synchronously get embeddings for the given input using the specified model.

        Args:
            model (str): The model to use for generating embeddings.
            input (Union[str, List[str]]): The input text or list of texts to embed.
            instruction (Optional[str]): Additional instructions for embedding generation.
            normalized (Optional[bool]): Whether to normalize the embeddings.

        Returns:
            Optional[Union[ErrorResponse, EmbeddingsResponse]]: The response from the API, which could be either
                                                                an error response or an embeddings response.
        """
        return self._handle_response(embeddings.sync(client=self._client, body=EmbeddingsRequest(
            model=model,
            input_=input,
            instruction=instruction,
            normalized=normalized,
        )))

    async def async_embeddings(self,
                               model: str,
                               input: Union[str, List[str]],
                               instruction: Optional[str] = None,
                               normalized: Optional[bool] = None) -> Optional[Union[ErrorResponse, EmbeddingsResponse]]:
        """
        Asynchronously get embeddings for the given input using the specified model.

        Args:
            model (str): The model to use for generating embeddings.
            input (Union[str, List[str]]): The input text or list of texts to embed.
            instruction (Optional[str]): Additional instructions for embedding generation.
            normalized (Optional[bool]): Whether to normalize the embeddings.

        Returns:
            Optional[Union[ErrorResponse, EmbeddingsResponse]]: The response from the API, which could be either
                                                                an error response or an embeddings response.
        """
        return self._handle_response(await embeddings.asyncio(client=self._client, body=EmbeddingsRequest(
            model=model,
            input_=input,
            instruction=instruction,
            normalized=normalized,
        )))
