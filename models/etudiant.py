from sqlalchemy import Column, Integer, String, Date, Numeric
from database import Base

class Etudiant(Base):
    __tablename__ = "etudiant"

    id_etud = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_inscription = Column(Date)
    solde_amende = Column(Numeric(5, 2), default=0)
