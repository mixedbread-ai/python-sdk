from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingsRequest")


@_attrs_define
class EmbeddingsRequest:
    """
    Attributes:
        model (str): Specifies the model to be used for generating embeddings.
        input_ (Union[List[str], str]): Specifies the input for which the embeddings should be generated.
        instruction (Union[Unset, str]): Required only for instruction based models. Specifies the instruction for
            generating embeddings.
        normalized (Union[Unset, bool]): Specifies whether the embeddings should be normalized.
    """

    model: str
    input_: Union[List[str], str]
    instruction: Union[Unset, str] = UNSET
    normalized: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model

        input_: Union[List[str], str]
        if isinstance(self.input_, list):
            input_ = self.input_

        else:
            input_ = self.input_

        instruction = self.instruction

        normalized = self.normalized

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "input": input_,
            }
        )
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if normalized is not UNSET:
            field_dict["normalized"] = normalized

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model")

        def _parse_input_(data: object) -> Union[List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_type_0 = cast(List[str], data)

                return input_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], str], data)

        input_ = _parse_input_(d.pop("input"))

        instruction = d.pop("instruction", UNSET)

        normalized = d.pop("normalized", UNSET)

        embeddings_request = cls(
            model=model,
            input_=input_,
            instruction=instruction,
            normalized=normalized,
        )

        embeddings_request.additional_properties = d
        return embeddings_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
