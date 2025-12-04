#analyticsRouter.py
from fastapi import APIRouter
from app.services.analyticsService import AnalyticsService

router = APIRouter()
service = AnalyticsService()

@router.get("/insightsPostgres")
def get_insights():
    return service.get_insights()

@router.get("/businessMetrics")
def get_business_metrics():
    """Endpoint para métricas de negocio"""
    return service.get_business_metrics()

@router.get("/reuseStats")
def get_reuse_stats():
    """Endpoint para estadísticas de reutilización"""
    return service.get_reuse_stats()

@router.get("/episodicMemory")
def get_episodic_memory():
    """Endpoint para memoria episódica de Pinecone"""
    return service.get_episodic_memory()

@router.get("/semanticMemory")
def get_semantic_memory():
    """Endpoint para memoria semántica de Pinecone"""
    return service.get_semantic_memory()
