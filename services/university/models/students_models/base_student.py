from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, field_validator


class DegreeEnum(StrEnum):
    ASSOCIATE = 'Associate'
    BACHELOR = 'Bachelor'
    MASTER = 'Master'
    DOCTORATE = 'Doctorate'


class BaseModelStudent(BaseModel):
    model_config = ConfigDict(extra='forbid')

    first_name: str
    last_name: str
    email: EmailStr
    degree: DegreeEnum
    phone: str
    group_id: int

    @field_validator('phone')
    def validator_phone(cls, v):
        if len(v) != 12:
            raise ValueError("Номер телефона должен содержать 12 символов")
        if not v.startswith('+79'):
            raise ValueError("Номер телефона должен начинаться с '+79'")
        return v

