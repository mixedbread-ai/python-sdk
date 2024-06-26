# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .object_type import ObjectType
from .ranked_document import RankedDocument
from .usage import Usage


class RerankingResponse(pydantic_v1.BaseModel):
    usage: Usage = pydantic_v1.Field()
    """
    The usage of the model
    """

    model: str = pydantic_v1.Field()
    """
    The model used
    """

    data: typing.List[RankedDocument] = pydantic_v1.Field()
    """
    The ranked documents.
    """

    object: typing.Optional[ObjectType] = pydantic_v1.Field(default=None)
    """
    The object type of the response
    """

    top_k: int = pydantic_v1.Field()
    """
    The number of documents to return.
    """

    return_input: bool = pydantic_v1.Field()
    """
    Whether to return the documents.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
