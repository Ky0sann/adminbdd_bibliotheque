from database import get_session
from models.emprunt import Emprunt
from logging_config import get_logger
from datetime import date
'''
Repository pour gérer les emprunts dans la bibliothèque.
'''
logger = get_logger(__name__) # Logger pour le module emprunt_repo

class EmpruntRepository:
    def __init__(self, engine): # Initialisation du repository avec le moteur de base de données
        self.engine = engine

    def create(self, emprunt: Emprunt): # Crée un nouvel emprunt dans la base de données
        session = get_session(self.engine) # Obtient une session de base de données
        try:
            session.add(emprunt) # Ajoute l'emprunt à la session
            session.commit() # Valide la transaction 
            logger.info( # Log l'opération de création
                f"Emprunt créé : étudiant {emprunt.id_etud}, livre {emprunt.isbn}"
            )
        except Exception as e: # Gestion des exceptions
            session.rollback() # Annule la transaction en cas d'erreur
            logger.error(f"Erreur emprunt : {e}") # Log l'erreur
            raise # Relance l'exception
        finally:
            session.close() # Ferme la session

    def get_actifs(self): # Récupère tous les emprunts actifs
        session = get_session(self.engine)
        return session.query(Emprunt).filter(Emprunt.date_retour == None).all()
    
    def get_all(self): # Récupère tous les emprunts
        session = get_session(self.engine)
        return session.query(Emprunt).all() # Retourne tous les emprunts

    def get_by_id(self, id_emprunt: int): # Récupère un emprunt par son identifiant
        session = get_session(self.engine)
        return session.get(Emprunt, id_emprunt) # Retourne l'emprunt correspondant à l'ID

    def update(self, emprunt: Emprunt): # Met à jour un emprunt existant
        session = get_session(self.engine)
        try:
            session.merge(emprunt) # Fusionne les modifications de l'emprunt
            session.commit()
            logger.info(f"Emprunt mis à jour : {emprunt.id_emprunt}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
    
    def supprimer_emprunt(self, id_emprunt: int): # Supprime un emprunt par son identifiant
        session = get_session(self.engine)
        try:
            emprunt = session.get(Emprunt, id_emprunt)
            if emprunt:
                session.delete(emprunt) # Supprime l'emprunt de la session
                session.commit()
                logger.info(f"Emprunt supprimé : {id_emprunt}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
    
    def mettre_a_jour_emprunt(self, id_emprunt: int, date_emprunt : date, date_retour: date, amende: float): # Met à jour les détails d'un emprunt
        session = get_session(self.engine)
        try:
            emprunt = session.get(Emprunt, id_emprunt) # Récupère l'emprunt par son ID
            if emprunt:
                emprunt.date_emprunt = date_emprunt # Met à jour la date d'emprunt
                emprunt.date_retour = date_retour # Met à jour la date de retour
                emprunt.amende = amende # Met à jour l'amende
                session.commit() # Valide les modifications
                logger.info(f"Emprunt mis à jour : {id_emprunt}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
