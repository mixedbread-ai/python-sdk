# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MultipleEncodingsEmbeddingItem(pydantic.BaseModel):
    base_64: typing.List[str] = pydantic.Field(alias="base64")
    binary: typing.List[int]
    float_: typing.List[float] = pydantic.Field(alias="float")
    int_8: typing.List[int] = pydantic.Field(alias="int8")
    ubinary: typing.List[int]
    uint_8: typing.List[int] = pydantic.Field(alias="uint8")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
