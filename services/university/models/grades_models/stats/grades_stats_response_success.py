from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

from services.university.models.grades_models.base_grade import GradeEnum


class GradeStatisticResponse(BaseModel):
    model_config = ConfigDict(extra='forbid')

    count: int = Field(ge=0)
    min: Optional[int] = GradeEnum
    max: Optional[int] = GradeEnum
    avg: Optional[float] = GradeEnum