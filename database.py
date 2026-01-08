from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base() # Base pour les modèles ORM

def get_engine(user, password, host, port, dbname): # Crée et retourne un moteur de base de données
    url = ( 
        f"postgresql+psycopg2://{user}:{password}"
        f"@{host}:{port}/{dbname}"
    )
    return create_engine(url, echo=False)

def get_session(engine): # Crée et retourne une session de base de données
    return sessionmaker(bind=engine)()

