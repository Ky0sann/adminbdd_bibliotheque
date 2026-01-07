from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from config import DB_CONFIG

def authenticate(username, password):
    try:
        from database import get_engine

        engine = get_engine(
            user=username,
            password=password,
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            dbname=DB_CONFIG["database"]
        )

        with engine.connect() as conn:
            role = conn.execute(text("SELECT current_user")).scalar()

        return engine, role

    except OperationalError:
        return None, None
