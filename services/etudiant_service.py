from models.etudiant import Etudiant
from repositories.etudiant_repo import EtudiantRepository

class EtudiantService:
    def __init__(self, engine):
        self.repo = EtudiantRepository(engine)

    def ajouter_etudiant(self, nom, prenom, email):
        etudiant = Etudiant(
            nom=nom,
            prenom=prenom,
            email=email
        )
        self.repo.create(etudiant)

    def afficher_etudiants(self):
        return self.repo.get_all()
    
    def supprimer_etudiant(self, id_etud: int):
        self.repo.delete(id_etud)
    
    def mettre_a_jour_etudiant(self, id_etud: int, nouveau_nom: str, nouveau_prenom: str, nouveau_email: str):
        self.repo.update(id_etud, nouveau_nom, nouveau_prenom, nouveau_email)