from pydantic import BaseModel, Field



class SummaryRequest(BaseModel):
    username: str = Field(min_length=1, max_length=39)

class LanguageCount(BaseModel):
    language: str
    repos_count: int

class SummaryResponse(BaseModel):
    username: str
    total_repos: int
    total_stars: int
    top_languages: list[LanguageCount]