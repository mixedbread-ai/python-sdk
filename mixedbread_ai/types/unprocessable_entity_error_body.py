# This file was auto-generated by Fern from our API Definition.

import typing

from .invalid_matryoshka_dimensions_error import InvalidMatryoshkaDimensionsError
from .invalid_matryoshka_model_error import InvalidMatryoshkaModelError
from .model_not_found_error import ModelNotFoundError
from .validation_error import ValidationError
from .web_truncation_error import WebTruncationError

UnprocessableEntityErrorBody = typing.Union[
    ValidationError,
    WebTruncationError,
    InvalidMatryoshkaModelError,
    InvalidMatryoshkaDimensionsError,
    ModelNotFoundError,
]