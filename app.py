from services.etudiant_service import EtudiantService
from logging_config import get_logger
from database import Base, engine

logger = get_logger(__name__)

def menu():
    print("""
1. Ajouter un étudiant
2. Lister les étudiants
3. Supprimer un étudiant
4. Mettre à jour un étudiant
0. Quitter
""")

def main():
    Base.metadata.create_all(engine)
    logger.info("Application démarrée")

    while True:
        menu()
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            email = input("Email : ")
            EtudiantService.ajouter_etudiant(nom, prenom, email)

        elif choix == "2":
            etudiants = EtudiantService.afficher_etudiants()
            for e in etudiants:
                print(f"{e.id_etud} - {e.nom} {e.prenom} ({e.email})")
        
        elif choix == "3":
            id_etud = int(input("ID de l'étudiant à supprimer : "))
            EtudiantService.supprimer_etudiant(id_etud)
        
        elif choix == "4":
            id_etud = int(input("ID de l'étudiant à mettre à jour : "))
            nouveau_nom = input("Nouveau nom : ")
            nouveau_prenom = input("Nouveau prénom : ")
            nouveau_email = input("Nouvel email : ")
            EtudiantService.mettre_a_jour_etudiant(id_etud, nouveau_nom, nouveau_prenom, nouveau_email)

        elif choix == "0":
            logger.info("Application arrêtée")
            break

        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()
