import pathlib

from repo_schema import Repo, REPOS_ADAPTER


def save_repos(repos: list[Repo], path: pathlib.Path):
    path.write_bytes(REPOS_ADAPTER.dump_json(repos, indent=2, by_alias=True))