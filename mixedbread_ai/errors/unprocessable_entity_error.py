# This file was auto-generated by Fern from our API Definition.

from ..core.api_error import ApiError
from ..types.validation_error import ValidationError


class UnprocessableEntityError(ApiError):
    def __init__(self, body: ValidationError):
        super().__init__(status_code=422, body=body)
