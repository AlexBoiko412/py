from collections import Counter

from repo_schema import Repo
from repos_api_schema import SummaryResponse, LanguageCount


def summarize(repos: list[Repo], username: str) -> SummaryResponse:
    total_repos = len(repos)
    total_stars = sum([repo.stargazers_count for repo in repos])

    languages = [repo.language for repo in repos if repo.language is not None]

    top_languages = [
        LanguageCount(language=lang, repos_count=count)
        for lang, count in Counter(languages).most_common()
    ]

    return SummaryResponse(
        total_repos=total_repos,
        total_stars=total_stars,
        top_languages=top_languages,
        username=username
    )