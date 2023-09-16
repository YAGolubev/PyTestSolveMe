from pydantic import BaseModel, Field, validator


class Post (BaseModel):
    # id: int
    id: int = Field(le=3)
    title: str
    # name: str = Field(alias="_name")

    # @validator("id")
    # def check_that_id_is_less_then_two(cls, v):
    #     if v > 2:
    #         raise ValueError("Id is not less than two")
    #     else:
    #         return v
