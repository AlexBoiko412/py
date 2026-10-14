import httpx

from fastapi import Request

def get_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.client