from fastapi import FastAPI
app = FastAPI()

from database.connection import Settings

settings = Settings()
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

from route.user import router
from fastapi import Request
from fastapi.templating import Jinja2Templates

app.include_router(router)

templates = Jinja2Templates(directory = "templates/")

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse("main.html",{'request':request})