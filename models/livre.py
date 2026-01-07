from sqlalchemy import Column, String, Integer
from database import Base

class Livre(Base):
    __tablename__ = "livre"

    isbn = Column(String(13), primary_key=True)
    titre = Column(String(200), nullable=False)
    editeur = Column(String(100))
    annee = Column(Integer)
    exemplaires_dispo = Column(Integer, default=1)
