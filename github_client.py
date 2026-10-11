import asyncio
from datetime import datetime, timezone
from typing import Any
import httpx
import os

from pydantic import ValidationError, TypeAdapter
from exceptions import *

from repo_schema import Repo


_REPOS_ADAPTER = TypeAdapter(list[Repo])

def _build_headers() -> dict[str, str]:
    headers = {'Accept': 'application/vnd.github+json'}
    token = os.getenv('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'

    return headers

def make_async_client(**kwargs) -> httpx.AsyncClient:
    return httpx.AsyncClient(headers=_build_headers(), timeout=10, **kwargs)

def _parse_repos(response: httpx.Response, username: str) -> list[Repo]:
    status = response.status_code
    if status == httpx.codes.NOT_FOUND:
        raise UserNotFoundError(f'User {username} not found')
    if status == httpx.codes.UNAUTHORIZED:
        raise AuthError('Not authorized')
    if status in (httpx.codes.FORBIDDEN, httpx.codes.TOO_MANY_REQUESTS):
        if response.headers.get('x-ratelimit-remaining') == '0':
            reset_time = response.headers.get('x-ratelimit-reset')
            when = datetime.fromtimestamp(int(reset_time), timezone.utc) if reset_time else "later"
            raise RateLimitError(f'Rate limit exceeded, try again at {when}')
        raise AuthError('Access forbidden')
    if status >= 400:
        raise GithubError(f'Unexpected error from GitHub: {status}')

    try:
        repo_list = _REPOS_ADAPTER.validate_python(response.json())
    except ValidationError as err:
        raise ReposValidationError(err.errors(include_url=False)) from err

    return repo_list

async def _get_with_retry_async(
        client: httpx.AsyncClient,
        url: str,
        params: dict[str, Any],
        attempts: int
    ) -> httpx.Response:

    for attempt in range(1, attempts + 1):
        try:
            return await client.get(url, params=params)
        except httpx.TimeoutException as err:
            if attempt == attempts:
                raise GitHubConnectionError(f'Timeout exceeded after {attempts} attempts') from err
            await asyncio.sleep(attempt)
    raise ValueError('attempts should be greater than 0')

async def fetch_repos_async(client: httpx.AsyncClient, username: str) -> list[Repo]:
    try:
        response = await _get_with_retry_async(
            client,
            f'https://api.github.com/users/{username}/repos',
            params={'per_page': 100},
            attempts=3
        )
    except httpx.RequestError as err:
        raise GitHubConnectionError('Unable to establish connection with GitHub') from err

    return _parse_repos(response, username)