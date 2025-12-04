#postgres.py
from app.core.database import get_conn
import random


class Postgres:
    def __init__(self):
        self.conn = get_conn()

    def get_insights(self):
        """Obtiene case_type, success, fecha"""
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

    def get_business_metrics(self):
        """
        Obtiene métricas de negocio: times_used, tiempo promedio, ahorro, etc.
        Mockea datos que no existen en la BD
        """
        query = """
        SELECT
            case_type,
            success,
            times_used,
            created_at,
            metadata->>'fecha' AS fecha
        FROM procedural_memory
        ORDER BY created_at DESC;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()

        # Enriquecer con datos mockeados
        enriched_data = []
        for row in rows:
            case_type, success, times_used, created_at, fecha = row

            # Mockear datos de negocio
            processing_time = random.uniform(2, 8) if success else random.uniform(10, 20)  # minutos
            manual_time = random.uniform(15, 45)  # tiempo manual en minutos
            satisfaction = random.uniform(4.0, 5.0) if success else random.uniform(2.0, 3.5)  # escala 1-5
            cost_per_hour = 25000  # COP por hora de agente

            # Calcular ahorros
            time_saved = manual_time - processing_time
            money_saved = (time_saved / 60) * cost_per_hour

            enriched_data.append({
                'case_type': case_type,
                'success': success,
                'times_used': times_used or 0,
                'created_at': created_at.isoformat() if created_at else None,
                'fecha': fecha,
                'processing_time': round(processing_time, 2),
                'manual_time': round(manual_time, 2),
                'time_saved': round(time_saved, 2),
                'money_saved': round(money_saved, 2),
                'satisfaction': round(satisfaction, 1)
            })

        return enriched_data

    def get_reuse_stats(self):
        """Estadísticas de reutilización de soluciones"""
        query = """
        SELECT
            case_type,
            AVG(times_used) as avg_reuse,
            MAX(times_used) as max_reuse,
            COUNT(*) as total_cases
        FROM procedural_memory
        GROUP BY case_type
        ORDER BY avg_reuse DESC;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
        return [
            {
                'case_type': row[0],
                'avg_reuse': float(row[1]) if row[1] else 0,
                'max_reuse': row[2] or 0,
                'total_cases': row[3]
            }
            for row in rows
        ]

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