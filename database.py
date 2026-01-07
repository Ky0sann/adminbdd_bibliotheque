from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

def get_engine(user, password, host, port, dbname):
    url = (
        f"postgresql+psycopg2://{user}:{password}"
        f"@{host}:{port}/{dbname}"
    )
    return create_engine(url, echo=False)

def get_session(engine):
    return sessionmaker(bind=engine)()

