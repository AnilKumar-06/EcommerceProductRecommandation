from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    ASTRADB_API_ENDPOINT=os.getenv("ASTRADB_API_ENDPOINT")
    ASTRADB_KEYSPACE=os.getenv("ASTRADB_KEYSPACE")
    HF_TOKEN=os.getenv("HF_TOKEN")