from pickle import FALSE

import  pytest
from services.auth.auth_service import AuthService
from services.auth.models.login.login_request import LoginRequest
from services.auth.models.register.register_request import RegisterRequest
from services.university.models.grades_models.base_grade import MIN_MARK, MAX_MARK
from services.university.models.grades_models.grades_request import GradesRequest
from services.university.models.groups_models.groups_request import GroupsRequest
from services.university.models.students_models.base_student import DegreeEnum
from services.university.models.students_models.student_request import StudentRequest
from services.university.models.teachers_models.base_teachers import SubjectEnum
from services.university.models.teachers_models.teachers_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from faker import Faker
import random
import json

faker = Faker()

@pytest.fixture(scope='function', autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils

@pytest.fixture(scope='function', autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils

@pytest.fixture(scope='function')
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              upper_case=True,
                              lower_case=True,
                              digits=True)
    auth_service.register_user(register_req=RegisterRequest(
        username=username,
        password=password,
        password_repeat=password,
        email=faker.email()))

    login_response = auth_service.login_user(login_req=LoginRequest(
        username=username,
        password=password
    ))

    return login_response.access_token

@pytest.fixture(scope='function')
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(
        url=AuthService.SERVICE_URL,
        headers={"Authorization":f"Bearer {access_token}"}
    )
    return api_utils

@pytest.fixture(scope='function')
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(
        url=UniversityService.SERVICE_URL,
        headers={"Authorization":f"Bearer {access_token}"}
    )
    print(f'{access_token}')
    return api_utils

@pytest.fixture(scope='function')
def university_api_test_group(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    group = GroupsRequest(name=faker.name())
    group_response = university_service.create_group(create_group_req=group)
    return group_response

@pytest.fixture(scope='function')
def university_api_test_student(university_api_test_group, university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    student = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name_female(),
        email=faker.email(),
        degree=random.choice([option for option in DegreeEnum]),
        phone=faker.numerify('+79#########'),
        group_id=university_api_test_group.id
    )
    student_response = university_service.create_student(create_student_request=student)
    return student_response

@pytest.fixture(scope='function')
def university_api_test_teacher(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name_female(),
        subject=random.choice([sbj for sbj in SubjectEnum])
    )
    teacher_response = university_service.create_teacher(create_teacher=teacher)
    return teacher_response

@pytest.fixture(scope='function')
def university_api_test_grade(
        university_api_utils_admin,
        university_api_test_student,
        university_api_test_teacher
):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    grade = GradesRequest(
        teacher_id=university_api_test_teacher.id,
        student_id=university_api_test_student.id,
        grade=random.choice([grade for grade in range(MIN_MARK, MAX_MARK + 1)]),
    )
    grade_res = university_service.create_grade(create_grade_req=grade)
    return grade_res

@pytest.fixture(scope='function')
def university_api_test_any_grade(
        university_api_utils_admin,
        university_api_test_student,
        university_api_test_teacher
):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    grade = GradesRequest(
        teacher_id=university_api_test_teacher.id,
        student_id=university_api_test_student.id,
        grade=random.choice([grade for grade in range(MIN_MARK, MAX_MARK + 1)]),
    )
    grade_res = university_service.create_grade(create_grade_req=grade)
    return grade_res


