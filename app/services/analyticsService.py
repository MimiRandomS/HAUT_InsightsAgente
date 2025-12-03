#analyticsService.py
from app.repositories.postgres import Postgres

class AnalyticsService:
    def __init__(self):
        self.postgres = Postgres()

    def get_insights(self):
        return self.postgres.get_insights()

