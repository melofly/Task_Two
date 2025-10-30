from enum import IntEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class GradeEnum(IntEnum):
    FAIL = 0
    POOR = 1
    GOOD = 2
    VERY_GOOD = 3
    EXCELLENT = 4
    PERFECT = 5


class BaseModelGrades(BaseModel):
    model_config = ConfigDict(extra='forbid')

    teacher_id: int
    student_id: int
    grade: int = GradeEnum