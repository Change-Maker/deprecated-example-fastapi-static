# import io
import os

import aiofiles
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse, Response
from pydantic import BaseModel

_WORKING_DIR = os.path.realpath(os.path.dirname(__file__))
_EXAMPLE_HTML_PATH = os.path.realpath(
    os.path.join(_WORKING_DIR, "../../client/example.html"),
)
_STORES_DIR = os.path.realpath(os.path.join(_WORKING_DIR, "../stores"))
_users = []

router = APIRouter(
    prefix="/example",
    tags=["example"],
)


def to_lower_camel(string: str) -> str:
    return (
        "".join(
            [
                s.capitalize() if i > 0 else s
                for i, s in enumerate(string.split("_"))
            ]
        )
    )


class User(BaseModel):
    name: str
    age: int
    is_verified: bool

    class Config:
        alias_generator = to_lower_camel

        # This make User model accept constructing with snake case
        # attributes.
        # Without this, `User(name="alfa", age=14, is_verified=True)`
        # will raise an error which says `isVerified` field is required.
        allow_population_by_field_name = True


class Result(BaseModel):
    success: bool
    msg: str | None


@router.get("")
async def example_page():
    async with aiofiles.open(_EXAMPLE_HTML_PATH, "r") as f:
        return HTMLResponse(content=await f.read(), status_code=200)


@router.get("/users")
async def get_users() -> list[User]:
    return _users


@router.post("/user")
async def add_user(user: User, resp: Response) -> Result:
    if next((u for u in _users if u.name == user.name), None) is None:
        _users.append(user)
        return Result(success=True, msg=None)
    else:
        resp.status_code = 409  # Conflict.
        return Result(success=False, msg="User already exists.")


@router.post("/txt-file")
async def receive_txt_file(file: UploadFile = File(..., alias="txtFile")):
    # # Handle a file without saving it into disk.
    # buffer = io.BytesIO()
    # buffer.write(await file.read())
    # buffer.seek(0)  # Set the stream's position back to the start.
    # # Handling...
    # buffer.close()

    out_file_path = os.path.join(_STORES_DIR, file.filename)
    CHUNK_SIZE = 1024

    # # Load entire file into memory and write to disk.
    # async with aiofiles.open(out_file_path, "wb") as f:
    #     await f.write(await file.read())

    # Write files in the chunked manner.
    async with aiofiles.open(out_file_path, "wb") as f:
        while chunk := await file.read(CHUNK_SIZE):
            await f.write(chunk)

    return Result(success=True, msg=None)
