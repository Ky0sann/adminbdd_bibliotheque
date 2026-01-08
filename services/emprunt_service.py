from datetime import date, timedelta
from models.emprunt import Emprunt
from repositories.emprunt_repo import EmpruntRepository
from repositories.livre_repo import LivreRepository
'''
Service pour gérer les emprunts dans la bibliothèque.
'''
DUREE_MAX = 14 # Durée maximale d'emprunt en jours
AMENDE_PAR_JOUR = 0.50 # Amende par jour de retard

class EmpruntService:
    def __init__(self, engine): # Initialisation du service avec le moteur de base de données
        self.repo = EmpruntRepository(engine) # Repository des emprunts
        self.livre_repo = LivreRepository(engine) # Repository des livres

    def emprunter_livre(self, id_etud: int, isbn: str): # Emprunte un livre pour un étudiant
        livre = self.livre_repo.get_by_isbn(isbn) # Récupère le livre par son ISBN
        if not livre or livre.exemplaires_dispo <= 0: # Vérifie la disponibilité du livre
            raise Exception("Livre indisponible") # Lève une exception si le livre n'est pas disponible

        emprunt = Emprunt( # Crée un nouvel emprunt
            id_etud=id_etud,
            isbn=isbn,
            date_emprunt=date.today()
        )

        self.repo.create(emprunt) # Enregistre l'emprunt dans la base de données
        self.livre_repo.update_exemplaires(isbn, -1) # Décrémente le nombre d'exemplaires disponibles

    def retourner_livre(self, id_emprunt: int): # Retourne un livre emprunté
        emprunt = self.repo.get_by_id(id_emprunt) # Récupère l'emprunt par son ID

        if not emprunt or emprunt.date_retour: # Vérifie si l'emprunt est valide et non déjà retourné
            raise Exception("Emprunt invalide") # Lève une exception si l'emprunt est invalide

        date_retour = date.today() # Date de retour du livre
        emprunt.date_retour = date_retour # Met à jour la date de retour

        retard = (date_retour - emprunt.date_emprunt).days - DUREE_MAX # Calcule le nombre de jours de retard
        if retard > 0:
            emprunt.amende = retard * AMENDE_PAR_JOUR # Calcule l'amende en fonction du retard

        self.repo.update(emprunt) # Met à jour l'emprunt dans la base de données
        self.livre_repo.update_exemplaires(emprunt.isbn, +1) # Incrémente le nombre d'exemplaires disponibles

    def lister_emprunts_actifs(self): # Liste tous les emprunts actifs (non retournés)
        return self.repo.get_actifs() 
    
    def lister_emprunts(self): # Liste tous les emprunts 
        return self.repo.get_all()
    
    def supprimer_emprunt(self, id_emprunt: int): # Supprime un emprunt
        return self.repo.supprimer_emprunt(id_emprunt)
    
    def update_emprunt(self, id_emprunt: int, date_emprunt: date, date_retour: date, amende: float): #Mettre à jour un emprunt
        return self.repo.mettre_a_jour_emprunt(id_emprunt, date_emprunt, date_retour, amende)