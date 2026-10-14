from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from github_client import make_async_client

from repos_api import router as repos_router
from stream_api import router as stream_router

from repos_api_exceptions_handler import repos_api_exception_handler


load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with make_async_client() as client:
        app.state.client = client
        yield

app = FastAPI(lifespan=lifespan)

repos_api_exception_handler(app)


app.include_router(repos_router)
app.include_router(stream_router)
