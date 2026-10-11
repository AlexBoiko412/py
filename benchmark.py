import asyncio
import time

from dotenv import load_dotenv

from exceptions import GithubError
from github_client import fetch_repos_async, make_async_client


async def benchmark(usernames: list[str]) -> None:
    async with make_async_client() as client:
        users_seq = []

        start = time.perf_counter()
        for username in usernames:
            try:
                users_seq.append(await fetch_repos_async(client, username))
            except GithubError as err:
                users_seq.append(err)
        print(f'Sequential: {time.perf_counter() - start:.2f}')

        for user in users_seq:
            print(user)

        start = time.perf_counter()
        users = await asyncio.gather(
            *(fetch_repos_async(client, username) for username in usernames),
            return_exceptions=True
        )
        print(f'Parallel: {time.perf_counter() - start:.2f}')

        for user in users:
            print(user)

if __name__ == '__main__':
    load_dotenv()

    asyncio.run(
        benchmark([
            'AlexBoiko412',
            'AlexBoiko412',
            'AlexBoiko412',
            'AlexBoiko412',
            'AlexBoiko412asdqwdqw131',
        ])
    )