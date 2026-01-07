from services.etudiant_service import EtudiantService
from services.livre_service import LivreService
from services.emprunt_service import EmpruntService
from logging_config import get_logger
from database import Base, engine

logger = get_logger(__name__)

def menu():
    print("""
1. Ajouter un étudiant
2. Lister les étudiants
3. Supprimer un étudiant
4. Mettre à jour un étudiant
5. Ajouter un livre
6. Lister les livres
7. Emprunter un livre
8. Retourner un livre
9. Lister les emprunts actifs
10. Supprimer un livre
11. Modifier un livre
12. Supprimer un emprunt
13. Mettre à jour un emprunt
14. Lister tous les emprunts
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
        
        elif choix == "5":
            isbn = input("ISBN : ")
            titre = input("Titre : ")
            editeur = input("Éditeur : ")
            annee = int(input("Année : "))
            exemplaires = int(input("Nombre d'exemplaires : "))
            LivreService.ajouter_livre(isbn, titre, editeur, annee, exemplaires)
        
        elif choix == "6":
            livres = LivreService.lister_livres()
            for l in livres:
                print(f"{l.isbn} - {l.titre} ({l.annee}) - {l.exemplaires_dispo} exemplaires disponibles")
        
        elif choix == "7":
            id_etud = int(input("ID étudiant : "))
            isbn = input("ISBN du livre : ")
            EmpruntService.emprunter_livre(id_etud, isbn)
        
        elif choix == "8":
            id_emprunt = int(input("ID de l'emprunt : "))
            EmpruntService.retourner_livre(id_emprunt)
            
        elif choix == "9":
            emprunts = EmpruntService.lister_emprunts_actifs()
            for emp in emprunts:
                print(f"Emprunt ID: {emp.id_emprunt}, Étudiant ID: {emp.id_etud}, ISBN: {emp.isbn}, Date d'emprunt: {emp.date_emprunt}")
        
        elif choix == "10":
            isbn = input("ISBN du livre à supprimer : ")
            LivreService.supprimer_livre(isbn)
            print(f"Livre avec ISBN {isbn} supprimé.")
        
        elif choix == "11":
            isbn = input("ISBN du livre à modifier : ")
            nouveau_titre = input("Nouveau titre : ")
            nouveau_editeur = input("Nouvel éditeur : ")
            nouvelle_annee = int(input("Nouvelle année : "))
            nouveaux_exemplaires = int(input("Nouveau nombre d'exemplaires : "))
            LivreService.modifier_livre(isbn, nouveau_titre, nouveau_editeur, nouvelle_annee, nouveaux_exemplaires)
            print(f"Livre avec ISBN {isbn} modifié.")
        
        elif choix == "12":
            id_emprunt = int(input("ID de l'emprunt à supprimer : "))
            EmpruntService.supprimer_emprunt(id_emprunt)
            print(f"Emprunt avec ID {id_emprunt} supprimé.")
        
        elif choix == "13":
            id_emprunt = int(input("ID de l'emprunt à mettre à jour : "))
            date_emprunt = input("Nouvelle date d'emprunt (YYYY-MM-DD) : ")
            date_retour = input("Nouvelle date de retour (YYYY-MM-DD) : ")
            amende = float(input("Nouvelle amende : "))
            EmpruntService.update_emprunt(id_emprunt, date_emprunt, date_retour, amende)
            print(f"Emprunt avec ID {id_emprunt} mis à jour.")
        
        elif choix == "14":
            emprunts = EmpruntService.lister_emprunts()
            for emp in emprunts:
                print(f"Emprunt ID: {emp.id_emprunt}, Étudiant ID: {emp.id_etud}, ISBN: {emp.isbn}, Date d'emprunt: {emp.date_emprunt}, Date de retour: {emp.date_retour}, Amende: {emp.amende}")
                
        elif choix == "0":
            logger.info("Application arrêtée")
            break

        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()
