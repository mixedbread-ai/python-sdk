# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.jsonable_encoder import jsonable_encoder
from .core.remove_none_from_dict import remove_none_from_dict
from .core.request_options import RequestOptions
from .environment import MixedbreadAIEnvironment
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
from .types.internal_error import InternalError
from .types.multi_modal_input import MultiModalInput
from .types.multi_modal_reranking_input import MultiModalRerankingInput
from .types.not_found_error_body import NotFoundErrorBody
from .types.query import Query
from .types.reranking_response import RerankingResponse
from .types.too_many_requests_error_body import TooManyRequestsErrorBody
from .types.truncation_strategy import TruncationStrategy
from .types.unauthorized_error_body import UnauthorizedErrorBody
from .types.validation_error import ValidationError

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MixedbreadAI:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: MixedbreadAIEnvironment. The environment to use for requests from the client. from .environment import MixedbreadAIEnvironment

                                                Defaults to MixedbreadAIEnvironment.DEFAULT

        - api_key: str.

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from mixedbread-ai.client import MixedbreadAI

    client = MixedbreadAI(api_key="YOUR_API_KEY", )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MixedbreadAIEnvironment = MixedbreadAIEnvironment.DEFAULT,
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
        input: MultiModalInput,
        normalized: typing.Optional[bool] = OMIT,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        truncation_strategy: typing.Optional[TruncationStrategy] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        instruction: typing.Optional[str] = OMIT,
        texts: typing.Optional[typing.Sequence[str]] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddingsResponse:
        """
        Create embeddings for text or images using the specified model, encoding format, and normalization.

        Parameters:
            - model: str. The model to use for creating embeddings

            - input: MultiModalInput.

            - normalized: typing.Optional[bool]. Whether to normalize the embeddings

            - encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat].

            - truncation_strategy: typing.Optional[TruncationStrategy]. The truncation strategy to use for the input

            - dimensions: typing.Optional[int].

            - instruction: typing.Optional[str].

            - texts: typing.Optional[typing.Sequence[str]].

            - prompt: typing.Optional[str].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixedbread-ai.client import MixedbreadAI

        client = MixedbreadAI(api_key="YOUR_API_KEY", )
        client.embeddings(model="model", input="input", )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "input": input}
        if normalized is not OMIT:
            _request["normalized"] = normalized
        if encoding_format is not OMIT:
            _request["encoding_format"] = encoding_format
        if truncation_strategy is not OMIT:
            _request["truncation_strategy"] = truncation_strategy
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
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
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
            raise UnprocessableEntityError(pydantic.parse_obj_as(ValidationError, _response.json()))  # type: ignore
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
        query: Query,
        input: MultiModalRerankingInput,
        rank_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        return_input: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RerankingResponse:
        """
        Parameters:
            - model: str. The model to use for reranking documents

            - query: Query. The query to rerank the documents

            - input: MultiModalRerankingInput.

            - rank_fields: typing.Optional[typing.Sequence[str]].

            - top_k: typing.Optional[int]. The number of documents to return

            - return_input: typing.Optional[bool]. Whether to return the documents

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixedbread-ai import TextDocument
        from mixedbread-ai.client import MixedbreadAI

        client = MixedbreadAI(api_key="YOUR_API_KEY", )
        client.reranking(model="model", query=TextDocument(text="text", ), input=["input"], top_k=10, return_input=False, )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "query": query, "input": input}
        if rank_fields is not OMIT:
            _request["rank_fields"] = rank_fields
        if top_k is not OMIT:
            _request["top_k"] = top_k
        if return_input is not OMIT:
            _request["return_input"] = return_input
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/reranking"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
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
            raise UnprocessableEntityError(pydantic.parse_obj_as(ValidationError, _response.json()))  # type: ignore
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


class AsyncMixedbreadAI:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: MixedbreadAIEnvironment. The environment to use for requests from the client. from .environment import MixedbreadAIEnvironment

                                                Defaults to MixedbreadAIEnvironment.DEFAULT

        - api_key: str.

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from mixedbread-ai.client import AsyncMixedbreadAI

    client = AsyncMixedbreadAI(api_key="YOUR_API_KEY", )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MixedbreadAIEnvironment = MixedbreadAIEnvironment.DEFAULT,
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
        input: MultiModalInput,
        normalized: typing.Optional[bool] = OMIT,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        truncation_strategy: typing.Optional[TruncationStrategy] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        instruction: typing.Optional[str] = OMIT,
        texts: typing.Optional[typing.Sequence[str]] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddingsResponse:
        """
        Create embeddings for text or images using the specified model, encoding format, and normalization.

        Parameters:
            - model: str. The model to use for creating embeddings

            - input: MultiModalInput.

            - normalized: typing.Optional[bool]. Whether to normalize the embeddings

            - encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat].

            - truncation_strategy: typing.Optional[TruncationStrategy]. The truncation strategy to use for the input

            - dimensions: typing.Optional[int].

            - instruction: typing.Optional[str].

            - texts: typing.Optional[typing.Sequence[str]].

            - prompt: typing.Optional[str].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixedbread-ai.client import AsyncMixedbreadAI

        client = AsyncMixedbreadAI(api_key="YOUR_API_KEY", )
        await client.embeddings(model="model", input="input", )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "input": input}
        if normalized is not OMIT:
            _request["normalized"] = normalized
        if encoding_format is not OMIT:
            _request["encoding_format"] = encoding_format
        if truncation_strategy is not OMIT:
            _request["truncation_strategy"] = truncation_strategy
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
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
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
            raise UnprocessableEntityError(pydantic.parse_obj_as(ValidationError, _response.json()))  # type: ignore
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
        query: Query,
        input: MultiModalRerankingInput,
        rank_fields: typing.Optional[typing.Sequence[str]] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        return_input: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RerankingResponse:
        """
        Parameters:
            - model: str. The model to use for reranking documents

            - query: Query. The query to rerank the documents

            - input: MultiModalRerankingInput.

            - rank_fields: typing.Optional[typing.Sequence[str]].

            - top_k: typing.Optional[int]. The number of documents to return

            - return_input: typing.Optional[bool]. Whether to return the documents

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixedbread-ai import TextDocument
        from mixedbread-ai.client import AsyncMixedbreadAI

        client = AsyncMixedbreadAI(api_key="YOUR_API_KEY", )
        await client.reranking(model="model", query=TextDocument(text="text", ), input=["input"], top_k=10, return_input=False, )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "query": query, "input": input}
        if rank_fields is not OMIT:
            _request["rank_fields"] = rank_fields
        if top_k is not OMIT:
            _request["top_k"] = top_k
        if return_input is not OMIT:
            _request["return_input"] = return_input
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/reranking"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
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
            raise UnprocessableEntityError(pydantic.parse_obj_as(ValidationError, _response.json()))  # type: ignore
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


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MixedbreadAIEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")