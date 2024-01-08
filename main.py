from fastapi import FastAPI
app = FastAPI()

from database.connection import Settings
settings = Settings()
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()
