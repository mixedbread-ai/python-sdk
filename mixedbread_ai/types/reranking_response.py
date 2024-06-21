# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .object_type import ObjectType
from .ranked_document import RankedDocument
from .usage import Usage

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RerankingResponse(pydantic.BaseModel):
    usage: Usage = pydantic.Field()
    """
    The usage of the model
    """

    model: str = pydantic.Field()
    """
    The model used
    """

    data: typing.List[RankedDocument] = pydantic.Field()
    """
    The ranked documents.
    """

    object: typing.Optional[ObjectType] = pydantic.Field(default=None)
    """
    The object type of the response
    """

    top_k: int = pydantic.Field()
    """
    The number of documents to return.
    """

    return_input: bool = pydantic.Field()
    """
    Whether to return the documents.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
