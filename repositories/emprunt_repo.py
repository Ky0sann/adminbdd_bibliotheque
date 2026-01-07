from database import get_session
from models.emprunt import Emprunt
from logging_config import get_logger
from datetime import date

logger = get_logger(__name__)

class EmpruntRepository:
    def __init__(self, engine):
        self.engine = engine

    def create(self, emprunt: Emprunt):
        session = get_session(self.engine)
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

    def get_actifs(self):
        session = get_session(self.engine)
        return session.query(Emprunt).filter(Emprunt.date_retour == None).all()
    
    def get_all(self):
        session = get_session(self.engine)
        return session.query(Emprunt).all()

    def get_by_id(self, id_emprunt: int):
        session = get_session(self.engine)
        return session.get(Emprunt, id_emprunt)

    def update(self, emprunt: Emprunt):
        session = get_session(self.engine)
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
    
    def supprimer_emprunt(self, id_emprunt: int):
        session = get_session(self.engine)
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
    
    def mettre_a_jour_emprunt(self, id_emprunt: int, date_emprunt : date, date_retour: date, amende: float):
        session = get_session(self.engine)
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
