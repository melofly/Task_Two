from requests import Session
import requests
from logger.logger import Logger
import curlify
import json

from selenium.webdriver.support.expected_conditions import none_of

from utils.json_utils import JsonUtils

def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)

        Logger.info(f"Request: {curlify.to_curl(response.request)}")

        body = (
            json.dumps(response.json(), indent=2, ensure_ascii=False)
            if JsonUtils.is_json(response.text)
            else response.text
        )

        Logger.info(
            f"Response status code={response.status_code}, "
            f"elapsed_time={response.elapsed.total_seconds()}s\n{body}\n"
        )

        return response

    return _log_response

class ApiUtils:
    def __init__(self, url: str, headers=None):
        if headers is None:
            headers = {}

        self.session = Session()
        self.session.headers.update(headers)
        self._url = url

    @log_response
    def get(self, endpoint_url, params=None, **kwargs):
        return self.session.get(self._url + endpoint_url, params=params, **kwargs)

    @log_response
    def post(self, endpoint_url, data=None, json=None, **kwargs):
        return self.session.post(
            self._url + endpoint_url,
            data,
            json,
            **kwargs
        )

    @log_response
    def delete(self, endpoint_url, data=None, json=None, **kwargs):
        return self.session.delete(
            url=self._url + endpoint_url,
            data=data,
            json=json,
            **kwargs
        )

    @log_response
    def put(self, endpoint_url, data=None, json=None, **kwargs):
        return self.session.put(
            url=self._url + endpoint_url,
            data=data,
            json=json,
            **kwargs
        )
