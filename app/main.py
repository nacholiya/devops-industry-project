from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword")
    )

@app.get("/")
def root():
    return {"message": "Industry Ready DevOps Project"}

@app.get("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}
