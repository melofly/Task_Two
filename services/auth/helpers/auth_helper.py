from services.general.base_helper import BaseHelper

class AuthHelpers(BaseHelper):
    ENDPOINT_PREFIX = '/auth'

    REG_ENDPOINT = f'{ENDPOINT_PREFIX}/register/'
    LOG_ENDPOINT = f'{ENDPOINT_PREFIX}/login/'

    def post_register(self, data=None):
        response = self.api_utils.post(
            endpoint_url=self.REG_ENDPOINT,
            data=data
        )
        return response

    def post_login(self, data=None):
        response = self.api_utils.post(
            endpoint_url=self.LOG_ENDPOINT,
            data=data
        )
        return response
