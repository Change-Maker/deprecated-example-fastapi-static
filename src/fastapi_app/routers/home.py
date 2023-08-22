from fastapi import APIRouter, Request
from loguru import logger

router = APIRouter()


@router.get("/hello")
async def hello_world(req: Request) -> str:
    logger.info(f"Received request: {req.method} {req.url}")
    return "world"
