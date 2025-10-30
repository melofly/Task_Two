import random
from http import HTTPStatus

import pytest

from services.university.helpers.grades_helper import GradesHelper
from services.university.models.grades_models.base_grade import MIN_MARK, MAX_MARK
from services.university.models.grades_models.grades_request import GradesRequest
from services.university.models.grades_models.stats.grades_stats_request import GradesStatsRequest
from services.university.university_service import UniversityService
from faker import Faker

faker = Faker()

class TestGroupApiContract:
    @pytest.mark.usefixtures('university_api_test_group')
    def test_validation_keys(
            self,
            university_api_utils_admin,
            university_api_test_teacher,
            university_api_test_student
    ):
        Logger.info('Создаем оценку')
        university_service = UniversityService(api_utils=university_api_utils_admin)
        grade = GradesRequest(
            teacher_id=university_api_test_teacher.id,
            student_id=university_api_test_student.id,
            grade=random.choice([grade for grade in range(MIN_MARK, MAX_MARK + 1)]),
        )

        grade_t = GradesRequest(
            teacher_id=university_api_test_teacher.id,
            student_id=university_api_test_student.id,
            grade=random.choice([grade for grade in range(MIN_MARK, MAX_MARK + 1)]),
        )

        grade_res = university_service.create_grade(create_grade_req=grade)
        grade_res_t = university_service.create_grade(create_grade_req=grade_t)

        Logger.info('Проверяем оценки')
        grade_stats = GradesStatsRequest(
            teacher_id=university_api_test_teacher.id,
            student_id=university_api_test_student.id,
            group_id=university_api_test_student.group_id
        )

        grade_stats_response = university_service.get_grade_stats(stats_student=grade_stats)

        actual_min_max = [grade_stats_response.max, grade_stats_response.min]
        excepted_min_max = sorted([grade_res.grade, grade_res_t.grade], reverse=True)

        actual_avg = grade_stats_response.avg
        excepted_avg = (grade_stats_response.max + grade_stats_response.min) / grade_stats_response.count

        assert actual_min_max == excepted_min_max, f'{actual_min_max} вышло, а должно {excepted_min_max}'
        assert actual_avg == excepted_avg, f'{actual_avg} вышло, а должно {excepted_avg}'


    @pytest.mark.skip(reason='Пока не работает')
    @pytest.mark.usefixtures('university_api_test_group')
    def test_validation_errors_for_grades_stats(
            self,
            university_api_utils_admin,
            university_api_test_teacher,
            university_api_test_student,
            university_api_test_grade
    ):
        Logger.info('Проверяем оценку с неправильными данными на вход')
        grade_helper = GradesHelper(api_utils=university_api_utils_admin)
        grade_stats = GradesStatsRequest(
            teacher_id=university_api_test_teacher.id,
            student_id='5555',
            group_id=university_api_test_student.group_id
        )
        res = grade_helper.get_stats_grade(params=grade_stats)
        
        actual = status_code
        excepted = HTTPStatus.UNPROCESSABLE_CONTENT

        assert res.status_code == HTTPStatus.UNPROCESSABLE_CONTENT, f'Должно быть {excepted}, есть на самом деле {actual}'