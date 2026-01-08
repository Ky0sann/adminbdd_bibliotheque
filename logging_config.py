import logging
from config import LOG_LEVEL # Niveau de log défini dans la configuration

logging.basicConfig( # Configuration de base du logging
    level=LOG_LEVEL, # Niveau de log
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", # Format des messages de log
    handlers=[ # Handlers pour écrire les logs dans un fichier et la console
        logging.FileHandler("bibliotheque.log"),
        logging.StreamHandler()
    ]
)

def get_logger(name: str): # Fonction pour obtenir un logger nommé
    return logging.getLogger(name)
