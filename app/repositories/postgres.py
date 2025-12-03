# postgres.py
from app.core.database import get_conn


class Postgres:
    def __init__(self):
        self.conn = get_conn()

    def get_insights(self):
        query = """
        SELECT
            case_type,
            success,
            metadata->>'fecha' AS fecha
        FROM procedural_memory;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
        return rows

    def get_fields(self):
        query = """
        SELECT 
            column_name, 
            data_type
        FROM information_schema.columns
        WHERE table_name = 'procedural_memory';
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
        return rows

    def get_vector(self):
        query = """
        SELECT 
            id
        FROM procedural_memory;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
        return rows