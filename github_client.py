import time
from typing import Any
import httpx
import os

from pydantic import ValidationError, TypeAdapter
from pydantic_core import ErrorDetails

from repo_schema import Repo

class GithubError(Exception):
    pass

class UserNotFoundError(GithubError):
    pass

class AuthError(GithubError):
    pass

class RateLimitError(GithubError):
    pass

class GitHubConnectionError(GithubError):
    pass

class ReposValidationError(GithubError):
    def __init__(self, errors: list[ErrorDetails]) -> None:
        self.errors = errors
        super().__init__(f'{len(errors)} validation errors in GitHub response encountered')

def _get_with_retry(client: httpx.Client, url: str, params: dict[str, Any], attempts) -> httpx.Response:
    for attempt in range(1, attempts + 1):
        try:
            return client.get(url, params=params)
        except httpx.TimeoutException as err:
            if attempt == attempts:
                raise GitHubConnectionError(f'Timeout exceeded after {attempts} attempts') from err
            time.sleep(attempt)
    raise ValueError('attempts should be greater than 0')


def fetch_repos(username: str) -> list[Repo]:
    headers = {'Accept': 'application/vnd.github+json'}
    token = os.getenv('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'

    with httpx.Client(
        headers=headers,
        timeout=10
    ) as client:
        try:
            response = _get_with_retry(
                client,
                f'https://api.github.com/users/{username}/repos',
                params={'per_page': 100},
                attempts=3
            )
        except httpx.RequestError as err:
            raise GitHubConnectionError('Unable to establish connection with GitHub') from err

    status = response.status_code
    if status == httpx.codes.NOT_FOUND:
        raise UserNotFoundError(f'User {username} not found')
    if status == httpx.codes.UNAUTHORIZED:
        raise AuthError('Not authorized')
    if status in (httpx.codes.FORBIDDEN, httpx.codes.TOO_MANY_REQUESTS):
        if response.headers.get('x-ratelimit-remaining') == '0':
            raise RateLimitError('Rate limit exceeded, try again later')
        raise AuthError('Access forbidden')
    if status >= 400:
        raise GithubError(f'Unexpected error from GitHub: {status}')

    _repos_adapter = TypeAdapter(list[Repo])

    try:
        repo_list = _repos_adapter.validate_python(response.json())
    except ValidationError as err:
        raise ReposValidationError(err.errors(include_url=False)) from err

    return repo_list