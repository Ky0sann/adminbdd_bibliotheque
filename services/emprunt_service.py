from datetime import date, timedelta
from models.emprunt import Emprunt
from repositories.emprunt_repo import EmpruntRepository
from repositories.livre_repo import LivreRepository

DUREE_MAX = 14
AMENDE_PAR_JOUR = 0.50

class EmpruntService:

    @staticmethod
    def emprunter_livre(id_etud: int, isbn: str):
        livre = LivreRepository.get_by_isbn(isbn)

        if not livre or livre.exemplaires_dispo <= 0:
            raise Exception("Livre indisponible")

        emprunt = Emprunt(
            id_etud=id_etud,
            isbn=isbn,
            date_emprunt=date.today()
        )

        EmpruntRepository.create(emprunt)
        LivreRepository.update_exemplaires(isbn, -1)

    @staticmethod
    def retourner_livre(id_emprunt: int):
        emprunt = EmpruntRepository.get_by_id(id_emprunt)

        if not emprunt or emprunt.date_retour:
            raise Exception("Emprunt invalide")

        date_retour = date.today()
        emprunt.date_retour = date_retour

        retard = (date_retour - emprunt.date_emprunt).days - DUREE_MAX
        if retard > 0:
            emprunt.amende = retard * AMENDE_PAR_JOUR

        EmpruntRepository.update(emprunt)
        LivreRepository.update_exemplaires(emprunt.isbn, +1)

    @staticmethod
    def lister_emprunts_actifs():
        return EmpruntRepository.get_actifs()
    
    @staticmethod
    def lister_emprunts():
        return EmpruntRepository.get_all()
    
    @staticmethod
    def supprimer_emprunt(id_emprunt: int):
        return EmpruntRepository.supprimer_emprunt(id_emprunt)
    
    @staticmethod 
    def update_emprunt(id_emprunt: int, date_emprunt: date, date_retour: date, amende: float):
        return EmpruntRepository.mettre_a_jour_emprunt(id_emprunt, date_emprunt, date_retour, amende)