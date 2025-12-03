#config.py
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_URI = os.getenv("POSTGRES_URI")
PINECONE_KEY = os.getenv("PINECONE_API_KEY")