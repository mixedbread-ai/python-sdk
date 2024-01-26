from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.embedding import Embedding
    from ..models.model_usage import ModelUsage


T = TypeVar("T", bound="EmbeddingsResponse")


@attr.s(auto_attribs=True)
class EmbeddingsResponse:
    """
    Attributes:
        normalized (bool): Indicates if the embeddings were normalized.
        data (List['Embedding']):
        model (str): The embeddings model used.
        usage (ModelUsage):
    """

    normalized: bool
    data: List["Embedding"]
    model: str
    usage: "ModelUsage"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        normalized = self.normalized
        data = []
        for componentsschemas_embeddings_list_item_data in self.data:
            componentsschemas_embeddings_list_item = componentsschemas_embeddings_list_item_data.to_dict()

            data.append(componentsschemas_embeddings_list_item)

        model = self.model
        usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "normalized": normalized,
                "data": data,
                "model": model,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.embedding import Embedding
        from ..models.model_usage import ModelUsage

        d = src_dict.copy()
        normalized = d.pop("normalized")

        data = []
        _data = d.pop("data")
        for componentsschemas_embeddings_list_item_data in _data:
            componentsschemas_embeddings_list_item = Embedding.from_dict(componentsschemas_embeddings_list_item_data)

            data.append(componentsschemas_embeddings_list_item)

        model = d.pop("model")

        usage = ModelUsage.from_dict(d.pop("usage"))

        embeddings_response = cls(
            normalized=normalized,
            data=data,
            model=model,
            usage=usage,
        )

        embeddings_response.additional_properties = d
        return embeddings_response

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
