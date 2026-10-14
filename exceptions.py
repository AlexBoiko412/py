from pydantic_core import ErrorDetails


class GithubError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class UserNotFoundError(GithubError):
    pass

class AuthError(GithubError):
    pass

class RateLimitError(GithubError):
    def __init__(self, message: str, headers: dict[str, str]) -> None:
        super().__init__(message)
        self.headers = headers

class GitHubConnectionError(GithubError):
    pass

class ReposValidationError(GithubError):
    def __init__(self, errors: list[ErrorDetails]) -> None:
        self.errors = errors
        super().__init__(f'{len(errors)} validation errors in GitHub response encountered')