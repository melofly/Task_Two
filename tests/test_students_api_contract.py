import random

from logger.logger import Logger
from services.university.models.groups_models.groups_request import GroupsRequest
from services.university.models.students_models.base_student import DegreeEnum
from services.university.models.students_models.student_request import StudentRequest
from services.university.university_service import UniversityService
from faker import Faker

faker = Faker()


class TestStudentsContract:
    def test_student_create(self, university_api_utils_admin):
        Logger.info('Создание группы')
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group = GroupsRequest(name=faker.name())
        group_response = university_service.create_group(create_group_req=group)

        Logger.info('Создание студента')
        student = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name_female(),
            email=faker.email(),
            degree=random.choice([option for option in DegreeEnum]),
            phone=faker.numerify('+79#########'),
            group_id=group_response.id
        )

        student_response = university_service.create_student(create_student_request=student)

        actual = student_response.group_id
        expected = group_response.id

        assert actual == expected, f'не тот статус {actual} сейчас, а должен {expected}'

