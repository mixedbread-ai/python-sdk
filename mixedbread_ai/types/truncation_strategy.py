# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TruncationStrategy(str, enum.Enum):
    """
    Truncation strategies for sentence embeddings
    """

    START = "start"
    END = "end"
    NONE = "none"

    def visit(
        self,
        start: typing.Callable[[], T_Result],
        end: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TruncationStrategy.START:
            return start()
        if self is TruncationStrategy.END:
            return end()
        if self is TruncationStrategy.NONE:
            return none()
