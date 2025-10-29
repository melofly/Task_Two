from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class GradeStatisticResponse(BaseModel):
    model_config = ConfigDict(extra='forbid')

    count: int = Field(ge=0)
    min: Optional[int] = Field(None, ge=0, le=5)
    max: Optional[int] = Field(None, ge=0, le=5)
    avg: Optional[float] = Field(None, ge=0, le=5)