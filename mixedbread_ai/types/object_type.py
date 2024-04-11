# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObjectType(str, enum.Enum):
    LIST = "list"
    EMBEDDING = "embedding"
    EMBEDDING_DICT = "embedding_dict"
    TEXT_DOCUMENT = "text_document"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        embedding: typing.Callable[[], T_Result],
        embedding_dict: typing.Callable[[], T_Result],
        text_document: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObjectType.LIST:
            return list_()
        if self is ObjectType.EMBEDDING:
            return embedding()
        if self is ObjectType.EMBEDDING_DICT:
            return embedding_dict()
        if self is ObjectType.TEXT_DOCUMENT:
            return text_document()