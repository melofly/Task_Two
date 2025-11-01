from services.university.models.grades_models.base_grade import BaseModelGrades
from pydantic import BaseModel
from typing import Optional


class GradesStatsRequest(BaseModel):
    teacher_id: int = None
    student_id: int = None
    group_id: int = None