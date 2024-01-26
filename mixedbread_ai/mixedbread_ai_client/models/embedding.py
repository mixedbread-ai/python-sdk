from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Embedding")


@attr.s(auto_attribs=True)
class Embedding:
    """
    Attributes:
        embedding (List[float]): The generated embeddings.
        index (int): Index of the request text the embedding corresponds to.
        truncated (Union[Unset, bool]): Indicates if the text was truncated for the model.
    """

    embedding: List[float]
    index: int
    truncated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        embedding = self.embedding

        index = self.index
        truncated = self.truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        embedding = cast(List[float], d.pop("embedding"))

        index = d.pop("index")

        truncated = d.pop("truncated", UNSET)

        embedding = cls(
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
