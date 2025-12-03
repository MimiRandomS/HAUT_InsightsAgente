#database.py
import psycopg
import os
from app.core.config import POSTGRES_URI

def get_conn():
    if POSTGRES_URI is None:
        raise Exception("POSTGRES_URI not set")
    return psycopg.connect(os.getenv("POSTGRES_URI"))
