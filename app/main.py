#main.py
from fastapi import FastAPI
from app.routers.analyticsRouter import router as analytics_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(analytics_router, prefix="/api")
app.mount("/static", StaticFiles(directory="static"), name="static")
