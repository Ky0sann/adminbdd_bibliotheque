from sqlalchemy import Column, Integer, String, Date, Numeric
from database import Base
'''
Entité représentant un étudiant dans la bibliothèque.
'''
class Etudiant(Base):
    __tablename__ = "etudiant"

    id_etud = Column(Integer, primary_key=True) # Identifiant unique de l'étudiant
    nom = Column(String(50), nullable=False) # Nom de l'étudiant
    prenom = Column(String(50), nullable=False) # Prénom de l'étudiant
    email = Column(String(100), unique=True, nullable=False) # Email de l'étudiant
    date_inscription = Column(Date) # Date d'inscription de l'étudiant
    solde_amende = Column(Numeric(5, 2), default=0) # Solde des amendes de l'étudiant
