from services.auth.helpers.auth_helper import AuthHelpers
from services.auth.helpers.user_helper import UserHelper
from services.auth.models.login.login_request import LoginRequest
from services.auth.models.login.login_success_response import SuccessResponseLogin
from services.auth.models.register.register_request import RegisterRequest
from services.auth.models.register.register_success_response import SuccessResponseRegister
from services.auth.models.user_me.me_success_response import SuccessResponseMe
from services.general.base_service import BaseService
from utils.api_utils import ApiUtils

class AuthService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.auth_helper = AuthHelpers(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def register_user(self, register_req: RegisterRequest) -> SuccessResponseRegister:
        response = self.auth_helper.post_register(data=register_req.model_dump())
        return SuccessResponseRegister(**response.json())

    def login_user(self, login_req: LoginRequest) -> SuccessResponseLogin:
        response = self.auth_helper.post_login(data=login_req.model_dump())
        return SuccessResponseLogin(**response.json())

    def check_me(self) -> SuccessResponseMe:
        response = self.user_helper.get_me()
        return SuccessResponseMe(**response.json())