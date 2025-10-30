from services.university.models.grades_models.base_grade import BaseModelGrades
from pydantic import BaseModel


class GradesStatsRequest(BaseModel):
    teacher_id: int
    student_id: int
    group_id: int