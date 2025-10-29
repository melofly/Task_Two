from pydantic import BaseModel, ConfigDict, EmailStr, model_validator

from services.auth.models.base_auth import BaseAuth


class RegisterRequest(BaseAuth):
    password_repeat: str
    email: EmailStr
    #
    # @model_validator(mode='after')
    # def validate_passwords_match(self):
    #     if self.password != self.password_repeat:
    #         raise ValueError("Пароли не совпадают")
    #     return self

