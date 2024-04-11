# This file was auto-generated by Fern from our API Definition.

from ..core.api_error import ApiError
from ..types.internal_error import InternalError


class InternalServerError(ApiError):
    def __init__(self, body: InternalError):
        super().__init__(status_code=500, body=body)