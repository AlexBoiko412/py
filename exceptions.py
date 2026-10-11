from pydantic_core import ErrorDetails


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