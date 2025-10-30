from enum import IntEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

MIN_MARK = 0
MAX_MARK = 5

GRADE_INTERVAL = range(MIN_MARK, MAX_MARK + 1)

class BaseModelGrades(BaseModel):
    model_config = ConfigDict(extra='forbid')

    teacher_id: int
    student_id: int
    grade: int = GradeEnum