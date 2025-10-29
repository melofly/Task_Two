from services.general.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = '/students'

    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    STUDENT_ID_ENDPOINT = f'{ENDPOINT_PREFIX}/{{student_id}}/'

    def post_create_student(self, json=None):
        res = self.api_utils.post(
            endpoint_url=self.ROOT_ENDPOINT,
            json=json
        )
        return res

    def get_students(self):
        res = self.api_utils.get(
            endpoint_url=self.ROOT_ENDPOINT
        )
        return res

    def delete_student(self, index_student: str):
        res = self.api_utils.delete(
            endpoint_url=self.STUDENT_ID_ENDPOINT.format(student_id=index_student)
        )
        return res

    def get_student(self, index_student: str):
        res = self.api_utils.get(
            endpoint_url=self.STUDENT_ID_ENDPOINT.format(student_id=index_student)
        )
        return res

    def put_student(self, index_student: str, json=None):
        res = self.api_utils.put(
            endpoint_url=self.STUDENT_ID_ENDPOINT.format(student_id=index_student),
            json=json
        )
        return res



