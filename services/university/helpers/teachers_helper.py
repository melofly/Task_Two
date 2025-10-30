from services.general.base_helper import BaseHelper


class TeachersHelper(BaseHelper):
    ENDPOINT_PREFIX = '/teachers'

    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    TEACHER_ID_ENDPOINT = f'{ENDPOINT_PREFIX}/{{teacher_id}}/'

    def post_create_teacher(self, json=None):
        res = self.api_utils.post(
            endpoint_url=self.ROOT_ENDPOINT,
            json=json
        )
        return res

    def get_teachers(self):
        res = self.api_utils.get(
            endpoint_url=self.ROOT_ENDPOINT
        )
        return res

    def delete_teacher(self, id: str):
        res = self.api_utils.delete(
            endpoint_url=self.TEACHER_ID_ENDPOINT.format(teacher_id=id)
        )
        return res

    def get_teacher(self, id: str):
        res = self.api_utils.get(
            endpoint_url=self.TEACHER_ID_ENDPOINT.format(teacher_id=id)
        )
        return res

    def put_teacher(self, id: str, json=None):
        res = self.api_utils.put(
            endpoint_url=self.TEACHER_ID_ENDPOINT.format(teacher_id=id),
            json=json
        )
        return res