from pydantic import BaseModel, ConfigDict, EmailStr, model_validator


class BaseAuth(BaseModel):
    model_config = ConfigDict(extra='forbid')

    username: str
    password: str