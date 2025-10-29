from typing import Literal

from services.auth.models.base_auth import BaseAuth


class SuccessResponseLogin(BaseAuth):
    access_token: str
    token_type: Literal["Bearer"]
