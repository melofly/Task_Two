import random

from logger.logger import Logger
from services.university.models.grades_models.base_grade import GradeEnum
from services.university.models.grades_models.grades_request import GradesRequest
from services.university.models.grades_models.stats.grades_stats_request import GradesStatsRequest
from services.university.models.groups_models.groups_request import GroupsRequest
from services.university.models.students_models.base_student import DegreeEnum
from services.university.models.students_models.student_request import StudentRequest
from services.university.models.teachers_models.base_teachers import SubjectEnum
from services.university.models.teachers_models.teachers_request import TeacherRequest
from services.university.university_service import UniversityService
from faker import Faker

faker = Faker()

class TestGroupApiContract:
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

        Logger.info('Создание препода')
        teacher = TeacherRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name_female(),
            subject=random.choice([sbj for sbj in SubjectEnum])
        )

        teacher_response = university_service.create_teacher(create_teacher=teacher)

        Logger.info('Создание оценки')

        grade = GradesRequest(
            teacher_id=teacher_response.id,
            student_id=student_response.id,
            grade=random.choice([grade for grade in GradeEnum]),
        )

        grade_t = GradesRequest(
            teacher_id=teacher_response.id,
            student_id=student_response.id,
            grade=random.choice([grade for grade in GradeEnum]),
        )

        grade_res = university_service.create_grade(create_grade_req=grade)
        grade_res_t = university_service.create_grade(create_grade_req=grade_t)

        Logger.info('Подсчет статы')

        grade_stats = GradesStatsRequest(
            teacher_id=teacher_response.id,
            student_id=student_response.id,
            group_id=student_response.group_id
        )

        grade_stats_response = university_service.grade_stats(stats_student=grade_stats)

        actual_min_max = [grade_stats_response.max, grade_stats_response.min]
        excepted_min_max = sorted([grade_res.grade, grade_res_t.grade], reverse=True)

        actual_avg = grade_stats_response.avg
        excepted_avg = (grade_stats_response.max + grade_stats_response.min) / grade_stats_response.count

        assert actual_min_max == excepted_min_max, f'{actual_min_max} вышло, а должно {excepted_min_max}'
        assert actual_avg == excepted_avg, f'{actual_avg} вышло, а должно {excepted_avg}'








