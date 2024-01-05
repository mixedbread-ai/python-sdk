# coding: utf-8

"""
    mixedbread-ai

    Discover how to convert text into embeddings with the Embeddings API. Ideal for NLP tasks like text similarity and clustering. Use top open source models or your own fine-tuned models.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from mixedbread_ai.models.embeddings_request_input import EmbeddingsRequestInput
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmbeddingsRequest(BaseModel):
    """
    EmbeddingsRequest
    """ # noqa: E501
    input: Optional[EmbeddingsRequestInput] = None
    model: Optional[StrictStr] = Field(default=None, description="Specifies the model to be used for generating embeddings.")
    instruction: Optional[StrictStr] = Field(default=None, description="Required only for instruction based models. Specifies the instruction for generating embeddings.")
    normalized: Optional[StrictBool] = Field(default=None, description="Specifies whether the embeddings should be normalized.")
    __properties: ClassVar[List[str]] = ["input", "model", "instruction", "normalized"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EmbeddingsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of input
        if self.input:
            _dict['input'] = self.input.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EmbeddingsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input": EmbeddingsRequestInput.from_dict(obj.get("input")) if obj.get("input") is not None else None,
            "model": obj.get("model"),
            "instruction": obj.get("instruction"),
            "normalized": obj.get("normalized")
        })
        return _obj


