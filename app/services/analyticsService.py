#analyticsService.py
from app.repositories.postgres import Postgres
from app.repositories.pinecone_repo import PineconeRepo


class AnalyticsService:
    def __init__(self):
        self.postgres = Postgres()
        self.pinecone = PineconeRepo()

    def get_insights(self):
        return self.postgres.get_insights()

    def get_business_metrics(self):
        """Métricas de impacto de negocio"""
        return self.postgres.get_business_metrics()

    def get_reuse_stats(self):
        """Estadísticas de reutilización"""
        return self.postgres.get_reuse_stats()

    def get_episodic_memory(self):
        """Memoria episódica desde Pinecone"""
        return self.pinecone.get_episodic_memory()

    def get_semantic_memory(self):
        """Memoria semántica desde Pinecone"""
        return self.pinecone.get_semantic_memory()

