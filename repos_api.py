import httpx
from fastapi import APIRouter, Depends

from deps import get_client
from github_client import fetch_repos_async
from repo_schema import Repo
from repos_api_schema import SummaryRequest, SummaryResponse
from repos_service import summarize

router = APIRouter(prefix="/repos", tags=["repos"])

@router.get('')
async def repos_for_user(username: str, client: httpx.AsyncClient = Depends(get_client)) -> list[Repo]:

    repos = await fetch_repos_async(client, username)

    return repos


@router.post('/summary')
async def repos_summary(body: SummaryRequest, client: httpx.AsyncClient = Depends(get_client)) -> SummaryResponse:

    repos = await fetch_repos_async(client, body.username)

    response = summarize(repos, body.username)

    return response
