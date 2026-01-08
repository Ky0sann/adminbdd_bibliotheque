import os
from dotenv import load_dotenv

load_dotenv() # Charge les variables d'environnement depuis le fichier .env

DB_CONFIG = { # Configuration de la base de données
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

DATABASE_URL = ( # URL de connexion à la base de données
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO") # Niveau de log par défaut est INFO
