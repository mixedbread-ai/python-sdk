from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Embedding")


@_attrs_define
class Embedding:
    """
    Attributes:
        object_ (str): The object type.
        embedding (List[float]): The generated embeddings.
        index (int): Index of the request text the embedding corresponds to.
        truncated (Union[Unset, bool]): Indicates if the text was truncated for the model.
    """

    object_: str
    embedding: List[float]
    index: int
    truncated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_

        embedding = self.embedding

        index = self.index

        truncated = self.truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "embedding": embedding,
                "index": index,
            }
        )
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = d.pop("object")

        embedding = cast(List[float], d.pop("embedding"))

        index = d.pop("index")

        truncated = d.pop("truncated", UNSET)

        embedding = cls(
            object_=object_,
            embedding=embedding,
            index=index,
            truncated=truncated,
        )

        embedding.additional_properties = d
        return embedding

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
