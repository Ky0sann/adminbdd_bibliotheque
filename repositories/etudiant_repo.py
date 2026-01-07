from database import get_session
from models.etudiant import Etudiant
from logging_config import get_logger

logger = get_logger(__name__)

class EtudiantRepository:
    def __init__(self, engine):
        self.engine = engine

    def create(self, etudiant: Etudiant):
        session = get_session(self.engine)
        try:
            session.add(etudiant)
            session.commit()
            logger.info(f"Étudiant ajouté : {etudiant.email}")
        except Exception as e:
            session.rollback()
            logger.error(f"Erreur création étudiant : {e}")
            raise
        finally:
            session.close()

    def get_all(self):
        session = get_session(self.engine)
        return session.query(Etudiant).all()

    def delete(self, id_etud: int):
        session = get_session(self.engine)
        try:
            etud = session.get(Etudiant, id_etud)
            if etud:
                session.delete(etud)
                session.commit()
                logger.info(f"Étudiant supprimé : {id_etud}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
    
    def update(self, id_etud: int, nouveau_nom: str, nouveau_prenom: str, nouveau_email: str):
        session = get_session(self.engine)
        try:
            etud = session.get(Etudiant, id_etud)
            if etud:
                etud.nom = nouveau_nom
                etud.prenom = nouveau_prenom
                etud.email = nouveau_email
                session.commit()
                logger.info(f"Étudiant mis à jour : {id_etud}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
