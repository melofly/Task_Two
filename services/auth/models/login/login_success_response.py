from typing import Literal

from pydantic import BaseModel

from services.auth.models.base_auth import BaseAuth


class SuccessResponseLogin(BaseModel):
    access_token: str
    token_type: Literal["Bearer"]