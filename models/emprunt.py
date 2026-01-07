from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from database import Base

class Emprunt(Base):
    __tablename__ = "emprunt"

    id_emprunt = Column(Integer, primary_key=True)
    id_etud = Column(Integer, ForeignKey("etudiant.id_etud"))
    isbn = Column(String(13), ForeignKey("livre.isbn"))
    date_emprunt = Column(Date, nullable=False)
    date_retour = Column(Date)
    amende = Column(Numeric(5, 2), default=0)
