from pathlib import Path

from pydantic import TypeAdapter

from repo_schema import Repo


def save_repos(repos: list[Repo]):
    _repos_adapter = TypeAdapter(list[Repo])
    Path('repos.json').write_bytes(_repos_adapter.dump_json(repos, indent=2, by_alias=True))