import os

import aiofiles
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

_WORKING_DIR = os.path.realpath(os.path.dirname(__file__))
_EXAMPLE_HTML_PATH = os.path.realpath(
    os.path.join(_WORKING_DIR, "../../client/example.html"),
)

router = APIRouter(
    prefix="/example",
    tags=["example"],
)


@router.get("")
async def example_page():
    async with aiofiles.open(_EXAMPLE_HTML_PATH, "r") as f:
        return HTMLResponse(content=await f.read(), status_code=200)
