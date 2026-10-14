import asyncio

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()

async def ticker():
    for i in range(1, 9):
        yield f'data: tick {i}\n\n'
        await asyncio.sleep(1)

@router.get("/stream")
async def stream():
    return StreamingResponse(
        ticker(),
        media_type="text/event-stream"
    )