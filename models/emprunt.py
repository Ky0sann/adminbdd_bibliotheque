from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from database import Base
'''
Entité représentant un emprunt dans la bibliothèque.
'''
class Emprunt(Base):
    __tablename__ = "emprunt"

    id_emprunt = Column(Integer, primary_key=True) # Identifiant unique de l'emprunt
    id_etud = Column(Integer, ForeignKey("etudiant.id_etud")) # Identifiant de l'étudiant qui a emprunté le livre
    isbn = Column(String(13), ForeignKey("livre.isbn")) # ISBN du livre emprunté
    date_emprunt = Column(Date, nullable=False) # Date à laquelle le livre a été emprunté
    date_retour = Column(Date) # Date à laquelle le livre a été retourné
    amende = Column(Numeric(5, 2), default=0) # Amende associée à l'emprunt
