from http import HTTPStatus

import pytest
import requests.status_codes
from faker import Faker
from services.university.helpers.groups_helper import GroupsHelper
from services.university.models.groups_models.groups_request import GroupsRequest

faker = Faker()

class TestGroupApiContract:
    def test_create_group_no_auth(self, university_api_utils_anonym):
        group_helper = GroupsHelper(api_utils=university_api_utils_anonym)

        response = group_helper.post_create_group(GroupsRequest(name=faker.name()).model_dump())

        actual = response.status_code
        expected = HTTPStatus.FORBIDDEN

        assert actual == expected, f'не тот статус {actual} сейчас, а должен {expected}'