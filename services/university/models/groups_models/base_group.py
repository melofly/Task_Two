from pydantic import BaseModel, ConfigDict


class BaseModelGroup(BaseModel):
    model_config = ConfigDict(extra='forbid')

    name: str
