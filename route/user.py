from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()
templates = Jinja2Templates(directory = "templates/")

# problems.html 연결
@router.get("/problems")
async def problems(request:Request):
    return templates.TemplateResponse(name="/users/problems.html",context={'request':request})

# list.html 연결

# reads.html 연결

# main.html 연결