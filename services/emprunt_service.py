from datetime import date, timedelta
from models.emprunt import Emprunt
from repositories.emprunt_repo import EmpruntRepository
from repositories.livre_repo import LivreRepository

DUREE_MAX = 14
AMENDE_PAR_JOUR = 0.50

class EmpruntService:
    def __init__(self, engine):
        self.repo = EmpruntRepository(engine)
        self.livre_repo = LivreRepository(engine)

    def emprunter_livre(self, id_etud: int, isbn: str):
        livre = self.livre_repo.get_by_isbn(isbn)
        if not livre or livre.exemplaires_dispo <= 0:
            raise Exception("Livre indisponible")

        emprunt = Emprunt(
            id_etud=id_etud,
            isbn=isbn,
            date_emprunt=date.today()
        )

        self.repo.create(emprunt)
        self.livre_repo.update_exemplaires(isbn, -1)

    def retourner_livre(self, id_emprunt: int):
        emprunt = self.repo.get_by_id(id_emprunt)

        if not emprunt or emprunt.date_retour:
            raise Exception("Emprunt invalide")

        date_retour = date.today()
        emprunt.date_retour = date_retour

        retard = (date_retour - emprunt.date_emprunt).days - DUREE_MAX
        if retard > 0:
            emprunt.amende = retard * AMENDE_PAR_JOUR

        self.repo.update(emprunt)
        self.livre_repo.update_exemplaires(emprunt.isbn, +1)

    def lister_emprunts_actifs(self):
        return self.repo.get_actifs()
    
    def lister_emprunts(self):
        return self.repo.get_all()
    
    def supprimer_emprunt(self, id_emprunt: int):
        return self.repo.supprimer_emprunt(id_emprunt)
    
    def update_emprunt(self, id_emprunt: int, date_emprunt: date, date_retour: date, amende: float):
        return self.repo.mettre_a_jour_emprunt(id_emprunt, date_emprunt, date_retour, amende)