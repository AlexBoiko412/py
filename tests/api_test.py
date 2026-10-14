import httpx
import pytest
from fastapi.testclient import TestClient

from api import app
from deps import get_client
from tests.github_client_test import create_mock_client




def test_repos(github_response_data):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=200, json=github_response_data)

    app.dependency_overrides[get_client] = lambda: create_mock_client(handler)

    tc = TestClient(app)
    response = tc.get('/repos?username=alex')
    assert response.status_code == 200
    assert response.json()[0]['full_name'] == 'alex/0days-in-the-wild'
    assert len(response.json()) == 100

def test_summary(github_response_data):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=200, json=github_response_data)

    app.dependency_overrides[get_client] = lambda: create_mock_client(handler)

    tc = TestClient(app)
    response = tc.post('/repos/summary', json={'username': 'alex'})
    assert response.status_code == 200
    assert response.json()['username'] == 'alex'
    assert response.json()['total_repos'] == 100
    assert response.json()['total_stars'] == 456

@pytest.mark.parametrize(
    'handler_status,headers,return_status,message',
    [
        (404, {}, 404, "not found"),
        (401, {}, 502, "Not authorized"),
        (403, {}, 502, "Access forbidden"),
        (403, {"x-ratelimit-remaining": "0", "x-ratelimit-reset": "1791900240"}, 429, "Rate limit"),
        (429, {"x-ratelimit-remaining": "0"}, 429, "later"),
    ],
)
def test_summarize_failed(handler_status, headers, return_status, message):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=handler_status, headers=headers)

    app.dependency_overrides[get_client] = lambda: create_mock_client(handler)

    tc = TestClient(app)
    response = tc.post('/repos/summary', json={'username': 'alex'})
    assert response.status_code == return_status

    for key, value in headers.items():
        assert response.headers[key] == value

    data = response.json()

    assert message in data['message']

def test_headers_truncated():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=403, headers={
            "x-ratelimit-remaining": "0",
            "x-ratelimit-reset": "1791900240",
            "x-meta_data": "data"
        })

    app.dependency_overrides[get_client] = lambda: create_mock_client(handler)

    tc = TestClient(app)
    response = tc.post('/repos/summary', json={'username': 'alex'})
    assert response.status_code == 429

    headers_keys = response.headers.keys()

    assert 'x-meta_data' not in headers_keys
    assert 'x-ratelimit-remaining' in headers_keys
    assert 'x-ratelimit-reset' in headers_keys

    data = response.json()

    assert 'Rate limit' in data['message']

def test_username_validation_failed(successful_summary):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=200, json=successful_summary)

    app.dependency_overrides[get_client] = lambda: create_mock_client(handler)

    tc = TestClient(app)
    response = tc.post('/repos/summary', json={'username': ''})

    assert response.status_code == 422

    loc = response.json()['detail'][0]['loc']
    assert 'body' in loc
    assert 'username' in loc

def test_stream(monkeypatch: pytest.MonkeyPatch):
    async def fake_sleep(seconds: int):
        pass

    monkeypatch.setattr('stream_api.asyncio.sleep', fake_sleep)

    tc = TestClient(app)
    with tc.stream('GET', '/stream') as r:
        lines = [l for l in r.iter_lines() if l]
        assert lines[0] == "data: tick 1"
        assert len(lines) == 8