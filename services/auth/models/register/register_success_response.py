from pydantic import BaseModel


class SuccessResponseRegister(BaseModel):
    detail: str