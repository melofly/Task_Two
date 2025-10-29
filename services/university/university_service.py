from services.general.base_service import BaseService
from services.university.helpers.grades_helper import GradesHelper
from services.university.helpers.groups_helper import GroupsHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teachers_helper import TeachersHelper
from services.university.models.groups_models.groups_request import GroupsRequest
from services.university.models.groups_models.groups_success_response import GroupSuccessResponse
from services.university.models.students_models.student_request import StudentRequest
from services.university.models.students_models.student_response_success import StudentResponse
from utils.api_utils import ApiUtils


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils=api_utils)

        self.grades_helper = GradesHelper(self.api_utils)
        self.groups_helper = GroupsHelper(self.api_utils)
        self.students_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeachersHelper(self.api_utils)

    def create_student(self, create_student_request: StudentRequest) -> StudentResponse:
        res = self.students_helper.post_create_student(json=create_student_request.model_dump())
        return StudentResponse(**res.json())

    def create_group(self, create_group_req: GroupsRequest) -> GroupSuccessResponse:
        res = self.groups_helper.post_create_group(json=create_group_req.model_dump())
        return GroupSuccessResponse(**res.json())