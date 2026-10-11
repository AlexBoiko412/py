import sys
import asyncio

from github_client import make_async_client, fetch_repos_async

from exceptions import GithubError, ReposValidationError

from dotenv import load_dotenv
import argparse

from repo_schema import Repo
from save_repos import save_repos

def print_repos(repos: list[Repo]):
    for repo in repos:
        print(f'Name: {repo.full_name}, stars count: {repo.stargazers_count}; {repo.language}, Owner: {repo.owner.username}; {repo.owner.html_url}')


async def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "username",
        type=str,
        help="GitHub username"
    )

    args = parser.parse_args()

    try:
        async with make_async_client() as client:
            repos = await fetch_repos_async(client, args.username)
            save_repos(repos)
            print_repos(repos)
    except ReposValidationError as err:
        print(f'Validation errors {err}', file=sys.stderr)
        for error in err.errors:
            location = '.'.join(str(item) for item in error['loc'])
            print(f' {location}: {error['msg']}', file=sys.stderr)
        sys.exit(1)
    except GithubError as err:
        print(f'Error {err}', file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())