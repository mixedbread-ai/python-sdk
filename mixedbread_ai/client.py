# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.jsonable_encoder import jsonable_encoder
from .environment import MixedbreadAiApiEnvironment
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.internal_server_error import InternalServerError
from .errors.not_found_error import NotFoundError
from .errors.too_many_requests_error import TooManyRequestsError
from .errors.unauthorized_error import UnauthorizedError
from .errors.unprocessable_entity_error import UnprocessableEntityError
from .types.bad_request_error_body import BadRequestErrorBody
from .types.embeddings_request_encoding_format import EmbeddingsRequestEncodingFormat
from .types.embeddings_response import EmbeddingsResponse
from .types.forbidden_error_body import ForbiddenErrorBody
from .types.input import Input
from .types.internal_error import InternalError
from .types.not_found_error_body import NotFoundErrorBody
from .types.reranking_response import RerankingResponse
from .types.text_document import TextDocument
from .types.too_many_requests_error_body import TooManyRequestsErrorBody
from .types.truncation_strategy import TruncationStrategy
from .types.unauthorized_error_body import UnauthorizedErrorBody
from .types.unprocessable_entity_error_body import UnprocessableEntityErrorBody

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MixedbreadAiApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MixedbreadAiApiEnvironment = MixedbreadAiApiEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )

    def embeddings(
        self,
        *,
        model: str,
        input: Input,
        normalized: typing.Optional[bool] = OMIT,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        truncation_strategy: typing.Optional[TruncationStrategy] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        instruction: typing.Optional[str] = OMIT,
        texts: typing.Optional[typing.List[str]] = OMIT,
        prompt: typing.Optional[str] = OMIT,
    ) -> EmbeddingsResponse:
        """
        Create embeddings for text or images using the specified model, encoding format, and normalization.

        Parameters:
            - model: str. The model to use for creating embeddings

            - input: Input.

            - normalized: typing.Optional[bool]. Whether to normalize the embeddings

            - encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat].

            - truncation_strategy: typing.Optional[TruncationStrategy]. The truncation strategy to use for the input

            - dimensions: typing.Optional[int].

            - instruction: typing.Optional[str].

            - texts: typing.Optional[typing.List[str]].

            - prompt: typing.Optional[str].
        ---
        from mixedbread-ai.client import MixedbreadAiApi

        client = MixedbreadAiApi(api_key="YOUR_API_KEY", )
        client.embeddings(model="model", )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "input": input}
        if normalized is not OMIT:
            _request["normalized"] = normalized
        if encoding_format is not OMIT:
            _request["encoding_format"] = encoding_format
        if truncation_strategy is not OMIT:
            _request["truncation_strategy"] = truncation_strategy.value
        if dimensions is not OMIT:
            _request["dimensions"] = dimensions
        if instruction is not OMIT:
            _request["instruction"] = instruction
        if texts is not OMIT:
            _request["texts"] = texts
        if prompt is not OMIT:
            _request["prompt"] = prompt
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/embeddings"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EmbeddingsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequestErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ForbiddenErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic.parse_obj_as(UnprocessableEntityErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 429:
            raise TooManyRequestsError(
                pydantic.parse_obj_as(TooManyRequestsErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(InternalError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def reranking(
        self,
        *,
        model: str,
        input: typing.List[TextDocument],
        query: TextDocument,
        top_k: typing.Optional[int] = OMIT,
        return_input: typing.Optional[bool] = OMIT,
    ) -> RerankingResponse:
        """
        Parameters:
            - model: str. The model to use for creating embeddings

            - input: typing.List[TextDocument]. The input documents to rerank

            - query: TextDocument. The query to rerank the documents

            - top_k: typing.Optional[int]. The number of documents to return

            - return_input: typing.Optional[bool]. Whether to return the documents
        ---
        from mixedbread-ai import TextDocument
        from mixedbread-ai.client import MixedbreadAiApi

        client = MixedbreadAiApi(api_key="YOUR_API_KEY", )
        client.reranking(model="model", input=[TextDocument(text="text", )], query=TextDocument(text="text", ), top_k=10, return_input=False, )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "input": input, "query": query}
        if top_k is not OMIT:
            _request["top_k"] = top_k
        if return_input is not OMIT:
            _request["return_input"] = return_input
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/reranking"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RerankingResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequestErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ForbiddenErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic.parse_obj_as(UnprocessableEntityErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 429:
            raise TooManyRequestsError(
                pydantic.parse_obj_as(TooManyRequestsErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(InternalError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMixedbreadAiApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MixedbreadAiApiEnvironment = MixedbreadAiApiEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )

    async def embeddings(
        self,
        *,
        model: str,
        input: Input,
        normalized: typing.Optional[bool] = OMIT,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        truncation_strategy: typing.Optional[TruncationStrategy] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        instruction: typing.Optional[str] = OMIT,
        texts: typing.Optional[typing.List[str]] = OMIT,
        prompt: typing.Optional[str] = OMIT,
    ) -> EmbeddingsResponse:
        """
        Create embeddings for text or images using the specified model, encoding format, and normalization.

        Parameters:
            - model: str. The model to use for creating embeddings

            - input: Input.

            - normalized: typing.Optional[bool]. Whether to normalize the embeddings

            - encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat].

            - truncation_strategy: typing.Optional[TruncationStrategy]. The truncation strategy to use for the input

            - dimensions: typing.Optional[int].

            - instruction: typing.Optional[str].

            - texts: typing.Optional[typing.List[str]].

            - prompt: typing.Optional[str].
        ---
        from mixedbread-ai.client import AsyncMixedbreadAiApi

        client = AsyncMixedbreadAiApi(api_key="YOUR_API_KEY", )
        await client.embeddings(model="model", )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "input": input}
        if normalized is not OMIT:
            _request["normalized"] = normalized
        if encoding_format is not OMIT:
            _request["encoding_format"] = encoding_format
        if truncation_strategy is not OMIT:
            _request["truncation_strategy"] = truncation_strategy.value
        if dimensions is not OMIT:
            _request["dimensions"] = dimensions
        if instruction is not OMIT:
            _request["instruction"] = instruction
        if texts is not OMIT:
            _request["texts"] = texts
        if prompt is not OMIT:
            _request["prompt"] = prompt
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/embeddings"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EmbeddingsResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequestErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ForbiddenErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic.parse_obj_as(UnprocessableEntityErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 429:
            raise TooManyRequestsError(
                pydantic.parse_obj_as(TooManyRequestsErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(InternalError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def reranking(
        self,
        *,
        model: str,
        input: typing.List[TextDocument],
        query: TextDocument,
        top_k: typing.Optional[int] = OMIT,
        return_input: typing.Optional[bool] = OMIT,
    ) -> RerankingResponse:
        """
        Parameters:
            - model: str. The model to use for creating embeddings

            - input: typing.List[TextDocument]. The input documents to rerank

            - query: TextDocument. The query to rerank the documents

            - top_k: typing.Optional[int]. The number of documents to return

            - return_input: typing.Optional[bool]. Whether to return the documents
        ---
        from mixedbread-ai import TextDocument
        from mixedbread-ai.client import AsyncMixedbreadAiApi

        client = AsyncMixedbreadAiApi(api_key="YOUR_API_KEY", )
        await client.reranking(model="model", input=[TextDocument(text="text", )], query=TextDocument(text="text", ), top_k=10, return_input=False, )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "input": input, "query": query}
        if top_k is not OMIT:
            _request["top_k"] = top_k
        if return_input is not OMIT:
            _request["return_input"] = return_input
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/reranking"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RerankingResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequestErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ForbiddenErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic.parse_obj_as(UnprocessableEntityErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 429:
            raise TooManyRequestsError(
                pydantic.parse_obj_as(TooManyRequestsErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(InternalError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MixedbreadAiApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
