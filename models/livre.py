from sqlalchemy import Column, String, Integer
from database import Base
'''
Entité représentant un livre dans la bibliothèque.
'''
class Livre(Base):
    __tablename__ = "livre"

    isbn = Column(String(13), primary_key=True) # ISBN unique du livre
    titre = Column(String(200), nullable=False) # Titre du livre
    editeur = Column(String(100)) # Éditeur du livre
    annee = Column(Integer) # Année de publication du livre
    exemplaires_dispo = Column(Integer, default=1) # Nombre d'exemplaires disponibles
