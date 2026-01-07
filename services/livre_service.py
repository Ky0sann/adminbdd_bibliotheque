from models.livre import Livre
from repositories.livre_repo import LivreRepository

class LivreService:

    @staticmethod
    def ajouter_livre(isbn, titre, editeur, annee, exemplaires):
        livre = Livre(
            isbn=isbn,
            titre=titre,
            editeur=editeur,
            annee=annee,
            exemplaires_dispo=exemplaires
        )
        LivreRepository.create(livre)

    @staticmethod
    def lister_livres():
        return LivreRepository.get_all()

    @staticmethod
    def obtenir_livre_par_isbn(isbn):
        return LivreRepository.get_by_isbn(isbn)

    @staticmethod
    def supprimer_livre(isbn):
        LivreRepository.delete(isbn)
    
    @staticmethod
    def mettre_a_jour_exemplaires(isbn: str, delta: int):
        LivreRepository.update_exemplaires(isbn, delta)
    
    @staticmethod
    def modifier_livre(isbn: str, nouveau_titre: str, nouveau_editeur: str, nouvelle_annee: int, nouveaux_exemplaires: int):
        LivreRepository.update_livre(isbn, nouveau_titre, nouveau_editeur, nouvelle_annee, nouveaux_exemplaires)