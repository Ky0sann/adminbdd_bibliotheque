from database import SessionLocal
from models.etudiant import Etudiant
from logging_config import get_logger

logger = get_logger(__name__)

class EtudiantRepository:

    @staticmethod
    def create(etudiant: Etudiant):
        session = SessionLocal()
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

    @staticmethod
    def get_all():
        session = SessionLocal()
        return session.query(Etudiant).all()

    @staticmethod
    def delete(id_etud: int):
        session = SessionLocal()
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
    
    @staticmethod
    def update(id_etud: int, nouveau_nom: str, nouveau_prenom: str, nouveau_email: str):
        session = SessionLocal()
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
