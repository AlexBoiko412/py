import pathlib

import httpx
import pytest
from _pytest.monkeypatch import MonkeyPatch

from github_client import make_async_client, fetch_repos_async
from exceptions import UserNotFoundError, AuthError, RateLimitError, ReposValidationError, GitHubConnectionError
from save_repos import save_repos
from repo_schema import Repo, Owner, REPOS_ADAPTER

@pytest.fixture
def successful_response():
    return [
        {
            "full_name": "owner123/repo1",
            "name": "repo1",
            "html_url": "https://github.com/owner123/repo1",
            "stargazers_count": 2,
            "owner": {
                "login": "owner123",
                "html_url": "https://github.com/owner123"
            }
        }
    ]

@pytest.fixture
def invalid_response():
    return [
        {
            "full_name": "owner123/repo1",
            "name": False,
            "html_url": "https://github.com/owner123/repo1",
            "stargazers_count": -1,
            "owner": {
                "login": "",
                "html_url": "https://github.com/owner123"
            }
        },
        {
            "full_name": "owner123/repo12",
            "name": "repo12",
            "html_url": 10,
            "stargazers_count": -1,
            "owner": {
                "login": "owner123",
                "html_url": "https://github.com/owner123"
            }
        }
    ]

def create_mock_client(handler, **kwargs) -> httpx.AsyncClient:
    return make_async_client(
        transport=httpx.MockTransport(handler),
        **kwargs
    )

async def test_fetch_repos_success(successful_response: list[dict]):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=200, json=successful_response)

    async with create_mock_client(handler) as client:
        repos = await fetch_repos_async(client, "owner123")

        assert len(repos) == 1
        assert repos[0].full_name == "owner123/repo1"


@pytest.mark.parametrize(
    'status,headers,exc,message',
    [
        (404, {}, UserNotFoundError, "not found"),
        (401, {}, AuthError, "Not authorized"),
        (403, {}, AuthError, "Access forbidden"),
        (403, {"x-ratelimit-remaining": "0", "x-ratelimit-reset": "1791900240"}, RateLimitError, "Rate limit"),
        (429, {"x-ratelimit-remaining": "0"}, RateLimitError, "later"),  # no reset header
    ],
)
async def test_fetch_repos_failed(
        status: int,
        headers: dict[str, str],
        exc,
        message: str,
        monkeypatch: MonkeyPatch
):

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=status, headers=headers)

    async with create_mock_client(handler) as client:
        with pytest.raises(exc, match=message):
            await fetch_repos_async(client, 'owner123')

async def test_fetch_repos_invalid(invalid_response: list[dict]):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=200, json=invalid_response)

    async with create_mock_client(handler) as client:
        with pytest.raises(ReposValidationError) as err:
            await fetch_repos_async(client, "owner123")

        locs = [e['loc'] for e in err.value.errors]
        assert locs == [
            (0, "stargazers_count"),
            (0, "name"),
            (0, "owner", "login"),
            (1, "stargazers_count"),
            (1, "html_url")
        ]

async def test_fetch_repos_timeout_error(monkeypatch: MonkeyPatch):
    async def fake_sleep(seconds: int):
        pass

    monkeypatch.setattr('github_client.asyncio.sleep', fake_sleep)

    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout('Timeout exceeded')

    async with create_mock_client(handler) as client:
        with pytest.raises(GitHubConnectionError):
            await fetch_repos_async(client, "owner123")

def test_save_repos(tmp_path: pathlib.Path):
    repos = [
        Repo(
            full_name = "owner123/repo1",
            name='repo1',
            html_url="https://github.com/owner123/repo1",
            stargazers_count=1,
            owner=Owner(
                login="owner123",
                html_url="https://github.com/owner123"
            )
        ),
        Repo(
            full_name="owner123/repo2",
            name='repo2',
            html_url="https://github.com/owner123/repo2",
            stargazers_count=4,
            owner=Owner(
                login="owner123",
                html_url="https://github.com/owner123"
            )
        ),
        Repo(
            full_name="owner123/repo3",
            name='repo3',
            html_url="https://github.com/owner123/repo3",
            stargazers_count=0,
            owner=Owner(
                login="owner123",
                html_url="https://github.com/owner123"
            )
        )
    ]
    save_repos(repos, tmp_path / 'repos.json')

    with open(tmp_path / 'repos.json', 'r') as f:
        assert REPOS_ADAPTER.validate_json(f.read()) == repos

async def test_sends_bearer_token(monkeypatch: MonkeyPatch, successful_response: list[dict]):
    monkeypatch.setenv('GITHUB_TOKEN', 'token')
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen['auth'] = request.headers.get('Authorization')
        return httpx.Response(status_code=200, json=successful_response)

    async with create_mock_client(handler) as client:
        await fetch_repos_async(client, "owner123")

    assert seen.get('auth') == 'Bearer token'

async def test_retry_then_success(monkeypatch: MonkeyPatch, successful_response: list[dict]):
    sleeps: list[int] = []

    async def fake_sleep(seconds: int):
        sleeps.append(seconds)

    monkeypatch.setattr('github_client.asyncio.sleep', fake_sleep)
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if calls < 3:
            raise httpx.ReadTimeout('Timeout exceeded')
        return httpx.Response(status_code=200, json=successful_response)

    async with create_mock_client(handler) as client:
        repos = await fetch_repos_async(client, 'owner123')

    assert calls == 3
    assert sleeps == [1, 2]
    assert repos[0].name == 'repo1'