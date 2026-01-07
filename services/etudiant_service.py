from models.etudiant import Etudiant
from repositories.etudiant_repo import EtudiantRepository

class EtudiantService:

    @staticmethod
    def ajouter_etudiant(nom, prenom, email):
        etudiant = Etudiant(
            nom=nom,
            prenom=prenom,
            email=email
        )
        EtudiantRepository.create(etudiant)

    @staticmethod
    def afficher_etudiants():
        return EtudiantRepository.get_all()
    
    @staticmethod
    def supprimer_etudiant(id_etud: int):
        EtudiantRepository.delete(id_etud)
    
    @staticmethod
    def mettre_a_jour_etudiant(id_etud: int, nouveau_nom: str, nouveau_prenom: str, nouveau_email: str):
        session = EtudiantRepository.update(id_etud, nouveau_nom, nouveau_prenom, nouveau_email)