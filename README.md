# Application de gestion de bibliothèque

Application Python en ligne de commande permettant de gérer une bibliothèque de livres, avec gestion des livres, des utilisateurs et des emprunts. 

L'application utilise PostgreSQL comme base de données et psycopg2 + SQLAlchemy pour gérer la connexion, l'interaction et le mapping objet-relationnel avec la base de données.

## Fonctionnalités

- Ajouter, modifier et supprimer des livres, emprunts et utilisateurs.
- Faire un emprunt et retour d'un livre.
- Gestion des logs et des erreurs.

---

## Prérequis

- Python 3.9+  
- PostgreSQL  
- Bibliothèques Python : `psycopg2` et `SQLAlchemy`  

---

## Installation des dépendances

Assurez-vous d’installer les deux bibliothèques suivantes dans votre environnement Python :  

- `psycopg2` : pour la connexion à PostgreSQL  
- `SQLAlchemy` : pour la gestion ORM  

---

## Configuration

Avant de lancer l'application, créez un fichier `.env` à la racine du projet avec le contenu suivant :  
- DB_HOST=localhost : Adresse de votre serveur PostgreSQL
- DB_PORT=5432 : Port utilisé par PostgreSQL
- DB_NAME=nomdelabdd : Nom de votre base de données
- DB_USER=utilisateurdelabdd : Nom d'utilisateur PostgreSQL
- DB_PASSWORD=motdepassedelabdd : Mot de passe PostgreSQL
- LOG_LEVEL=INFO : Niveau de logs (INFO, WARNING, ERROR)
---
