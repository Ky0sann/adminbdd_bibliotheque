from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from config import DB_CONFIG
'''
Authentification des utilisateurs pour accéder à la base de données.
'''
def authenticate(username, password):
    try:
        from database import get_engine

        engine = get_engine( # Crée une connexion à la base de données
            user=username,
            password=password,
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            dbname=DB_CONFIG["database"]
        )

        with engine.connect() as conn: # Ouvre une connexion
            role = conn.execute(text("SELECT current_user")).scalar()

        return engine, role # Retourne le moteur et le rôle de l'utilisateur

    except OperationalError:
        return None, None
