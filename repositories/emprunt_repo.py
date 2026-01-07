from database import SessionLocal
from models.emprunt import Emprunt
from logging_config import get_logger
from datetime import date

logger = get_logger(__name__)

class EmpruntRepository:

    @staticmethod
    def create(emprunt: Emprunt):
        session = SessionLocal()
        try:
            session.add(emprunt)
            session.commit()
            logger.info(
                f"Emprunt créé : étudiant {emprunt.id_etud}, livre {emprunt.isbn}"
            )
        except Exception as e:
            session.rollback()
            logger.error(f"Erreur emprunt : {e}")
            raise
        finally:
            session.close()

    @staticmethod
    def get_actifs():
        session = SessionLocal()
        return session.query(Emprunt).filter(Emprunt.date_retour == None).all()
    
    @staticmethod
    def get_all():
        session = SessionLocal()
        return session.query(Emprunt).all()

    @staticmethod
    def get_by_id(id_emprunt: int):
        session = SessionLocal()
        return session.get(Emprunt, id_emprunt)

    @staticmethod
    def update(emprunt: Emprunt):
        session = SessionLocal()
        try:
            session.merge(emprunt)
            session.commit()
            logger.info(f"Emprunt mis à jour : {emprunt.id_emprunt}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
    
    @staticmethod
    def supprimer_emprunt(id_emprunt: int):
        session = SessionLocal()
        try:
            emprunt = session.get(Emprunt, id_emprunt)
            if emprunt:
                session.delete(emprunt)
                session.commit()
                logger.info(f"Emprunt supprimé : {id_emprunt}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
    
    @staticmethod
    def mettre_a_jour_emprunt(id_emprunt: int, date_emprunt : date, date_retour: date, amende: float):
        session = SessionLocal()
        try:
            emprunt = session.get(Emprunt, id_emprunt)
            if emprunt:
                emprunt.date_emprunt = date_emprunt
                emprunt.date_retour = date_retour
                emprunt.amende = amende
                session.commit()
                logger.info(f"Emprunt mis à jour : {id_emprunt}")
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise
        finally:
            session.close()
