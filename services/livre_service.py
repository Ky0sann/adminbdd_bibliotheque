from models.livre import Livre
from repositories.livre_repo import LivreRepository

class LivreService:
    def __init__(self, engine):
        self.repo = LivreRepository(engine)

    def ajouter_livre(self, isbn, titre, editeur, annee, exemplaires):
        livre = Livre(
            isbn=isbn,
            titre=titre,
            editeur=editeur,
            annee=annee,
            exemplaires_dispo=exemplaires
        )
        self.repo.create(livre)

    def lister_livres(self):
        return self.repo.get_all()
    
    def obtenir_livre_par_isbn(self,isbn):
        return self.repo.get_by_isbn(isbn)

    def supprimer_livre(self, isbn):
        self.repo.delete(isbn)
    
    def mettre_a_jour_exemplaires(self,isbn: str, delta: int):
        self.repo.update_exemplaires(isbn, delta)
    
    def modifier_livre(self,isbn: str, nouveau_titre: str, nouveau_editeur: str, nouvelle_annee: int, nouveaux_exemplaires: int):
        self.repo.update_livre(isbn, nouveau_titre, nouveau_editeur, nouvelle_annee, nouveaux_exemplaires)