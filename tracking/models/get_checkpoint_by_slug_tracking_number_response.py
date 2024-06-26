# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

from __future__ import annotations
import pprint

from pydantic import BaseModel
from typing import Any, Dict, Optional
from typing_extensions import Self

from tracking.models.tag_v1 import TagV1
from tracking.models.checkpoint import Checkpoint


class GetCheckpointBySlugTrackingNumberResponse(BaseModel):
    """
    GetCheckpointBySlugTrackingNumberResponse
    """  # noqa: E501

    id: Optional[str] = None
    tracking_number: Optional[str] = None
    slug: Optional[str] = None
    tag: Optional[TagV1] = None
    subtag: Optional[str] = None
    subtag_message: Optional[str] = None
    checkpoint: Optional[Checkpoint] = None

    def to_str(self, **kwargs) -> str:
        return pprint.pformat(self.model_dump(**kwargs))

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        return self.model_dump(**kwargs)

    @classmethod
    def from_json(cls, json_str: str, **kwargs) -> Optional[Self]:
        return cls.model_validate_json(json_str, **kwargs)

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]], **kwargs) -> Optional[Self]:
        return cls.model_validate(obj, **kwargs) if isinstance(obj, Dict) else None
