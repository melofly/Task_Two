from pydantic import BaseModel, ConfigDict, EmailStr, model_validator

from services.auth.models.base_auth import BaseAuth


class RegisterRequest(BaseAuth):
    password_repeat: str
    email: EmailStr