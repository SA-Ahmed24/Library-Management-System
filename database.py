import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        dbname="library_db",
        user="postgres",
        password="Aitchison@24",
        host="localhost"
    )
    return conn
