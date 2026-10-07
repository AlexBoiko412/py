import os
from typing import Any

import httpx
from dotenv import load_dotenv
import argparse


def get_repos_star_counts_for_username(username: str) -> list[dict[str, Any]]:
    try:
        response = httpx.get(
            f'https://api.github.com/users/{username}/repos',
            timeout=10,
            headers={'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}'},
            params={"per_page": 100, "page": 1}
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as err:
        print(err)
        return []

def print_repos(repos: list[dict[str, int]]):
    for repo in repos:
        print(f'Name: {repo["full_name"]}, stars count: {repo["stargazers_count"]}')


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "username",
        type=str,
        help="GitHub username"
    )

    args = parser.parse_args()

    repos = get_repos_star_counts_for_username(args.username)
    print_repos(repos)

if __name__ == "__main__":
    main()