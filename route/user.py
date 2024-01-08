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
@router.post("/lists")
async def lists(request:Request):
    return templates.TemplateResponse(name="/users/lists.html",context={'request':request})

# reads.html 연결
@router.post("/reads")
async def reads(request:Request):
    return templates.TemplateResponse(name="users/reads.html",context={'request':request})

# main.html 연결
@router.get("/main")
async def main(request:Request):
    return templates.TemplateResponse(name="users/main.html",context={'request':request})