from database import get_session
from models.livre import Livre
from logging_config import get_logger
'''
Repository pour gérer les livres dans la bibliothèque.
'''

logger = get_logger(__name__)

class LivreRepository:
    def __init__(self, engine):
        self.engine = engine

    def create(self, livre: Livre):
        session = get_session(self.engine)
        try:
            session.add(livre)
            session.commit()
            logger.info(f"Livre ajouté : {livre.isbn}")
        except Exception as e:
            session.rollback()
            logger.error(f"Erreur création livre : {e}")
            raise
        finally:
            session.close()

    def get_all(self):
        session = get_session(self.engine)
        return session.query(Livre).all()
    
    def get_by_isbn(self, isbn: str):
        session = get_session(self.engine)
        return session.get(Livre, isbn)

    def update_exemplaires(self, isbn: str, delta: int):
        session = get_session(self.engine)
        try:
            livre = session.get(Livre, isbn)
            if livre:
                livre.exemplaires_dispo += delta
                session.commit()
                logger.info(
                    f"Mise à jour exemplaires ({isbn}) : {livre.exemplaires_dispo}"
                )
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()

    def delete(self, isbn: str):
        session = get_session(self.engine)
        try:
            livre = session.get(Livre, isbn)
            if livre:
                session.delete(livre)
                session.commit()
                logger.info(f"Livre supprimé : {isbn}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
            
    def update_livre(self, isbn: str, nouveau_titre: str, nouveau_editeur: str, nouvelle_annee: int, nouveaux_exemplaires: int):
        session = get_session(self.engine)
        try:
            livre = session.get(Livre, isbn)
            if livre:
                livre.titre = nouveau_titre
                livre.editeur = nouveau_editeur
                livre.annee = nouvelle_annee
                livre.exemplaires_dispo = nouveaux_exemplaires
                session.commit()
                logger.info(f"Livre mis à jour : {isbn}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
