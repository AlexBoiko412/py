import fastapi
from fastapi.responses import JSONResponse

from exceptions import UserNotFoundError, RateLimitError, AuthError, ReposValidationError, GitHubConnectionError

def repos_api_exception_handler(app: fastapi.FastAPI) -> None:
    @app.exception_handler(UserNotFoundError)
    async def user_not_found(request, exc: UserNotFoundError):
        return JSONResponse(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            content={"message": str(exc)}
        )

    @app.exception_handler(RateLimitError)
    async def rate_limit_hit(request, exc: RateLimitError):
        return JSONResponse(
            status_code=fastapi.status.HTTP_429_TOO_MANY_REQUESTS,
            content={"message": str(exc)},
            headers=getattr(exc, "headers", {})
        )

    @app.exception_handler(AuthError)
    @app.exception_handler(ReposValidationError)
    async def error_upstream(request, exc):
        return JSONResponse(
            status_code=fastapi.status.HTTP_502_BAD_GATEWAY,
            content={"message": str(exc)}
        )

    @app.exception_handler(GitHubConnectionError)
    async def upstream_unreachable(request, exc):
        return JSONResponse(
            status_code=fastapi.status.HTTP_504_GATEWAY_TIMEOUT,
            content={"message": str(exc)}
        )

