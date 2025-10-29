from pydantic import BaseModel


class SuccessResponseMe(BaseModel):
    detail: str


