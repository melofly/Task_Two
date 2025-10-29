from services.general.base_helper import BaseHelper


class GradesHelper(BaseHelper):
    ENDPOINT_PREFIX = '/grades'

    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    GRADE_ID_ENDPOINT = f'{ENDPOINT_PREFIX}/{{grade_id}}/'
    GRADE_STATS = F'{ENDPOINT_PREFIX}/stats/'

    def post_create_grade(self, json=None):
        res = self.api_utils.post(
            endpoint_url=self.ROOT_ENDPOINT,
            json=json
        )
        return res

    def get_grades(self):
        res = self.api_utils.get(
            endpoint_url=self.ROOT_ENDPOINT
        )
        return res

    def delete_grade(self, index: str):
        res = self.api_utils.delete(
            endpoint_url=self.GRADE_ID_ENDPOINT.format(grade_id=index)
        )
        return res

    def get_stats_grade(self):
        res = self.api_utils.get(
            endpoint_url=self.GRADE_STATS
        )
        return res

    def put_grade(self, index: str, json=None):
        res = self.api_utils.put(
            endpoint_url=self.GRADE_ID_ENDPOINT.format(grade_id=index),
            json=json
        )
        return res



