from typing import Annotated

from pydantic import BaseModel, Field


class Owner(BaseModel):
    username: Annotated[str, Field(min_length=1, alias="login")]
    html_url: Annotated[str, Field(min_length=1)]

class Repo(BaseModel):
    full_name: Annotated[str, Field(min_length=1)]
    stargazers_count: Annotated[int, Field(ge=0)]
    name: Annotated[str, Field(min_length=1)]
    html_url: Annotated[str, Field(min_length=1)]
    language: str | None = None
    owner: Owner