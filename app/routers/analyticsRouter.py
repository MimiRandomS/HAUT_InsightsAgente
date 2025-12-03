#analyticsRouter.py
from fastapi import APIRouter, Query
from app.services.analyticsService import AnalyticsService

router = APIRouter()
service = AnalyticsService()

@router.get("/insightsPostgres")
def get_insights():
    return service.get_insights()
