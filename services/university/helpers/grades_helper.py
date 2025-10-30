from services.general.base_helper import BaseHelper


class GradesHelper(BaseHelper):
    ENDPOINT_PREFIX = '/grades'

    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    GRADE_ID_ENDPOINT = f'{ENDPOINT_PREFIX}/{{grade_id}}/'
    GRADE_STATS = F'{ENDPOINT_PREFIX}/stats/'

    def post_create_grade(self, data=None):
        res = self.api_utils.post(
            endpoint_url=self.ROOT_ENDPOINT,
            data=data
        )
        return res

    def get_grades(self, params=None):
        res = self.api_utils.get(
            endpoint_url=self.ROOT_ENDPOINT,
            params=params
        )
        return res

    def delete_grade(self, id: str):
        res = self.api_utils.delete(
            endpoint_url=self.GRADE_ID_ENDPOINT.format(grade_id=id)
        )
        return res

    def get_stats_grade(self, params=None):
        res = self.api_utils.get(
            endpoint_url=self.GRADE_STATS,
            params=params
        )
        return res

    def put_grade(self, id: str, json=None):
        res = self.api_utils.put(
            endpoint_url=self.GRADE_ID_ENDPOINT.format(grade_id=id),
            json=json
        )
        return res