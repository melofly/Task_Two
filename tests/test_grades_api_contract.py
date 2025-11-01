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

    def test_grades_stats_min_accurate(self, university_api_test_grades_and_stats):
        grade_one, grade_two, stats = university_api_test_grades_and_stats

        actual = stats.min
        expected = min(grade_one.grade, grade_two.grade)
        assert actual == expected, (f'Сейчас: {actual},'
                                    f'Должно: {expected}')

    def test_grades_stats_max_accurate(self, university_api_test_grades_and_stats):
        grade_one, grade_two, stats = university_api_test_grades_and_stats

        actual = stats.max
        expected = max(grade_one.grade, grade_two.grade)
        assert actual == expected, (f'Сейчас: {actual},'
                                    f'Должно: {expected}')

    def test_grades_stats_avg_accurate(self, university_api_test_grades_and_stats):
        grade_one, grade_two, stats = university_api_test_grades_and_stats

        actual = stats.avg
        expected = (grade_one.grade + grade_two.grade) / 2
        assert actual == expected, (f'Сейчас: {actual},'
                                    f'Должно: {expected}')

    def test_grades_stats_count_accurate(self, university_api_test_grades_and_stats):
        grade_one, grade_two, stats = university_api_test_grades_and_stats

        actual = stats.count
        expected = 2
        assert actual == expected, (f'Сейчас: {actual},'
                                    f'Должно: {expected}')