# GitHub Repos API

A small FastAPI service that reads a GitHub user's public repositories,
validates them with Pydantic, and returns a summary. Built as a learning project.

## Setup
    uv sync
    cp .env.example .env     # set GITHUB_TOKEN (optional, raises the rate limit)

## Run
    uvicorn api:app --reload          # API, docs at http://localhost:8000/docs
    python main.py <github-username>  # CLI, also writes repos.json

## Test
    pytest

## Endpoints
| Method | Path             | Description                                   |
|--------|------------------|-----------------------------------------------|
| GET    | /repos?username= | Validated list of the user's repos            |
| POST   | /repos/summary   | Total repos, total stars, repos per language  |
| GET    | /stream          | Server-Sent Events demo (one tick per second) |

## Errors
| Cause                                    | Status |
|------------------------------------------|--------|
| User not found                           | 404    |
| GitHub rate limit (includes x-ratelimit headers) | 429 |
| Bad token or invalid data from GitHub    | 502    |
| GitHub unreachable or timed out          | 504    |

Error body: `{"message": "<description>"}`

## Design notes
- One shared `httpx.AsyncClient`, created at startup and injected with `Depends`.
- GitHub responses are validated with Pydantic, so bad data fails with a clear error.
- Tests use `httpx.MockTransport`, so they never touch the network.