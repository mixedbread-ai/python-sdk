from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_usage import ModelUsage


T = TypeVar("T", bound="ModelBaseResponse")


@_attrs_define
class ModelBaseResponse:
    """
    Attributes:
        model (str): The embeddings model used.
        usage (ModelUsage):
    """

    model: str
    usage: "ModelUsage"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model

        usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_usage import ModelUsage

        d = src_dict.copy()
        model = d.pop("model")

        usage = ModelUsage.from_dict(d.pop("usage"))

        model_base_response = cls(
            model=model,
            usage=usage,
        )

        model_base_response.additional_properties = d
        return model_base_response

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
