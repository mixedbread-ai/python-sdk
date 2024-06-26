# This file was auto-generated by Fern from our API Definition.

from ..core.api_error import ApiError
from ..types.bad_request_error_body import BadRequestErrorBody


class BadRequestError(ApiError):
    def __init__(self, body: BadRequestErrorBody):
        super().__init__(status_code=400, body=body)
