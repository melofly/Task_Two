import random
import pytest
from services.university.models.grades_models.base_grade import MIN_MARK, MAX_MARK
from services.university.models.grades_models.grades_request import GradesRequest
from services.university.models.grades_models.stats.grades_stats_request import GradesStatsRequest
from services.university.university_service import UniversityService
from faker import Faker

from tests.conftest import university_api_test_student

faker = Faker()

class TestGradesApiContract:
    @pytest.mark.usefixtures('university_api_test_group')
    def test_success_create_grade(
            self,
            university_api_utils_admin,
            university_api_test_teacher,
            university_api_test_student
    ):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        grade = GradesRequest(
            teacher_id=university_api_test_teacher.id,
            student_id=university_api_test_student.id,
            grade=random.choice([grade for grade in range(MIN_MARK, MAX_MARK + 1)]),
        )

        res = university_service.create_grade(create_grade_req=grade)

        actual = res.student_id
        excepted = university_api_test_student.id
        assert actual == excepted, (f'Сейчас: {actual},'
                                    f'Должно: {excepted}')

    @pytest.mark.usefixtures('university_api_test_group')
    def test_student_id_params_grades_stat(
            self,
            university_api_utils_admin,
            university_api_test_grade
    ):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        grade_stats = GradesStatsRequest(
            student_id=university_api_test_grade.student_id,
        )
        res = university_service.get_grade_stats(grade_stats)

        actual = res.max
        excepted = university_api_test_grade.grade

        assert actual == excepted, (f'Сейчас: {actual},'
                                    f'Должно: {excepted}')

    @pytest.mark.usefixtures('university_api_test_group')
    def test_group_id_params_grades_stat(
            self,
            university_api_utils_admin,
            university_api_test_grade,
            university_api_test_student
    ):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        grade_stats = GradesStatsRequest(
            group_id=university_api_test_student.group_id,
        )
        res = university_service.get_grade_stats(grade_stats)

        actual = res.max
        excepted = university_api_test_grade.grade

        assert actual == excepted, (f'Сейчас: {actual},'
                                    f'Должно: {excepted}')

    @pytest.mark.usefixtures('university_api_test_group')
    def test_teacher_id_params_grades_stat(
            self,
            university_api_utils_admin,
            university_api_test_grade,
    ):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        grade_stats = GradesStatsRequest(
            teacher_id=university_api_test_grade.teacher_id
        )
        res = university_service.get_grade_stats(grade_stats)

        actual = res.max
        excepted = university_api_test_grade.grade

        assert actual == excepted, (f'Сейчас: {actual},'
                                    f'Должно: {excepted}')

    @pytest.mark.usefixtures('university_api_test_group')
    def test_no_params_grades_stat(
            self,
            university_api_utils_admin,
            university_api_test_grade,
            university_api_test_student
    ):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        grade_stats = GradesStatsRequest()
        res = university_service.get_grade_stats(grade_stats)

        actual = res.count
        excepted = university_api_test_grade.id

        assert actual == excepted, (f'Сейчас: {actual},'
                                    f'Должно: {excepted}')

    @pytest.mark.usefixtures('university_api_test_group')
    def test_avg_grades_stat(
            self,
            university_api_utils_admin,
            university_api_test_grade,
            university_api_test_student,
            university_api_test_any_grade
    ):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        grade_stats = GradesStatsRequest(
            student_id=university_api_test_student.id
        )
        res = university_service.get_grade_stats(grade_stats)

        actual = res.avg
        excepted = (university_api_test_grade.grade + university_api_test_any_grade.grade) / 2

        assert actual == excepted, (f'Сейчас: {actual},'
                                    f'Должно: {excepted}')
