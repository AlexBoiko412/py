import os

import httpx
from dotenv import load_dotenv


def get_reps_star_counts_for_username(username: str) -> list[dict[str, int]]:
    load_dotenv()
    try:
        response = httpx.get(
            f'https://api.github.com/users/{username}/repos',
            timeout=10,
            headers={'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}'}
        )
        response.json()
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as err:
        print(err)
        return []

def print_reps(reps: list[dict[str, int]]):
    for repo in reps:
        print(f'Name: {repo['full_name']}, stars count: {repo['stargazers_count']}')


def main():
    reps = get_reps_star_counts_for_username('AlexBoiko412')
    print_reps(reps)

if __name__ == "__main__":
    main()